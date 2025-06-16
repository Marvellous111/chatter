// Response interface to be gotten from the server, should be used as the schema for structure

interface Response {
  content: {
    type: string,
    required: true
  };
  datetime: {
    type: Date,
    required: true
  };
  tokenSpeed: {
    type: string,
    required: true
  };
  responseTime: {
    type: string,
    required: true
  };
  modelUsed: {
    type: string;
    required: true
  }
}

// Query interface for sending to the backend
interface Query {
  content: {
    type: String,
    required: true
  };
  modelUsed: {
    type: String,
    required: true
  };
  datetime: {
    type: String,
    required: true
  };
  attachment: {
    type: Boolean,
    default: false
  };
  websearch: {
    type: Boolean,
    default: false
  };
}