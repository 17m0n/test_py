const axios = require('axios');
const app = require('../app');

describe('API HTTP status codes', () => {
  it('returns 404 Not Found for the root route', async () => {
    const response = await axios.get('http://localhost:3000/');
    expect(response.status).toBe(404);
  });

  it('returns 409 Conflict for POST requests to /users', async () => {
    const response = await axios.post('http://localhost:3000/users', {
      name: 'John Doe',
      email: 'john.doe@example.com',
    });
    expect(response.status).toBe(409);
  });

  // add more tests for other unsuccessful routes here...
});
