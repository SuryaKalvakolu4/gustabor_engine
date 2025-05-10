import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const BASE = 'http://localhost:8000';

@Injectable({ providedIn: 'root' })
export class ApiService {
  constructor(private http: HttpClient) {}

  submitProfile(profile: any): Observable<any> {
    return this.http.post(`${BASE}/profile/`, profile);
  }

  getRecommendations(profileId: number): Observable<any> {
    return this.http.get(`${BASE}/recommend/${profileId}`);
  }

  getExplanation(profileId: number, recipeName: string): Observable<any> {
    return this.http.get(`${BASE}/explain/${profileId}/${recipeName}`);
  }
}
