import { uploadCSV } from "./api";

export default function UploadCSV({ userId }) {
  return (
    <input
      type="file"
      accept=".csv"
      onChange={(e) => uploadCSV(userId, e.target.files[0])}
    />
  );
}
