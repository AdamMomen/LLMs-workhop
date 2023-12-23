from llama_hub.whatsapp import WhatsappChatLoader
from llama_index import VectorStoreIndex, get_response_synthesizer
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.postprocessor import SimilarityPostprocessor


loader = WhatsappChatLoader("./data/BALI_NOMAD_CODERS_CHAT.txt")
docs = loader.load_data()

index = VectorStoreIndex(docs)

retriever = VectorIndexRetriever(index=index, similarity_top_k=10)

response_synth = get_response_synthesizer()

query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synth,
    node_postprocessors=[SimilarityPostprocessor(simlarity_cutoff=0.7)]
)

response = query_engine.query("What does Adam usually talk about?")
print(response)
