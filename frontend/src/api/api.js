const API_BASE = 'http://localhost:8000';

export const askQuestion = async (question) => {
  const res = await fetch(`${API_BASE}/ask`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  });
  //console.log(res);
  return res.json();
};

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  await fetch(`${API_BASE}/upload`, {
    method: 'POST',
    body: formData,
  });
};

export const fetchStats = async () => {
  const res = await fetch(`${API_BASE}/stats`);
  return res.json();
};
