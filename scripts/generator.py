from transformers import pipeline

def generate_script(topic, tone="dramatic"):
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Write a 200-word YouTube script about '{topic}'. Make it {tone}."
    return generator(prompt, max_length=300)[0]["generated_text"]

if __name__ == "__main__":
    trends = fetch_trends()  # From Phase 1
    for playlist, topic in trends.items():
        tone = "educational" if playlist == "Kids Education" else "dramatic"
        script = generate_script(topic, tone)
        print(f"📝 {playlist} Script:\n{script}\n")