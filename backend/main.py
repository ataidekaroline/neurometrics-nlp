from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.services.nlp_engine import NeuroMetricsEngine

# Initialize FastAPI application with metadata
app = FastAPI(
    title="NeuroMetrics API",
    description="API for extracting linguistic biomarkers to support cognitive decline research.",
    version="1.0.0"
)

# Initialize the core NLP engine instance
engine = NeuroMetricsEngine()

# Define Pydantic models for strict data validation
class AnalysisRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    total_words: int
    unique_words: int
    lexical_density_ttr: float
    avg_sentence_length: float
    filler_word_count: int

@app.get("/")
def read_root():
    """
    Health check endpoint to verify API status.
    """
    return {"status": "healthy", "project": "NeuroMetrics API"}

@app.post("/api/analyze", response_model=AnalysisResponse)
def analyze_text(request: AnalysisRequest):
    """
    Endpoint to analyze clinical transcripts and extract linguistic biomarkers.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text content cannot be empty.")
    
    try:
        metrics = engine.analyze_transcription(request.text)
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal NLP Engine error: {str(e)}")