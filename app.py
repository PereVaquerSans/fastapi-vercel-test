from fastapi import FastAPI

app = fastAPI()

#Root route
@app.get("/")
def root():
   return {"message: Welcome to the main route"}

# Route to display info for ítems
@app.get("/items/")
def items():
   return {"message: Welcome to the items route"}

# Route to display info fot updating items
@app.get("/items/update/")
def update_items():
   return {"message: Welcome to the update item route"}