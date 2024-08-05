<!-- # Document-based-Question-Answering-System
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

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/pratheeshkumar99/Document-based-Question-Answering-System.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd Document-based-Question-Answering-System
    ```

3. **Set up the Conda Environment**:
    
    ```bash
    conda create --name your_env_name python=3.9
    conda activate your_env_name
    ```

4. **Install the Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the Environment Variables**:
    - The `.env` file is already included in the project. Edit this file to add your own API keys:
        ```env
        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_API_KEY=your-langchain-api-key
        OPENAI_API_KEY=your-openai-api-key
        LANGCHAIN_PROJECT=QA_project
        ```
    - Replace `your-langchain-api-key` and `your-openai-api-key` with your actual API keys.

### Usage

1. **Run the Streamlit application**:
    - Ensure you have activated your conda environment:
        ```bash
        conda activate your_env_name
        ```
    - Start the Streamlit app:
        ```bash
        streamlit run document_query_app.py
        ```

2. **Interact with the application**:
    - Upload a text document using the file uploader.
    - Enter your query in the provided input box.
    - Click on the "Get Answer" button to retrieve the answer based on the context of the uploaded document.

### Example Questions

Here are some example questions you can ask based on the sample documents provided:

#### For `cvd.txt`:

1. **What are the primary risk factors for cardiovascular disease?**
    - Answer: The primary risk factors for cardiovascular disease (CVD) include smoking, high blood pressure, high cholesterol, diabetes, inactivity, being overweight or obese, poor diet, and family history of heart disease.

2. **Can you list the common symptoms of cardiovascular diseases?**
    - Answer: Common symptoms of cardiovascular disease include chest pain or discomfort, shortness of breath, pain, numbness, weakness, or coldness in your legs or arms, and pain in the neck, jaw, throat, upper abdomen, or back.

3. **What are some preventive measures to reduce the risk of cardiovascular disease?**
    - Answer: Preventive measures to reduce the risk of cardiovascular disease include quitting smoking, eating a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins, exercising regularly, maintaining a healthy weight, managing stress, and controlling conditions like hypertension, high cholesterol, and diabetes.

4. **Why is early detection of cardiovascular disease important?**
    - Answer: Early detection of cardiovascular disease can be life-saving. Regular check-ups are recommended, particularly for individuals with risk factors. Monitoring and managing blood pressure, cholesterol levels, and other markers of cardiovascular health can prevent or delay the onset of CVD.

#### For `climate.txt`:

1. **What are some of the impacts of climate change as described in the document?**
    - Answer: Climate change refers to considerable alterations in global temperatures and weather patterns over time. Scientists believe that human activities, particularly since the Industrial Revolution, are the main cause of recent climate changes, due to the increased emission of greenhouse gases. These changes can result in effects like rising average temperatures, altered weather patterns, extreme weather events, and rising sea levels. These impacts can harm ecosystems, water resources, agricultural productivity, food security, and coastal communities.

2. **How can communities adapt to the effects of climate change according to the document?**
    - Answer: The text suggests that both mitigation and adaptation are vital strategies to combat the effects of climate change. Mitigation refers to efforts like reducing greenhouse gas emissions, using renewable energy, and enhancing the natural carbon sink capacity of forests. Adaptation measures involve building flood defenses, creating drought-resistant crops, and developing climate-resilient infrastructure. The impacts of climate change, such as altered weather patterns, extreme weather events, and rising sea levels, can have severe consequences on ecosystems, water resources, agricultural productivity, and food security.

### Project Structure

- **document_query_app.py**: The main script to run the Streamlit app.
- **requirements.txt**: A list of all the dependencies required for the project.
- **.env**: Environment variables for API keys and configuration.
- **data**: Directory containing sample documents for testing (`cvd.txt` and `climate.txt`).

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

### License

This project is licensed under the MIT License. -->


# Document-based Question Answering System

This project demonstrates a Retrieval-Augmented Generation (RAG) system for question answering. It integrates OpenAI’s GPT-4 model with FAISS for vector similarity search, enabling the system to provide accurate and contextually relevant answers based on a given document or dataset.

## Key Components

1. **Data Ingestion**: The system starts by loading and preprocessing text documents, converting them into a format suitable for further analysis.
2. **Text Splitting**: Documents are split into smaller, manageable chunks using the Recursive Character Text Splitter. This step ensures that each chunk is of an optimal size for processing and embedding.
3. **Embedding Generation**: Each document chunk is transformed into a high-dimensional vector representation using OpenAI’s embedding model. These embeddings capture the semantic meaning of the text, enabling efficient similarity search.
4. **Vector Store**: The embeddings are stored in FAISS (Facebook AI Similarity Search), a library that allows for fast and efficient similarity searches.
5. **Question Answering**: When a query is received, the system retrieves the most relevant document chunks from the vector store based on their similarity to the query. These chunks are then combined with the query and passed to GPT-4, which generates a contextually accurate answer.

## Features

- **Efficient Document Processing**: Handles large documents by splitting them into smaller chunks, ensuring efficient processing and retrieval.
- **Advanced Embeddings**: Utilizes state-of-the-art embeddings to capture the semantic meaning of the text.
- **Accurate Retrieval**: Employs FAISS for fast and accurate retrieval of relevant document chunks.
- **Contextual Question Answering**: Uses GPT-4 to generate answers based on the retrieved context, ensuring relevance and accuracy.

## Prerequisites

- Python 3.9
- Conda (for managing environments)

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/pratheeshkumar99/Document-based-Question-Answering-System.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd Document-based-Question-Answering-System
    ```

