import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';


const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};

@Injectable()
export class OutlineColorApiService {

  constructor(private http: HttpClient) {
  };

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }


  updateOutlineColor(outlineColor): Observable<any> {
    return this.http.post(`${API_URL}/outline_color`, outlineColor, httpOptions)
  }

  getOutlineColor(): Observable<any> {
    return this.http.get(`${API_URL}/outline_color`).catch(OutlineColorApiService._handleError);
  }

}
