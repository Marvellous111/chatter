// Response interface to be gotten from the server, should be used as the schema for structure

interface Response {
  content: String;
  datetime: Date;
  tokenSpeed: String;
  responseTime: String;
  modelUsed: String;
}

// Query interface for sending to the backend
interface Query {
  content: String;
  modelUsed: String;
  datetime: String;
  attachmentStatus: Boolean;
  websearch: Boolean;
  deepreasoning: Boolean;
  attachment?: File;
}
