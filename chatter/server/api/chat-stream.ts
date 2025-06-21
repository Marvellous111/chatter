import { defineEventHandler } from 'h3';
import axios from 'axios';
import type { IncomingMessage, ServerResponse } from 'http';

export default defineEventHandler(async (event) => {

  if (event.method !== 'POST') {
    throw createError({
      statusCode: 405,
      statusMessage: 'Method Not Allowed'
    })
  }
  const config = useRuntimeConfig().server;
  const body = await readBody(event);

  const backend_url = config.backend_url;

  setHeaders(event, {
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Transfer-Encoding': 'Chunked'
  })

  try {
    const controller = new AbortController();
    console.log(`${event.method} request for chat response to server`)
    const serverResponse = await axios.post(`${backend_url}`,
      body,
      {
        responseType: 'stream',
        headers: {
          'Accept': 'text/plain'
        },
        timeout: 100000,
      }
    )
    const response = serverResponse.data;


    const readableStream = new ReadableStream({
      async start(controller) {
        response.on('data', (chunk: Buffer) => {
          controller.enqueue(new Uint8Array(chunk))
        })
        response.on('end', () => {
          console.log("Server stream end")
          controller.close()
        })
        response.on('error', (error: Error) => {
          console.error('Server stream error: ', error)
          controller.error(error)
        })
      },
      cancel() {
        console.log("Stream is cancelled by user client")
        response.destroy()
      }
    })
    console.log(readableStream)
    return readableStream
  } catch(error: any) {
    console.error("Server streaming error: ", error)
    if (error.name === 'AbortError') {
      throw createError({
        statusCode: 408,
        statusMessage: 'Request timeout'
      })
    }
    throw createError({
      statusCode: 500,
      statusMessage: "Failed to stream from server"
    })
  }
})