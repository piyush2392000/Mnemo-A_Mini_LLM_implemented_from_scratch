Hi there!!!! 
In this projects i have coded a llm from the ground up in stages 
The three main stages of coding a LLM are
1) Implementing the architecture and data preprocessing (stage 1)
2) Pretraining a LLM to create a foundation model (stage 2)
3) Fine-tuning the foundation model to become a personal assistant or text classifier (stage 3).
<img width="1400" height="781" alt="image" src="https://github.com/user-attachments/assets/3dcfb35d-7bab-45fd-b5f8-f4d935259e95" />

In stage 1, we will learn about the fundamental data preprocessing steps and before coding the attention mechanism we will try to understand every component seperately such as creating tokens from sentences, creating indices from these tokens, creating vector embeddings that are not yet contextually aware, adding positional encoding into those embeddings, through various types of attention creating contextually aware embeddings, layer normalisation and finally encoders and decoders.
Next, in stage 2, we will learn how to code and pretrain a GPT-like LLM capable of generating new texts. We will also go over the fundamentals of evaluating LLMs, which is essential for developing capable NLP systems.
Pretraining an LLM from scratch is a significant endeavor, demanding thousands to millions of dollars in computing costs for GPT-like models. Therefore, the focus of stage 2 is on implementing training for educational purposes using a small dataset. In addition, we will also see code examples for loading openly available model weights.
Finally, in stage 3, we will take a pretrained LLM and fine-tune it to follow instructions such as answering queries or classifying texts the most common tasks in many real-world applications and research.

If you want a detailed explaination in a component level way, you are covered i have blogged my whole learnings on Medium.
1) https://medium.com/@piyush23242001/building-a-large-language-model-09490a8ab8a9
2) https://medium.com/@piyush23242001/data-preprocessing-4cbec80b1b32
3) https://medium.com/@piyush23242001/attention-is-all-you-need-1-db8f0fbeb7a0
4) https://medium.com/@piyush23242001/attention-is-all-you-need-2-2ea7f4472e38
5) https://medium.com/@piyush23242001/implementing-a-gpt-6d5edc9d3bc1
6) https://medium.com/@piyush23242001/pretraining-of-model-e7007da07207
7) https://medium.com/@piyush23242001/temperature-scaling-top-k-sampling-loading-model-weights-c54a86f81415
