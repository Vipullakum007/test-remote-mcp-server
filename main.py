from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator Server")

# tool : add 2 numbers
@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# Tool : Generate a random number between a given range
@mcp.tool
def random_number(min: int=1 , max: int= 100) -> int:
    """
    Generate a random number between a given range.
    
    Args:
        min (int): The minimum value of the range.
        max (int): The maximum value of the range.
        
    Returns:
        int: A random number between min and max.
    """
    return random.randint(min, max)
    
# Resource : Server Information
@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple server that provides basic calculator functions and random number generation.",
        "tools": ["add", "random_number"],
        "authors": ["Your Name"]
    }
    return json.dumps(info, indent=4)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)