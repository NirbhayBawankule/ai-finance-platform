const API = import.meta.env.VITE_BACKEND_URL;

export const predict = (userId) =>
  fetch(`${API}/predict`, {
    method: "POST",
    headers: { user_id: userId }
  }).then(res => res.json());

export const uploadCSV = (userId, file) => {
  const form = new FormData();
  form.append("file", file);

  return fetch(`${API}/upload-csv`, {
    method: "POST",
    headers: { user_id: userId },
    body: form
  });
};
