import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Myslak} from './myslak.model';
import * as Auth0 from 'auth0-web';

@Injectable()
export class MyslaksApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }


 updateMyslak(myslak: Myslak){
    return 'siemanko'
  }

  saveMyslak(myslak: Myslak): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${Auth0.getAccessToken()}`
      })
    };
    return this.http
      .post(`${API_URL}/myslaks`, myslak, httpOptions);
  }




// GET list of public, future events
  getMyslaks(): Observable<any> {
    return this.http
      .get(`${API_URL}/myslaks`)
      .catch(MyslaksApiService._handleError);
  }
}
