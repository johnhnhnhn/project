// React component to fetch and display articles
import React, { useEffect, useState } from 'react';

const Dashboard = () => {
  const [data, setData] = useState({ articles: [], sentiments: [], trends: [] });

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/articles')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <ul>
        {data.articles.map((article, index) => (
          <li key={index}>
            <h2>{article.title}</h2>
            <p>{article.link}</p>
            <p>Sentiment: {data.sentiments[index]}</p>
            <p>Trend: {data.trends[index]}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
