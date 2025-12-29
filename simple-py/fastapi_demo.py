# -*- coding: utf-8 -*-
# 完整FastAPI基础示例（Java SpringBoot 对应版）
# 适用Java开发者快速上手，覆盖所有基础核心场景

# ======================================
# 基础导入
# ======================================
from typing import Union, List, Optional
from pydantic import BaseModel, Field  # 对应Java DTO/Entity + JSR380校验
from fastapi import FastAPI, Query, Path, Body, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware  # 对应SpringBoot CORS配置
from fastapi.responses import JSONResponse, PlainTextResponse  # 对应SpringBoot ResponseEntity

# ======================================
# 1. FastAPI 实例创建（核心入口）
# 对应 SpringBoot：@SpringBootApplication + SpringApplication.run()
# ======================================
# app实例 = Spring容器 + MVC核心配置
app = FastAPI(
    title="Java开发者FastAPI学习示例",  # 对应spring.application.name
    description="覆盖FastAPI所有基础场景，附带SpringBoot概念映射",
    version="1.0.0",
    docs_url="/swagger",  # 对应SpringBoot Swagger-UI（默认/docs，自定义为/swagger）
    redoc_url="/redoc",   # 备用接口文档UI
    openapi_url="/openapi.json"  # OpenAPI规范文件地址
)

# ======================================
# 2. 跨域配置
# 对应 SpringBoot：@CrossOrigin 注解 / WebMvcConfigurer 跨域配置
# ======================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（生产环境请指定具体域名，如["http://localhost:8080"]）
    allow_credentials=True,  # 允许携带Cookie
    allow_methods=["*"],     # 允许所有HTTP方法（GET/POST/PUT/DELETE等）
    allow_headers=["*"],     # 允许所有请求头
)

