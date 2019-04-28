import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  api_url:string="http://127.0.0.1:5000/"

  constructor(private httpclient:HttpClient) {}
  
  onGetRequest(value){
    console.log(value)
    return this.httpclient.post(`${this.api_url}requestForData`, value, httpOptions)
  }
}

