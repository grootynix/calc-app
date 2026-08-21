from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.calculator import calculate

app = FastAPI(title="Calculator API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float
    expression: str

@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}

@app.post("/calculate", response_model=CalculationResponse)
def calculate_endpoint(request: CalculationRequest):
    try:
        result = calculate(request.expression)
        return CalculationResponse(
            result=result,
            expression=request.expression
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))