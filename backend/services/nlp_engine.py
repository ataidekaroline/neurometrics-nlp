import spacy

class NeuroMetricsEngine:
    def __init__(self):
        # Load the optimized English model from spaCy
        self.nlp = spacy.load("en_core_web_sm")
        
    def analyze_transcription(self, text: str) -> dict:
        """
        Processes the patient's transcription and extracts linguistic biomarkers.
        """
        doc = self.nlp(text)
        
        # Filter out punctuation and spaces to focus only on actual words
        valid_tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
        
        total_words = len(valid_tokens)
        unique_words = len(set(valid_tokens))
        
        # Type-Token Ratio (Lexical Density) calculation
        ttr = unique_words / total_words if total_words > 0 else 0
        
        # Basic Syntactic Complexity calculation (words per sentence)
        sentences = list(doc.sents)
        avg_sentence_length = total_words / len(sentences) if len(sentences) > 0 else 0
        
        return {
            "total_words": total_words,
            "unique_words": unique_words,
            "lexical_density_ttr": round(ttr, 3),
            "avg_sentence_length": round(avg_sentence_length, 2)
        }