import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root',
})
export class PatientService {
  
 private baseUrl = "http://localhost:8000/api/users";

  constructor(private http: HttpClient) { }

  // CREATE
  createPatient(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/create/`, data);
  }

  // UPDATE
  updatePatient(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/update/`, data);
  }

  // GET ALL
  getAllPatients(): Observable<any> {
    return this.http.post(`${this.baseUrl}/getall/`, {});
  }

  // GET BY ID
  getPatientById(id: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/get/`, { id });
  }

  // DELETE
  deletePatient(id: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/delete/`, { id });
  }
}





 