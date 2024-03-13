

import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5101/api/v0.1.0/',
});

export default api;
