import { z } from 'zod/v4';


// Query schema
export const query = z.object({
  content: z.coerce.string(),
  model_used: z.coerce.string(),
  model_provider: z.coerce.string(),
  attachment_status: z.boolean(),
  websearch: z.boolean(),
  deepreasoning: z.boolean(),
})

export type Query = z.infer<typeof query>;

export const chat = z.object({
  content: z.coerce.string(),
  response: z.coerce.string(),
})
export type Chat = z.infer<typeof chat>;
// Response schema to be gotten from the server, should be used as the schema for structure
interface Response {
  content: String;
  datetime: Date;
  tokenSpeed: String;
  responseTime: String;
  modelUsed: String;
}


