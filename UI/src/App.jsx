import ChatWindow from "./components/ChatWindow"
import AdminPanel from "./components/AdminPanel"
import ReasoningLogs from "./components/ReasoningLogs"

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Refund Agent</h1>

      <ChatWindow />
      <AdminPanel />
      <ReasoningLogs />
    </div>
  )
}

export default App