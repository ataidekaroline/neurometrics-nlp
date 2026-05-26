# NeuroMetrics

> A full-stack NLP pipeline for extracting linguistic biomarkers from clinical transcripts. It evaluates Type-Token Ratio and syntactic complexity to support computational neuroscience research and cognitive decline detection.

## 🔬 Scientific Background
Neurodegenerative conditions, such as Alzheimer's disease, often manifest early through subtle changes in speech and language production. Before significant memory loss occurs, patients may exhibit a decline in vocabulary richness and syntactic structure. 

NeuroMetrics is an automated pipeline designed to process clinical transcripts (such as the "Cookie Theft" picture description task) and extract quantitative linguistic biomarkers. 

Currently supported metrics:
- **Lexical Density (Type-Token Ratio):** Measures vocabulary richness. Lower scores often correlate with word-finding difficulties.
- **Syntactic Complexity:** Evaluates average sentence length and structural depth.

## 🏗️ Architecture
The system is built as a decoupled Full-Stack application:
- **Backend/Engine:** Python 3.12, utilizing `spaCy` for robust Natural Language Processing.
- **API Layer:** `FastAPI` to serve the NLP engine as microservices.
- **Frontend:** HTML/JS/CSS dashboard for clinical data visualization.

## 🚀 Quickstart (Development)

1. **Clone the repository:**
```bash
git clone [https://github.com//neurometrics-nlp.git](https://github.com/ataidekaroline/neurometrics-nlp.git)
cd neurometrics-nlp