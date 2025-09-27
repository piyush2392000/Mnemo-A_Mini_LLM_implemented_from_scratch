import torch
from llm import GPTModel, GPT_CONFIG_124M, generate_text_simple, text_to_token_ids, token_ids_to_text, generate_text
import tiktoken

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# create model instance here
model = GPTModel(GPT_CONFIG_124M)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.to(device)
# print(model.eval())

print("Model loaded and ready!")
tokenizer = tiktoken.get_encoding("gpt2")
token_ids = generate_text_simple(
    model=model,
    idx=text_to_token_ids("every efforts moves you", tokenizer).to(device),
    max_new_tokens=30,
    context_size=GPT_CONFIG_124M["context_length"],
)

token_ids1= generate_text(
    model=model,
    idx=text_to_token_ids("every efforts moves you", tokenizer).to(device),
    max_new_tokens=30,
    context_size=GPT_CONFIG_124M["context_length"],
    temperature=0.9,
    top_k=50,
)
print("Output text:\n", token_ids_to_text(token_ids, tokenizer))
print("Output text:\n", token_ids_to_text(token_ids1, tokenizer))

