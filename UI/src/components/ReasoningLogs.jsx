import { useEffect, useState } from "react"
import axios from "axios"

function ReasoningLogs() {
  const [logs, setLogs] = useState([])

  useEffect(() => {
    axios.get("http://localhost:8000/logs")
      .then((res) => {
        setLogs(res.data.logs)
      })
  }, [])

  return (
    <div>
      <h2>Reasoning Logs</h2>

      {logs.map((log, index) => (
        <p key={index}>{log}</p>
      ))}
    </div>
  )
}

export default ReasoningLogs