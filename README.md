# AI-Powered Question Answering System with Evaluation Metrics

This project implements an AI-powered question answering system using Google's Generative AI and LangChain. It processes PDF documents, creates embeddings, and uses a retrieval-based approach to answer questions based on the document content. Additionally, it includes evaluation metrics to assess the quality and readability of the generated answers.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ai-question-answering.git
   cd ai-question-answering
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Google API key:
   - Create a `.env` file in the project root directory
   - Add your Google API key to the file:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

5. Prepare your data:
   - Place your PDF document in the `data` folder (e.g., `data/AI.pdf`)

6. Run the indexing script to process the PDF and create embeddings:
   ```
   python store_index.py
   ```

## Usage

To run the question answering system with evaluation metrics:

1. Execute the main script:
   ```
   python app.py
   ```

2. The script will process a set of predefined questions and generate answers.

3. The results, including the questions, ground truth, generated answers, and evaluation metrics, will be displayed in the console and saved to a CSV file named `results.csv`.

## Evaluation Metrics

This project incorporates two main evaluation metrics to assess the quality of the generated answers:

1. **Factual Similarity Score**: 
   - Implemented in `metrices/factual_similarity.py`
   - Measures how similar the generated answer is to the ground truth
   - Uses cosine similarity between embeddings of the generated answer and the ground truth
   - Scores range from 0 to 1, with higher scores indicating greater similarity

2. **Readability Score**:
   - Implemented in `metrices/readability.py`
   - Uses the Flesch-Kincaid Grade Level to assess the readability of the generated answers
   - Lower scores indicate easier readability, while higher scores suggest more complex text
   - The mean score is reported for each answer

These metrics provide insights into both the accuracy and the comprehensibility of the AI-generated responses.

## Project Structure

- `app.py`: Main script for running the question answering system and evaluation
- `store_index.py`: Script for processing the PDF and creating embeddings
- `metrices/`: Directory containing the evaluation metric implementations
  - `factual_similarity.py`: Implements the factual similarity scoring
  - `readability.py`: Implements the readability scoring
- `data/`: Directory for storing input PDF documents
- `db/`: Directory where the processed embeddings are stored

## Output

The script generates a CSV file (`results.csv`) with the following columns:
- Question
- Ground Truth
- Generated Answer
- Similarity Score
- Readability Score

This allows for easy analysis and comparison of the AI's performance across different questions.

