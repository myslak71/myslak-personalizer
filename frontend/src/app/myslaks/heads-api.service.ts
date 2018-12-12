import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Head} from './head.model';

@Injectable()
export class HeadsApiService {

  constructor(private http: HttpClient) {
  }

  static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }



// GET list of public, future events
  getHeads(): Observable<any> {
    return this.http
      .get(`${API_URL}/heads`)
      .catch(HeadsApiService._handleError);
  }
}
