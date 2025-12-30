import { supabase } from "./supabase";

export default function Auth() {
  return (
    <button onClick={() => supabase.auth.signInWithOAuth({ provider: "google" })}>
      Login with Google
    </button>
  );
}
