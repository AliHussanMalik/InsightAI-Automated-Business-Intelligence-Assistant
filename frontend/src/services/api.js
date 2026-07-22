const API_BASE_URL = "http://127.0.0.1:8000";

export const uploadDataset = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/datasets/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || "Failed to upload dataset.");
  }

  return response.json();
};

export const fetchAllDatasets = async () => {
  const response = await fetch(`${API_BASE_URL}/datasets/`);
  if (!response.ok) {
    throw new Error("Failed to fetch datasets list.");
  }
  return response.json();
};

export const fetchDatasetById = async (datasetId) => {
  const response = await fetch(`${API_BASE_URL}/datasets/${datasetId}`);
  if (!response.ok) {
    throw new Error("Failed to fetch dataset details.");
  }
  return response.json();
};

export const queryDataset = async (datasetId, question) => {
  const response = await fetch(`${API_BASE_URL}/datasets/query`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      dataset_id: datasetId,
      question: question,
    }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || "Failed to process query.");
  }

  return response.json();
};
