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


## RAG Concepts ##
There are several variants of RAG improvements that have been proposed, each with its own strengths and weaknesses. Some of the most popular variants include:
- Query transformation, Examples: [Trafo #1](src/rag_01.ipynb), [Trafo #2](src/rag_02.ipynb) 
  - Multi-Query: Rephrase input query into multiple variants.
  - Document fusion: Reorder multiple documents based on their retrieval rank (reciprocal rank).
  - Decomposition: Decompose query in sub-steps similar to Chain-of-Thought (CoT) and query after each answer with new information.
  - Query abstraction (Step back): Generate higher-level LLM prompt with the input question.
  - HyDE (Hypothethical document embeddings): Generate hypothetical documents based on the input question in our vector store.

- Routing [Routing examples](src/rag_02.ipynb)
  - Structured output (e.g. JSON, Pydantic) for routing types
  - Semantic routing: Use semantic similarity to route the query to the correct model/with correct prompt template.
  
- Query construction [Query construction examples](src/rag_03.ipynb):
  - Meta data: Use meta data in queries to improve retrieval.
  - Make structured LLM outputs with Pydantic to constrict filters for documents/vector DBs.

- Indexing:
  - Use of multi-embeddings indexing for retreval (e.g. summarie + documents).
  - Multi-modal Rag:
    - Use Image+Text embeddings like CLIP and similarity search.
    - VLMs to generate image summaries. Embed those summaries with text and pass to LLM. No images in store.
    - VLMs to generate image summaries. Embed summaries. Pass raw image + summaries to VLM.
  - RAPTOR - Build a document tree:
    - Embed documents -> Cluster documents -> Summarize clusters contents -> Redo until converge to a root.
    - Index the clusters and perform retrieval on both all documents + clusters.
    - Helps to retrieve hierarchical information (sub-topics etc.)
  - ColBERT: Use of BERT for efficient retrieval by creating query token <-> document token relations.

- Retrieval:
  - Re-rank of documents importances using services like Cohere
  - Self-improving RAG:
    - Corrective RAG (CRAG): Reasoning over results and iterative improvement. LangGraph.
    - Self-RAG: Reiterate over the same question with new information.




