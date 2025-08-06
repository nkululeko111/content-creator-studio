from transformers import pipeline

def generate_script(topic):
    """Generate a video script using AI."""
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Write a 300-word YouTube script about '{topic}'. Keep it engaging and dramatic."
    script = generator(prompt, max_length=400, do_sample=True)[0]["generated_text"]
    return script

if __name__ == "__main__":
    topic = "Kenny Kunene's secret business deals"
    script = generate_script(topic)
    print(script)


#     import openai
# import os

# # Set your DeepAI API key here
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_script(topic, category):
#     prompt = (
#         f"Create a concise, engaging, and informative script for a YouTube video about '{topic}'. "
#         f"The style should be suitable for {category} content. Keep it under 150 words."
#     )
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or "gpt-4" if available
#         messages=[
#             {"role": "system", "content": "You are a creative scriptwriter."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=300,
#     )
#     script = response.choices[0].message['content'].strip()
#     return script

# if __name__ == "__main__":
#     topic = "Kenny Kunene politician controversy"
#     category = "News & Gossip"
#     script = generate_script(topic, category)
#     print("Generated Script:\n", script)