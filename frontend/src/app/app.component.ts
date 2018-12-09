import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {MyslaksApiService} from './myslaks/myslaks-api.service';
import {Myslak} from './myslaks/myslak.model';
import {HeadsApiService} from "./myslaks/heads-api.service";
import {Head} from "./myslaks/head.model";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Wonderful Myslak World';
  myslaksListSubs: Subscription;
  myslaksList: Myslak[];
  headsListSubs:Subscription;
  headsList: Head[];
  constructor(
    private myslaksApi: MyslaksApiService,
    private headsApi: HeadsApiService
){
  }



  ngOnInit() {
    this.myslaksListSubs= this.myslaksApi
      .getMyslaks()
      .subscribe(res => {
          this.myslaksList = res;
        },
        console.error
      );

    this.headsListSubs= this.headsApi
      .getHeads()
      .subscribe(res => {
          this.headsList = res;
        },
        console.error
      );



  }

  ngOnDestroy() {
    this.myslaksListSubs.unsubscribe();
    this.headsListSubs.unsubscribe();
  }
}
