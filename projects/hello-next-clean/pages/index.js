// pages/index.js
import { useEffect } from 'react';

export default function Home() {
  useEffect(() => {
    console.log('🚀 Index page loaded');
  }, []);

  return <h1>Hello from Next.js</h1>;
}
