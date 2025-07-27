import gradio as gr

def launch_interface(qa_chain):
    def ask(question):
        return qa_chain.run(question)

    interface = gr.Interface(fn=ask, inputs="text", outputs="text", title="Cyprus Legal RAG Assistant")
    interface.launch()
