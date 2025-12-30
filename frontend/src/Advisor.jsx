import { useEffect, useState } from "react";

export default function Advisor({ userId }) {
  const [advice, setAdvice] = useState("");

  useEffect(() => {
    fetch(import.meta.env.VITE_BACKEND_URL + "/advisor", {
      method: "POST",
      headers: { user_id: userId }
    })
      .then(r => r.json())
      .then(d => setAdvice(d.advice));
  }, []);

  return <p>{advice}</p>;
}
