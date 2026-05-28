import { useState } from "react"
import api from "../services/api"

function ChatWindow() {

  const [message, setMessage] = useState("")
  const [chat, setChat] = useState([])

  const sendMessage = async () => {

    if (!message.trim()) return

    // Add user message
    const updatedChat = [
      ...chat,
      {
        sender: "user",
        text: message
      }
    ]

    setChat(updatedChat)

    try {

      const lowerMsg = message.toLowerCase()

      // Greeting handling
      if (
        lowerMsg.includes("hi") ||
        lowerMsg.includes("hello") ||
        lowerMsg.includes("hey")
      ) {

        setChat([
          ...updatedChat,
          {
            sender: "bot",
            text:
              "Hello 👋 I am your AI Refund Support Agent. Please provide your Customer ID and Order ID."
          }
        ])

        setMessage("")
        return
      }

      // Fraud detection
      const suspiciousWords = [
        "hack",
        "chargeback",
        "lawsuit",
        "fraud"
      ]

      const suspiciousDetected =
        suspiciousWords.some(word =>
          lowerMsg.includes(word)
        )

      if (suspiciousDetected) {

        setChat([
          ...updatedChat,
          {
            sender: "bot",
            text:
              "⚠️ Suspicious activity detected. This conversation may be reviewed by security."
          }
        ])

        setMessage("")
        return
      }

      // Extract IDs
      const customerMatch =
        message.match(/CUST-\d+/i)

      const orderMatch =
        message.match(/(?:ORD|ORDER)-\d+/i)

      // Missing IDs
      if (!customerMatch || !orderMatch) {

        setChat([
          ...updatedChat,
          {
            sender: "bot",
            text:
              "Please provide your Customer ID and Order ID."
          }
        ])

        setMessage("")
        return
      }

      // Normalize IDs
      const customer_id =
        customerMatch[0].toUpperCase()

      const order_id =
        orderMatch[0]
          .replace("ORDER-", "ORD-")
          .toUpperCase()

      // API call
      const res = await api.post(
        "/chat",
        {
          customer_id,
          order_id
        }
      )

      const botMessage =
        res.data.ai_response ||
        res.data.reason ||
        "Refund processed."

      setChat([
        ...updatedChat,
        {
          sender: "bot",
          text: botMessage
        }
      ])

    } catch (err) {

      console.error(err)

      setChat([
        ...updatedChat,
        {
          sender: "bot",
          text:
            "Error processing refund request."
        }
      ])
    }

    setMessage("")
  }

  return (

    <div
      style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        maxWidth: "700px",
        margin: "auto"
      }}
    >

      <h2>AI Refund Support Agent</h2>

      {/* Chat Messages */}

      <div
        style={{
          height: "400px",
          overflowY: "auto",
          border: "1px solid #ddd",
          padding: "10px",
          marginBottom: "15px",
          borderRadius: "8px",
          background: "#f8fafc"
        }}
      >

        {chat.map((msg, index) => (

          <div
            key={index}
            style={{
              textAlign:
                msg.sender === "user"
                  ? "right"
                  : "left",
              marginBottom: "12px"
            }}
          >

            <span
              style={{
                display: "inline-block",
                padding: "10px 14px",
                borderRadius: "12px",
                background:
                  msg.sender === "user"
                    ? "#2563eb"
                    : "#e2e8f0",
                color:
                  msg.sender === "user"
                    ? "white"
                    : "black",
                maxWidth: "80%",
                whiteSpace: "pre-wrap"
              }}
            >
              {msg.text}
            </span>

          </div>
        ))}

      </div>

      {/* Input */}

      <div
        style={{
          display: "flex",
          gap: "10px"
        }}
      >

        <input
          type="text"
          placeholder="Example: Customer ID CUST-1 Order ID ORD-1"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={{
            flex: 1,
            padding: "12px"
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage()
            }
          }}
        />

        <button onClick={sendMessage}>
          Send
        </button>

      </div>

    </div>
  )
}

export default ChatWindow