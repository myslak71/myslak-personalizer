import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Myslak} from './myslak.model';


@Injectable()
export class MyslaksApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }


  saveMyslak(myslak: Myslak): Observable<Blob> {
    return this.http.post(`${API_URL}/myslak`, myslak, {responseType: 'blob'})
  }

}
