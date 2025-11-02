import React, { useState } from 'react';
import VideoUpload from '../components/VideoUpload';
import SummaryDisplay from '../components/SummaryDisplay';
import axios from 'axios';

export default function Home() {
  const [summary, setSummary] = useState(null);

  const uploaded = (data) => {
    setSummary(data.summary);
  }

  return (
    <div>
      <h2>Upload a lecture video</h2>
      <VideoUpload onUploaded={uploaded} />
      {summary && <SummaryDisplay summary={summary} />}
    </div>
  );
}
