import React, { useState } from 'react';
export default function QuizInterface({ questions }) {
  const [idx, setIdx] = useState(0);
  const [score, setScore] = useState(0);

  if (!questions || questions.length === 0) return <div>No questions</div>;

  const q = questions[idx];

  const answer = (i) => {
    if (i === q.answer) setScore(score + 1);
    if (idx + 1 < questions.length) setIdx(idx + 1)
    else alert(`Quiz complete. Score: ${score + (i === q.answer ? 1 : 0)} / ${questions.length}`)
  }

  return (
    <div>
      <h4>{q.question}</h4>
      <ul>
        {q.choices.map((c, i) => (
          <li key={i}><button onClick={() => answer(i)}>{c}</button></li>
        ))}
      </ul>
    </div>
  );
}
