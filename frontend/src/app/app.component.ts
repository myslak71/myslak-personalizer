import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {MyslaksApiService} from './myslaks/myslaks-api.service';
import {Myslak} from './myslaks/myslak.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Wonderful Myslak World';
  myslaksListSubs: Subscription;
  myslaksList: Myslak[];

  constructor(private myslaksApi: MyslaksApiService) {
  }

  ngOnInit() {
    this.myslaksListSubs= this.myslaksApi
      .getMyslaks()
      .subscribe(res => {
          this.myslaksList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.myslaksListSubs.unsubscribe();
  }
}
