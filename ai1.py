from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")

    summary = summarizer(text, max_length = 150, min_length = 30, do_sample= False)

    return summary[0]['summary_text']

input_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.
Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper.
Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue.
"""

summary = summarize_text(input_text)

print("Original Text: ")

print(input_text)

print("\nSummary:")
print(summary)