from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def get_answer(question, vectorstore=None):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # If vectorstore exists, use RAG
    if vectorstore is not None:
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        return qa_chain.invoke(question)

    # Else: Fallback to direct LLM response
    response = llm.invoke(question)
    return response.content  # or just str(response)
