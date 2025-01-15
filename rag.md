# RAG - Retrieval augmented generation #
This deep dive in to RAG is based on lang-chains [rag_from_scratch](https://github.com/langchain-ai/rag-from-scratch)

## What is RAG? ##
RAG is a model that combines retrieval and generation in a single model. It is based on the idea of using a retriever to retrieve relevant passages from a large corpus and then using a generator to generate the answer based on the retrieved passages. The retriever is used to narrow down the search space and provide relevant context to the generator, which can then generate more accurate and coherent answers.
A simple RAG example can be found here: [RAG](src/rag_01.ipynb) 

![RAG](/docs/rag_overview.png)


### 1. Indexing ###
The first step in using RAG is to index the corpus of documents that will be used for retrieval. This involves converting the documents into a format that can be efficiently searched and retrieved. The documents are typically indexed using a search engine like Elasticsearch, which allows for fast and efficient retrieval of relevant passages.

- Numerical representation of the text:
  - **Splitting**: The documents is split into smaller units to satisfy context windows.
  - 

### 2. Retrieval ###
Retrieval is the process to find the most relevant passages from the indexed corpus based on the input query. The retriever uses a search engine to search the indexed corpus and retrieve the most relevant passages based on the input query. This typically is using some kind of similarity search of embeddings.


### 3. Generation ###
Finally the generation step takes retrieved context data and input question. With this information it generates the answer prompting the LLM. 
