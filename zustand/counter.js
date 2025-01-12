import React from 'react';
import { useStore } from './store';  // Import your store

const Counter = () => {
  // Access state from the store
  const { count, increase, decrease } = useStore();

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increase}>Increase</button>
      <button onClick={decrease}>Decrease</button>
    </div>
  );
};

export default Counter;