# ======================================
# 3. 数据模型定义（Pydantic）
# 对应 Java：DTO/Entity 类 + JSR380校验（@NotNull/@Size/@Email等）
# ======================================
# 基础数据模型（用户模型）
class User(BaseModel):
    id: Optional[int] = None  # 可选字段（对应Java Integer类型，允许为null）
    username: str = Field(..., min_length=2, max_length=20, description="用户名，长度2-20")  # 必传字段
    # 对应Java：@NotBlank + @Size(min = 2, max = 20)
    age: int = Field(..., ge=0, le=150, description="年龄，取值范围0-150")  # 必传字段
    # 对应Java：@NotNull + @Min(0) + @Max(150)
    email: Optional[str] = Field(None, pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", description="邮箱（可选）")
    # 对应Java：@Email（可选字段）
    tags: List[str] = Field(default=[], description="用户标签列表，默认空列表")  # 集合类型
    # 对应Java：List<String> tags = new ArrayList<>();

# 嵌套数据模型（订单子项 + 订单主模型）
# 对应Java：嵌套DTO（如 Order 中包含 List<OrderItem>）
class OrderItem(BaseModel):
    product_id: int = Field(..., ge=1, description="商品ID，至少为1")
    quantity: int = Field(..., ge=1, description="购买数量，至少1件")
    price: float = Field(..., gt=0, description="商品单价，大于0")

class Order(BaseModel):
    order_id: Optional[str] = None
    user_id: int = Field(..., ge=1, description="用户ID，至少为1")
    items: List[OrderItem]  # 嵌套列表类型，对应Java List<OrderItem>
    total_amount: Optional[float] = None  # 订单总金额（可选，可通过items计算）

# ======================================
# 4. 依赖注入（Depends）
# 对应 SpringBoot：@Autowired / 构造器注入 / @RequestHeader / 公共逻辑抽取
# ======================================
def get_token_header(
    token: Optional[str] = Header(None, alias="Authorization", description="请求头Token，格式：Bearer xxx")
):
    """
    公共依赖：获取并校验请求头Token
    对应SpringBoot：
    1. @RequestHeader("Authorization") String token（单个接口获取头信息）
    2. HandlerInterceptor（全局Token拦截校验）
    3. 自定义参数解析器（抽取公共逻辑）
    """
    if not token:
        raise HTTPException(status_code=401, detail="未携带Authorization Token，无权访问")
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token格式错误，正确格式：Bearer {token}")
    # 返回处理后的Token（去掉Bearer 前缀）
    return token.replace("Bearer ", "")

def get_pagination_params(
    page: int = Query(1, ge=1, description="页码，默认1，最小1"),
    size: int = Query(10, ge=1, le=100, description="每页条数，默认10，最大100")
):
    """
    公共分页依赖：抽取并校验分页参数
    对应SpringBoot：
    1. 分页DTO（如 PageRequest）
    2. MyBatis-Plus 分页插件
    3. 自定义分页参数解析器
    """
    skip = (page - 1) * size  # 计算偏移量（对应SQL的LIMIT offset, size）
    return {
        "page": page,
        "size": size,
        "skip": skip
    }

# ======================================
# 5. 路由接口（对应 SpringBoot @RestController + 请求映射注解）
# ======================================

# 场景1：基础GET请求（无参数）
# 对应 SpringBoot：@GetMapping("/")
@app.get("/", response_class=JSONResponse, summary="根路径测试接口", tags=["基础测试"])
def read_root():
    """
    根路径测试
    对应SpringBoot完整代码：
    @RestController
    public class IndexController {
        @GetMapping("/")
        public Map<String, String> readRoot() {
            Map<String, String> result = new HashMap<>();
            result.put("Hello", "World");
            return result;
        }
    }
    """
    return {"Hello": "World"}

# 场景2：GET请求 + 路径参数 + 查询参数
# 对应 SpringBoot：@GetMapping("/items/{item_id}") + @PathVariable + @RequestParam
@app.get("/items/{item_id}", summary="商品查询接口", tags=["商品管理"])
def read_item(
    # 路径参数：对应 SpringBoot @PathVariable("item_id") int itemId
    item_id: int = Path(..., ge=1, le=1000, description="商品ID，取值范围1-1000"),
    # 查询参数：对应 SpringBoot @RequestParam(required = false) String q
    q: Union[str, None] = Query(None, min_length=1, max_length=50, description="查询关键字（可选）"),
    # 查询参数：带默认值，对应 SpringBoot @RequestParam(defaultValue = "true") boolean status
    status: Optional[bool] = Query(True, description="商品状态，默认启用")
):
    """
    商品查询接口
    - item_id：路径参数（必传，整数类型校验）
    - q：查询参数（可选，字符串长度校验）
    - status：查询参数（可选，布尔类型，默认值True）
    """
    return {"item_id": item_id, "q": q, "status": status}

# 场景3：POST请求 + 请求体
# 对应 SpringBoot：@PostMapping + @RequestBody + @Valid
@app.post("/users", summary="创建用户接口", tags=["用户管理"], response_model=User, status_code=201)
def create_user(
    # 请求体参数：对应 SpringBoot @RequestBody @Valid UserDTO user
    user: User = Body(..., description="用户信息JSON请求体")
):
    """
    创建用户
    - 接收User类型JSON请求体（自动校验字段规则）
    - response_model指定返回模型（自动过滤无关字段）
    - status_code=201 对应 SpringBoot @ResponseStatus(HttpStatus.CREATED)
    """
    # 模拟业务逻辑：给用户分配ID
    user.id = 1001  # 实际项目中从数据库获取自增ID
    return user

# 场景4：PUT请求 + 路径参数 + 请求体
# 对应 SpringBoot：@PutMapping("/users/{user_id}") + @PathVariable + @RequestBody
@app.put("/users/{user_id}", summary="更新用户接口", tags=["用户管理"], response_model=User)
def update_user(
    user_id: int = Path(..., ge=1, description="用户ID"),  # 路径参数
    user: User = Body(..., description="更新后的用户信息")   # 请求体参数
):
    """
    更新用户信息
    对应SpringBoot：
    @PutMapping("/users/{user_id}")
    public UserDTO updateUser(@PathVariable int user_id, @RequestBody @Valid UserDTO user) {
        // 业务逻辑：根据user_id更新用户信息
        return user;
    }
    """
    # 模拟业务逻辑：绑定用户ID
    user.id = user_id
    return user

# 场景5：DELETE请求 + 路径参数
# 对应 SpringBoot：@DeleteMapping("/users/{user_id}") + @PathVariable
@app.delete("/users/{user_id}", summary="删除用户接口", tags=["用户管理"], status_code=204)
def delete_user(
    user_id: int = Path(..., ge=1, description="要删除的用户ID")
):
    """
    删除用户
    - status_code=204：无返回内容（对应HTTP 204 No Content）
    对应SpringBoot：
    @DeleteMapping("/users/{user_id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteUser(@PathVariable int user_id) {
        // 业务逻辑：删除用户
    }
    """
    # 模拟删除逻辑
    return None

# 场景6：嵌套模型 + POST请求
# 对应 SpringBoot：嵌套DTO接收请求体
@app.post("/orders", summary="创建订单接口", tags=["订单管理"], response_model=Order, status_code=201)
def create_order(
    order: Order = Body(..., description="订单信息（包含订单子项列表）")
):
    """
    创建订单（嵌套数据模型示例）
    """
    # 模拟业务逻辑：生成订单ID + 计算总金额
    order.order_id = f"ORD{order.user_id}{System.currentTimeMillis()}"
    order.total_amount = sum(item.price * item.quantity for item in order.items)
    return order

# 场景7：使用依赖注入（Token校验 + 分页参数）
# 对应 SpringBoot：@Autowired + @RequestParam 分页参数 + Token拦截
@app.get("/users/list", summary="用户列表分页查询", tags=["用户管理"], dependencies=[Depends(get_token_header)])
def get_user_list(
    # 注入分页依赖
    pagination: dict = Depends(get_pagination_params),
    # 额外查询参数
    keyword: Optional[str] = Query(None, description="用户名关键字查询（可选）")
):
    """
    用户列表分页查询
    - 依赖1：get_token_header（Token校验，全局接口级依赖）
    - 依赖2：get_pagination_params（分页参数预处理）
    对应SpringBoot：
    @GetMapping("/users/list")
    public PageInfo<UserDTO> getUserList(
        @RequestParam(required = false) String keyword,
        @RequestParam(defaultValue = "1") int page,
        @RequestParam(defaultValue = "10") int size,
        @RequestHeader("Authorization") String token
    ) {
        // Token校验逻辑
        // 分页查询逻辑
        return new PageInfo<>();
    }
    """
    # 模拟分页查询结果
    return {
        "page": pagination["page"],
        "size": pagination["size"],
        "total": 100,
        "total_pages": 10,
        "keyword": keyword,
        "data": [
            {"id": 1, "username": "test1", "age": 20, "email": "test1@xxx.com", "tags": ["vip"]},
            {"id": 2, "username": "test2", "age": 25, "email": "test2@xxx.com", "tags": []}
        ]
    }

# 场景8：异常处理
# 对应 SpringBoot：@ExceptionHandler + @ControllerAdvice（全局异常处理）/ 手动抛出异常
@app.get("/exception/test", summary="异常抛出测试接口", tags=["基础测试"])
def exception_test(
    flag: bool = Query(True, description="是否抛出异常")
):
    """
    异常处理示例
    对应SpringBoot：
    throw new HTTPException(HttpStatus.BAD_REQUEST, "自定义异常信息");
    """
    if flag:
        # 手动抛出异常（对应SpringBoot的RuntimeException/自定义业务异常）
        raise HTTPException(status_code=400, detail="手动触发的业务异常")
    return {"message": "正常返回"}

# ======================================
# 6. 运行入口（对应SpringBoot的main方法）
# ======================================
if __name__ == "__main__":
    import uvicorn  # FastAPI的运行服务器（对应SpringBoot的内置Tomcat/Jetty）
    # 启动服务：对应 SpringApplication.run(Application.class, args)
    uvicorn.run(
        app="main:app",  # 本文件名称:FastAPI实例名（如果文件名为api.py，这里改为api:app）
        host="0.0.0.0",  # 监听所有网卡（本地访问：127.0.0.1，局域网可通过IP访问）
        port=8000,       # 端口号（对应SpringBoot的server.port=8000）
        reload=True      # 热重载（开发环境使用，生产环境关闭）
    )