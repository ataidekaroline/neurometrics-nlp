import spacy

class NeuroMetricsEngine:
    def __init__(self):
        # Load the optimized English model from spaCy
        self.nlp = spacy.load("en_core_web_sm")
        
        # Define common English filler words indicating hesitation
        self.filler_words = {"uh", "um", "er", "ah", "hm", "hmm", "well", "like", "basically"}
        
    def analyze_transcription(self, text: str) -> dict:
        """
        Processes the patient's transcription and extracts linguistic biomarkers,
        including hesitation markers (filler words).
        """
        doc = self.nlp(text)
        
        # Filter out punctuation and spaces
        valid_tokens = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
        
        total_words = len(valid_tokens)
        unique_words = len(set(valid_tokens))
        
        # Type-Token Ratio (Lexical Density)
        ttr = unique_words / total_words if total_words > 0 else 0
        
        # Syntactic Complexity (Words per sentence)
        sentences = list(doc.sents)
        avg_sentence_length = total_words / len(sentences) if len(sentences) > 0 else 0
        
        # Filler word extraction (Hesitation biomarker)
        filler_count = sum(1 for word in valid_tokens if word in self.filler_words)
        
        return {
            "total_words": total_words,
            "unique_words": unique_words,
            "lexical_density_ttr": round(ttr, 3),
            "avg_sentence_length": round(avg_sentence_length, 2),
            "filler_word_count": filler_count
        }