from gradio_client import Client, handle_file

def generate_podcast():
    client = Client("gabrielchua/open-notebooklm")
    
    result = client.predict(
        files=[handle_file('examples/Xai.pdf')],
        url="https://en.wikipedia.org/wiki/Hugging_Face",  # Replace with your desired URL
        question="How did Hugging Face become so successful?",  # Replace with your question
        tone="Fun",
        length="Short (1-2 min)",
        language="English",
        use_advanced_audio=False,
        api_name="/generate_podcast"
    )
    
    print("Podcast generated:")
    print(result)

if __name__ == "__main__":
    generate_podcast()
