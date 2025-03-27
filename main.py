from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        "name": "milk",
        "price": "$3.99",
        "size": "gallon",
        "quantity": 5
    }
}

@app.get("/")
def home():
    return {
        "Message": "Welcome to fast API"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0"
    }

@app.get("/about")
def about():
    return {
        "version": "v1.0",
        "OS": "Mac",
        "IDE": "VSCode",
        "framework": "fast API",
        "language": "python"
    }
    
@app.get("/item/{itemID}")
def getItem(itemID: int = Path(description = "The integer ID of the item of which to return inventory data.")):
    if (itemID in inventory):
        return inventory[itemID]
    return "Item with ID " + itemID + " not found."