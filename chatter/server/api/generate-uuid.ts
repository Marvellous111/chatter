import { defineEventHandler, setResponseHeaders, getRequestHeaders } from 'h3';
import axios from 'axios';

export default defineEventHandler(async (event) => {
  
  if (event.method !== 'GET') {
    throw createError({
      statusCode: 405,
      statusMessage: `${event.method} Method not allowed`
    })
  }

  const request_headers = getRequestHeaders(event); //Optional for the future
  const config = useRuntimeConfig().server;
  const backend_url = config.backend_url;

  try {
    console.log(`${event.method} request for uuid to server`);
    const serverResponse = await axios.get(`${backend_url}generate-id`,
      {
        timeout: 100000 // This should probably be reduced to a smaller timeout limit, but since its a free server it will be like this
      }
    )
    const response = serverResponse.data
    const responseuuid = response["uuid"];
    console.log(`Generated uuid is: ${response["uuid"]}`)

    setResponseHeaders(event, {
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Transfer-Encoding': 'Chunked',
    })
    return responseuuid
  } catch(error) {
    console.log(error)
  }
})