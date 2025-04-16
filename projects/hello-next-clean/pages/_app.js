// pages/_app.js
import { useEffect } from 'react';
import Script from 'next/script';

const GA_MEASUREMENT_ID = 'G-L2JT2SH6LR'; // 🔁 Replace with your own

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    console.log('✅ App loaded');
  }, []);

  return (
    <>
      {/* Google Analytics */}
      <Script
        strategy="afterInteractive"
        src={`https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`}
      />
      <Script
        id="ga-setup"
        strategy="afterInteractive"
        dangerouslySetInnerHTML={{
          __html: `
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
          gtag('config', '${GA_MEASUREMENT_ID}', {
            page_path: window.location.pathname,
          });
        `,
        }}
      />

      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
