import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MyApiService {
  private baseUrl = 'https://chat-project-cai2.onrender.com/hi';

  constructor(private http: HttpClient) {}

  getData() {
    return this.http.get(`${this.baseUrl}`);
  }
// todo change components and create db postgres
}
