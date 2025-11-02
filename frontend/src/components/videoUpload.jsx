import React, { useState } from 'react';
import axios from 'axios';

export default function VideoUpload({ onUploaded }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!file) return;
    setLoading(true);
    const form = new FormData();
    form.append('file', file);
    const res = await axios.post('/api/video/upload', form, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    setLoading(false);
    onUploaded(res.data);
  }

  return (
    <div>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={submit} disabled={loading}>Upload</button>
    </div>
  );
}
