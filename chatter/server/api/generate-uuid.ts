import { defineEventHandler } from 'h3';
import axios from 'axios';

export default defineEventHandler(async (event) => {
  
  if (event.method !== 'GET') {
    throw createError({
      statusCode: 405,
      statusMessage: `${event.method} Method not allowed`
    })
  }


  const config = useRuntimeConfig().server
  const backend_url = config.backend_url

  setHeaders(event, {
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Transfer-Encoding': 'Chunked'
  })

  try {
    console.log(`${event.method} request for uuid to server`);
    const serverResponse = await axios.get(`${backend_url}generate-unsignedid`,
      {
        timeout: 10000
      }
    )
    const response = serverResponse.data
    const responseuuid = response["uuid"];
    console.log(`Generated uuid is: ${response["uuid"]}`)
    return responseuuid
  } catch(error) {
    console.log(error)
  }
})