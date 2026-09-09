import { serve } from './server.mjs';
const port = Number(process.argv[2] ?? 8080);
await serve(port);
console.log(`http://localhost:${port}  (Strg+C zum Beenden)`);
