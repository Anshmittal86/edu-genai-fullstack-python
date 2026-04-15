# Terminologies

<details>
  <summary><b>1. Token</b></summary>
  
  A Token is a small piece of text, like a word, sub-word, or character.

**Example:**  
 `I love coding` -> `['I', 'Love', 'coding']`

</details>

<details>
  <summary><b>2. TokenID</b></summary>
  
  A TokenID is a number that represent a token.

**Example:**  
 `['I', 'Love', 'coding']` -> `[10, 23, 45]`

</details>

<details>
  <summary><b>3. Tokenization</b></summary>
  
  The process of breaking text into tokens.

**Example:** `I love coding` -> `['I', 'Love', 'coding']`

</details>

<details>
  <summary><b>4. Encoding</b></summary>
  
  The process of converting tokens into TokenIDs or Vectors
</details>

<details>
  <summary><b>5. Decoding</b></summary>
  
  The process of converting TokenIDs or vectors into readable text.
</details>

<details>
  <summary><b>6. Vector</b></summary>
  
  Mathematical representation of text capturing its meaning. Similar meanings have closer vectors.
</details>

<details>
  <summary><b>7. Transformer</b></summary>
  
  Transformer is a smart system or Architecture in AI that understands sequential data like text or audio and predict the next element by finding relationship between inputs using self attention mechanism. This processes all tokens at once instead one by one. Transformer Architecture introduced by the Google in 2017 in his research paper of "Attention all you need".
</details>

<details>
  <summary><b>8. Encoder</b></summary>
  
  Part of AI Model that reads and understand input context.
</details>

<details>
  <summary><b>9. Decoder</b></summary>
  
  Part of AI Model that generates output step by step. Used in ChatGPT
</details>

<details>
  <summary><b>10. Attention</b></summary>
  
  Mechanism that helps model focus on important words in a sentence. Not all words matter equally, attention decides importance.
</details>

<details>
  <summary><b>11. TopK</b></summary>
  
  TopK is technique where the model select only the top K most probable word and ignores all others before choosing the next word.
</details>

<details>
  <summary><b>12. TopP</b></summary>
  
  TopP (nucleus sampling) is a technique where the model keeps selecting the most probable words until their combined probability reaches a threshold P.
</details>

<details>
  <summary><b>13. Temperature</b></summary>
  
  Controls randomness of output.  
  **Low** = predictable, **High** = Creative
</details>

<details>
  <summary><b>14. Training Data</b></summary>
  
  Data used to teach the model patterns and knowledge.  
  **Quality Data** = better model performance.
</details>

<details>
  <summary><b>15. Machine Learning</b></summary>
  
  Technique where systems learn patterns from data without explicit programming. Model improves as it sees more data.
</details>

<details>
  <summary><b>16. Deep Learning</b></summary>
  
  Subset of Machine learning using neural networks with many layers. Good at complex tasks like vision and language.
</details>

<details>
  <summary><b>17. SuperVised Learning</b></summary>
  
  Model learn from Labeled data (input + correct output)  
  **Example:** Spam detection with labeled emails.
</details>

<details>
  <summary><b>18. Unsupervised learning</b></summary>
  
  Model finds patterns in unlabeled data.  
  **Example:** Customer segmentation.
</details>

<details>
  <summary><b>19. Reinforcement Learning</b></summary>
  
  Model learns by trial and error using reward and penalties.
</details>

<details>
  <summary><b>20. NLP</b></summary>
  
  Natural Language Processing, field focused on understanding human language.  
  Used in chatbots, translation, sentiment analysis.
</details>

<details>
  <summary><b>21. CNN</b></summary>
  
  Convolutional Neural Network used mainly for image processing. Detects patterns like edges, shapes, object.
</details>

<details>
  <summary><b>22. GAN</b></summary>
  
  Generative Adversarial Network with two models competing.
</details>

<details>
  <summary><b>23. Computer Vision</b></summary>
  
  Field where machines understand and interpret images and audio.  
  Used in face recognition, object detection
</details>

<details>
  <summary><b>24. BIAS in AI</b></summary>
  
  Where model shows unfair preference due to biased training data.  
  Leads to incorrect or unfair results.
</details>

<details>
  <summary><b>25. Hallucination</b></summary>
  
  When AI generates incorrect or made-up information confidently. Looks real, but actually false.
</details>

<details>
  <summary><b>26. Fine Tunning</b></summary>
  
  Process of training a pretrained model on specific data. Model specialized for a task.
</details>

<details>
  <summary><b>27. Vocabulary Size</b></summary>
  
  Total number of unique tokens a model can understand. Defines how many words or sub-words the model knows.
</details>

<details>
  <summary><b>28. Vector Embedding</b></summary>
  
  Vector embedding is a process where we capture the meaning and relationships between different pieces of data into meaningful numeric vectors, and we can store this data in a Vector Database
</details>
