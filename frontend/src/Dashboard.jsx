import { useEffect, useState } from "react";
import { supabase } from "./supabase";
import { predict } from "./api";
import Charts from "./Charts";
import UploadCSV from "./UploadCSV";
import Advisor from "./Advisor";

export default function Dashboard() {
  const [data, setData] = useState({});
  const [user, setUser] = useState(null);

  useEffect(() => {
    supabase.auth.getUser().then(({ data }) => {
      setUser(data.user);
      predict(data.user.id).then(setData);
    });
  }, []);

  if (!user) return null;

  return (
    <>
      <UploadCSV userId={user.id} />
      <Charts data={data} />
      <Advisor userId={user.id} />
    </>
  );
}
