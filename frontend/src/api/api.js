const API_BASE = 'http://localhost:8000'; // ✅ not 3000

export const askQuestion = async (question) => {
  try {
    const res = await fetch(`${API_BASE}/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`HTTP ${res.status}: ${errText}`);
    }

    return await res.json();
  } catch (err) {
    console.error("❌ Failed to reach /ask:", err);
    throw err;
  }
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
