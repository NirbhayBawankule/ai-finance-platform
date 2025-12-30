import { useEffect, useState } from "react";
import { supabase } from "./supabase";
import Auth from "./Auth";
import Dashboard from "./Dashboard";

export default function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    supabase.auth.onAuthStateChange((_e, session) => {
      setUser(session?.user ?? null);
    });
  }, []);

  return user ? <Dashboard /> : <Auth />;
}
