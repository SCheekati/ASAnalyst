import data_retrieval
import data_processing
import llm_analysis
from config import API_KEYS

if __name__ == "__main__":
    # Fetch ASN data
    asn = input("Enter the ASN to analyze: ")
    data = data_retrieval.fetch_as_data(asn)

    structured_data = data_processing.process_as_data(data)
    insights = llm_analysis.analyze_as_data(structured_data)

    print("\n--- Analysis Results ---\n")
    print(insights)