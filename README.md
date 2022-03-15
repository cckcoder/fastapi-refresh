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