import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { enableProdMode } from '@angular/core';
import { environment } from 'src/environments/environment';

interface RetrieveCommands{
  input_text: string,
  product: ["aos8", "aos10", "cppm"]
}
if (environment.production) {
  enableProdMode();
}
@Injectable({
  providedIn: 'root'
})

export class CommandSearchService {
  private apiUrl = environment.apiUrl;
  constructor(private http: HttpClient) { }

  retrieveCommands(params: RetrieveCommands): Observable<any>{
    return this.http.post(`${this.apiUrl}/command-retriever`, params, {headers: {'Content-Type': 'application/json'}});
  }
}
