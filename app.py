from fastapi import FastAPI

app = FastAPI()

#Root route
@app.get("/")
def root():
   return {"mensaje para mi polletin"}

# Route to display info for ítems
@app.get("/items/")
def items():
   return {"mensaje para mi polletaso"}

# Route to display info fot updating items
@app.get("/items/update/")
def update_items():

   return {"mensaje para mi polletón"}

