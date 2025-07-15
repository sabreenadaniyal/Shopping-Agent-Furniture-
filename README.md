# 🛋️ Smart Furniture Shopping Agent

An AI-powered assistant that helps you browse, explore, and receive recommendations for furniture products. The agent fetches real-time product data from a live API and uses an LLM to suggest items tailored to your preferences, such as room type, style, or color.

---

## 📌 What is the Project?

This is an interactive **shopping assistant** designed specifically for discovering and recommending **furniture**. Whether you're looking for a stylish sofa, a space-saving table, or the perfect chair for your living room, the agent is here to help — just ask.

---

## 🛠️ Technologies Used

* 🧠 OpenAI Agents SDK (using function calling)
* 🪑 Furniture product API (public or mock)
* 🐍 Python 3
* 🌿 Dotenv for key management
* 🔧 Requests for API calls
* 💬 Rich for formatted terminal output

---

## 💡 Features

* 🔍 Real-time product fetching from an API
* 🤖 Natural language understanding and smart suggestions
* 🛋️ Tailored furniture recommendations based on user input
* 🎨 Optional input: style, room type, and color
* 🧪 Easily extendable with new tools or filters

---

## 💬 Example Prompts

```bash
What should I buy today?
Can you suggest a modern chair for my bedroom?
Recommend a gift-worthy item for my mom.
Show me a white table that fits in a small space.
```

---

## ⚙️ How It Works

1. **User Input:** A natural-language query is passed to the agent
2. **Agent Understanding:** The LLM interprets the user’s intent
3. **Tool Calling:** Product API is accessed via `@function_tool`
4. **Response:** The agent formats the result and recommends an item

---

## 🚀 How to Run

1. Clone this repo
2. Create a `.env` file with your `GEMINI_API_KEY`
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the agent:

```bash
python agent.py
```

---

## 🧩 File Structure

```
├── main.py                 # Main agent code
├── .env                    # API key file
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 📈 Future Improvements

* ✅ Add filters for budget, material, and size
* 🌐 Integrate with a front-end (e.g. Streamlit or Chainlit)
* 🎤 Voice input capability
* 🛒 Wishlist and cart functionality

---

## 🙌 Acknowledgements

Special thanks to OpenAI for enabling interactive AI experiences with the `agents` SDK.
