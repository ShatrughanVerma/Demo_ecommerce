
import React, { useState } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';

function Chatbot() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const res = await axios.get(`http://localhost:5000/api/products?q=${query}`);
    setResults(res.data);
  };

  return (
    <div className="p-4">
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <button onClick={handleSearch}>Search</button>
      <div className="grid grid-cols-2 gap-4">
        {results.map(product => <ProductCard key={product.id} product={product} />)}
      </div>
    </div>
  );
}

export default Chatbot;
