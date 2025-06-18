
import React from 'react';

function ProductCard({ product }) {
  return (
    <div className="border p-2 rounded shadow">
      <img src={product.image_url} alt={product.name} className="w-full h-48 object-cover" />
      <h3>{product.name}</h3>
      <p>₹{product.price}</p>
      <p>{product.description}</p>
    </div>
  );
}

export default ProductCard;