3. **Set up the Conda Environment**:
    
    ```bash
    conda create --name your_env_name python=3.9
    conda activate your_env_name
    ```

4. **Install the Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the Environment Variables**:
    - The `.env` file is already included in the project. Edit this file to add your own API keys:
        ```env
        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_API_KEY=your-langchain-api-key
        OPENAI_API_KEY=your-openai-api-key
        LANGCHAIN_PROJECT=QA_project
        ```
    - Replace `your-langchain-api-key` and `your-openai-api-key` with your actual API keys.

## Usage

1. **Run the Streamlit application**:
    - Ensure you have activated your conda environment:
        ```bash
        conda activate your_env_name
        ```
    - Start the Streamlit app:
        ```bash
        streamlit run document_query_app.py
        ```

2. **Interact with the application**:
    - Upload a text document using the file uploader.
    - Enter your query in the provided input box.
    - Click on the "Get Answer" button to retrieve the answer based on the context of the uploaded document.

## Example Questions

Here are some example questions you can ask based on the sample documents provided:

#### For `cvd.txt`:

1. **What are the primary risk factors for cardiovascular disease?**
    - Answer: The primary risk factors for cardiovascular disease (CVD) include smoking, high blood pressure, high cholesterol, diabetes, inactivity, being overweight or obese, poor diet, and family history of heart disease.

2. **Can you list the common symptoms of cardiovascular diseases?**
    - Answer: Common symptoms of cardiovascular disease include chest pain or discomfort, shortness of breath, pain, numbness, weakness, or coldness in your legs or arms, and pain in the neck, jaw, throat, upper abdomen, or back.

3. **What are some preventive measures to reduce the risk of cardiovascular disease?**
    - Answer: Preventive measures to reduce the risk of cardiovascular disease include quitting smoking, eating a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins, exercising regularly, maintaining a healthy weight, managing stress, and controlling conditions like hypertension, high cholesterol, and diabetes.

4. **Why is early detection of cardiovascular disease important?**
    - Answer: Early detection of cardiovascular disease can be life-saving. Regular check-ups are recommended, particularly for individuals with risk factors. Monitoring and managing blood pressure, cholesterol levels, and other markers of cardiovascular health can prevent or delay the onset of CVD.

#### For `climate.txt`:

1. **What are some of the impacts of climate change as described in the document?**
    - Answer: Climate change refers to considerable alterations in global temperatures and weather patterns over time. Scientists believe that human activities, particularly since the Industrial Revolution, are the main cause of recent climate changes, due to the increased emission of greenhouse gases. These changes can result in effects like rising average temperatures, altered weather patterns, extreme weather events, and rising sea levels. These impacts can harm ecosystems, water resources, agricultural productivity, food security, and coastal communities.

2. **How can communities adapt to the effects of climate change according to the document?**
    - Answer: The text suggests that both mitigation and adaptation are vital strategies to combat the effects of climate change. Mitigation refers to efforts like reducing greenhouse gas emissions, using renewable energy, and enhancing the natural carbon sink capacity of forests. Adaptation measures involve building flood defenses, creating drought-resistant crops, and developing climate-resilient infrastructure. The impacts of climate change, such as altered weather patterns, extreme weather events, and rising sea levels, can have severe consequences on ecosystems, water resources, agricultural productivity, and food security.

## Project Structure

- **document_query_app.py**: The main script to run the Streamlit app.
- **requirements.txt**: A list of all the dependencies required for the project.
- **.env**: Environment variables for API keys and configuration.
- **data**: Directory containing sample documents for testing (`cvd.txt` and `climate.txt`).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License.