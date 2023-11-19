import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

interface RetrieveCommands{
  input_text: string,
  product: ["aos8", "aos10", "cppm"]
}

@Injectable({
  providedIn: 'root'
})
export class CommandSearchService {

  constructor(private http: HttpClient) { }

  retrieveCommands(params: RetrieveCommands): Observable<any>{
    return this.http.post(`${environment.api_endpoint}/command-retriever`, params, {headers: {'Content-Type': 'application/json'}});
  }
}
