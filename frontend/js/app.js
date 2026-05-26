/**
 * Interacts with the NeuroMetrics FastAPI backend.
 */

document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const transcript = document.getElementById('transcriptInput').value;
    const btn = document.getElementById('analyzeBtn');

    if (!transcript.trim()) {
        alert("Please enter a clinical transcript to analyze.");
        return;
    }

    // UI loading state
    btn.textContent = "Analyzing Pipeline...";
    btn.disabled = true;

    try {
        // Send POST request to our local FastAPI server
        const response = await fetch('http://127.0.0.1:8000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: transcript })
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }

        const data = await response.json();

        // Update the UI Dashboard with the calculated biomarkers
        document.getElementById('ttrResult').textContent = data.lexical_density_ttr;
        document.getElementById('syntaxResult').textContent = data.avg_sentence_length;
        document.getElementById('totalWordsResult').textContent = data.total_words;
        document.getElementById('uniqueWordsResult').textContent = data.unique_words;

    } catch (error) {
        console.error("Failed to extract metrics:", error);
        alert("Error connecting to the NLP Engine. Ensure the FastAPI server is running.");
    } finally {
        // Restore UI state
        btn.textContent = "Analyze Speech";
        btn.disabled = false;
    }
});