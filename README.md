# GET method overview
* Path parameters
* Predefined values
* Query parameters

## Path parameters
```python
@app.get("/blog/{id}")
def index(id):
    return { "message": f"Blog with id {id}"}
```

# Request
* automatic JSON parse

## Parameter metadata
* Information displayed in docs
* Using the Query, Path and Body imports
* set default value
    * `comment_id: int = Query(None)`

# Database

## Dependencies quick intro
* Allow a function to depend on another function
* Import functionality seamlessly
    `req_param: dict = Depends(required_functionality`

## Databases
* Any relational database
* ORM library
* SQLAlchemy

## Lib
* SqlAlchemy
    `pip install sqlalchemy`
* passlib
    `pip install passlib`
* bcrypt
    `pip install bcrypt`

## Process
* Import required libraries: sqlalchemy, passlib, bycrypt
* Create databased definition and run it in main.py
* Create database models (taables)
* Create functionality to write to database
* Create schemas
    * Data from user: UserBase
    * Response to user: UserDisplay
* Create API operation

## Other concepts overview
* Error handling
* Custom responses
* Headers
* Cookies
* Form data
* CORS

### Exceptions
#### HTTP Status Code
* 1xx informational
* 2xx success
* 3xx redirection
* 4xx client error
* 5xx server error

#### Custom exception
* Provide exception handler
```python
class StoryException(Exception):
    def __init__(self, name: str):
        self.name = name
```
#### Response
* Standard response is a model, list, database model, dict etc.
* We can customize the Response object
* No data conversion
    * `return Response(content=data, media_type"text/html")`
* Why?
    * add parameters: Headers, Cookies
    * different types of response
        * plain text
        * xml
        * html
        * files
        * streaming
    * complex decisional logic
    * better docs

#### Request Headers
* Add headers in request function definition
```python
@router.get("/")
def fun(custom_header: Optional[str] = Header(None))
    pass
```
* Automatic conversion between _ and -
* List of headers
```python
@router.get("/")
def fun(custom_header: Optional[List[str]] = Header(None))
    pass
```

#### Response Headers
```python
def fun(response: Response)
    response.headers['c-custom-header'] = 'abc'
```

#### Cookies
* Store information on the browser
* Can accept str, list, dict, model etc.

```python
response.set_cookie(key="test_cookie", value="test_cookie_value")
test_cookie: Optional[str] = Cookie(None)
```

#### Form data
* HTML form data `<form>...</form>`
* application/x-www-form-urlencoded
    `def create_product(name: str = Form(...)):`
* If you would like to use Form
    * MUST install `python-multipart` 

#### CORS
* Cross Origin Resource Sharing
    * example localhost:8008 <--> localhost:8000
    * this case CORS happend
* Need to allow CORS
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
## Authentication
* Authentication
* Secureing an endpoint
* Generating access token
* User authentication

### authentication
* Complex topic
* OAuth2 with username and password
* how to generate SECRET_KEY
    * [randomkeygen](https://randomkeygen.com/)
    * cli `openssl rand -hex 32`

#### Lib in use
* jose `pip install python-jose[cryptography]` 

#### Token
* Verify token
* Retrieve user associated with token
* Secure more endpoints          

## File section orverview
* File
* UploadFile
* Making files statically available
* Downloading file

### File
* Declared similarly to Form fields
    * `def get_file(file: bytes = File(...)):`
* Received as bytes
* Stored in memory

### UploadFile
* Provides more functionality
* Stored in memory up to a  certain size, then on disk
* Python file like object

### Make file static
* Need to install library `pip install aiofiles`
### Download file
* Provide more logic around file access
* Provide security
    ```python
        @router.get("/download/{name}", response_class=FileResponse)
        def download_file(name: str):
            ...
            return path
    ```

## Testing
* Supports maintainablility and scalability
* strive for 100% coverage
* Easy with requests and pytest libraries

### Example
```python
def test_get_all_posts():
    response = client.get("/blog/all")
    assert response.status.code == 200
```

### Library in use
* requests `pip install requests`
* pytest `pip install pytest`

## More Concepts
* Async await
* Templates
* Middleware
* Background tasks
* WebSockets

### Concurrency
* Functionality can be asynchronous
* We don't want the execution to block
* await means the process can be paused
* async defines a function with suspendable pointo

### Background tasks
* Functionality to be run after the call has been complete
* Can have access to request and response
```python
@router.get("/{id}")
def read_item(id: str, bt: BackgroundTasks):
    bt.add_task(some_functionality, params)
```
### WebSockets
* Two way communication
* Keep connection open
* Need websocket lib `pip install websockets`
# Ref
* [mysql docker-compose](https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee)