import { z } from 'zod/v4';


export const user = z.object({
  username: z.coerce.string(),
  password: z.coerce.string()
})

export type User = z.infer<typeof user>