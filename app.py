from Query import retriver
from metrices.factual_similarity import FactualSimilarity
from metrices.readability import Readibility
import pandas as pd

def main():
    questions = [
        "what is Theory of Mind?",
        "What is self awareness?",
    ]

    ground_truth = [
        "These are types of machines, which are expected to understand the psychological and emotional aspects of human mind and work accordingly. So far such machines are a dream but scientists are working to develop such machines in near future.",
        "These machines belong to a hypothetical concept that will be considered as super-intelligent machines, which can think, act, and will be self-aware asthey will have consciousness and sentiments like humans. Research is carried out to develop such machines and considered as future AI."
    ]

    answers = []
    contexts = []
    similarity_scores = []

    # Calculate readability scores
    readability_scores = []

    # Inference
    for query, truth in zip(questions, ground_truth):
        context, answer = retriver.reply(query)
        answers.append(answer)
        contexts.append(context)
        
        # Calculate similarity score
        similarity_score = FactualSimilarity.score(answer, truth)
        similarity_scores.append(similarity_score)
    
        readability_score = Readibility._flesch_kincaid_eval_fn(answer)
        readability_scores.append(readability_score['mean'])  # Using mean score for simplicity

    # Create a DataFrame to store results
    results_df = pd.DataFrame({
        'Question': questions,
        'Ground Truth': ground_truth,
        'Generated Answer': answers,
        'Similarity Score': similarity_scores
    })


    # for answer in answers:


    # Add readability scores to the DataFrame
    results_df['Readability Score'] = readability_scores

    # Print or save the results
    print(results_df)
    results_df.to_csv('results.csv', index=False)

if __name__ == "__main__":
    main()


