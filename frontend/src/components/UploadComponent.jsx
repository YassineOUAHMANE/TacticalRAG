import React, { useState } from 'react';
import { uploadFile } from '../api/api';

const UploadForm = () => {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (file) {
      await uploadFile(file);
      alert('Fichier téléchargé avec succès');
    }
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Télécharger</button>
    </div>
  );
};

export default UploadForm;
