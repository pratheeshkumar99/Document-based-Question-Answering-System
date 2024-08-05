# Document-based-Question-Answering-System
This project demonstrates a Retrieval-Augmented Generation (RAG) system for question answering. It integrates OpenAI’s GPT-4 model with FAISS for vector similarity search, enabling the system to provide accurate and contextually relevant answers based on a given document or dataset.




### Key Components

	1.	Data Ingestion: The system starts by loading and preprocessing text documents, converting them into a format suitable for further analysis.
	2.	Text Splitting: Documents are split into smaller, manageable chunks using the Recursive Character Text Splitter. This step ensures that each chunk is of an optimal size for processing and embedding.
	3.	Embedding Generation: Each document chunk is transformed into a high-dimensional vector representation using OpenAI’s embedding model. These embeddings capture the semantic meaning of the text, enabling efficient similarity search.
	4.	Vector Store: The embeddings are stored in FAISS (Facebook AI Similarity Search), a library that allows for fast and efficient similarity searches.
	5.	Question Answering: When a query is received, the system retrieves the most relevant document chunks from the vector store based on their similarity to the query. These chunks are then combined with the query and passed to GPT-4, which generates a contextually accurate answer.


### Features

	•	Efficient Document Processing: Handles large documents by splitting them into smaller chunks, ensuring efficient processing and retrieval.
	•	Advanced Embeddings: Utilizes state-of-the-art embeddings to capture the semantic meaning of the text.
	•	Accurate Retrieval: Employs FAISS for fast and accurate retrieval of relevant document chunks.
	•	Contextual Question Answering: Uses GPT-4 to generate answers based on the retrieved context, ensuring relevance and accuracy.



### Installation

- 1.	Clone the Repository:

``` git clone https://github.com/pratheeshkumar99/Document-based-Question-Answering-System.git```

- 2.    Navigate to the Project Directory:
``` cd project-name```

- 3.    Install the Required Packages:
```pip install -r requirements.txt```