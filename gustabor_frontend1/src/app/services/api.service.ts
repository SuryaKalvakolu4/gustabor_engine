import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000'; // adjust if deployed elsewhere

  constructor(private http: HttpClient) {}

  addPatient(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/patients/`, data);
  }

  askLlm(patientId: string, question: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/chat/`, {
      patient_id: patientId,
      query: question
    });
  }

  downloadReport(patientId: string): Observable<Blob> {
    return this.http.get(`${this.baseUrl}/reports/${patientId}`, {
      responseType: 'blob'
    });
  }
}
