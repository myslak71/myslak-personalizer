import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {MyslaksApiService} from './myslaks/myslaks-api.service';
import {Myslak} from './myslaks/myslak.model';
import {HeadsApiService} from "./myslaks/heads-api.service";
import {Head} from "./myslaks/head.model";
import {BackgroundsApiService} from "./myslaks/backgrounds-api.service";
import {Background} from "./myslaks/background.model";
import {Cloth} from "./myslaks/cloth.model";
import {ClothesApiService} from "./myslaks/clothes-api.service";
import {OutlineColor} from "./myslaks/outlineColor.model";
import {OutlineColorApiService} from "./myslaks/outlineColor-api.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Wonderful Myslak World';

  outlineColor: OutlineColor;

  myslaksListSubs: Subscription;
  myslaksList: Myslak[];

  headsListSubs: Subscription;
  headsList: Head[];

  backgroundsListSubs: Subscription;
  backgroundsList: Background[];

  clothesListSubs: Subscription;
  clothesList: Cloth[];


  constructor(
    private myslaksApi: MyslaksApiService,
    private headsApi: HeadsApiService,
    private backgroundsApi: BackgroundsApiService,
    private clothesApi: ClothesApiService,
    private outlineColorApi: OutlineColorApiService,
  ) {
  }


  ngOnInit() {
    this.myslaksListSubs = this.myslaksApi
      .getMyslaks()
      .subscribe(res => {
          this.myslaksList = res;
        },
        console.error
      );

    this.headsListSubs = this.headsApi
      .getHeads()
      .subscribe(res => {
          this.headsList = res;
        },
        console.error
      );

    this.backgroundsListSubs = this.backgroundsApi
      .getBackgrounds()
      .subscribe(res => {
          this.backgroundsList = res;
        },
        console.error
      );

    this.clothesListSubs = this.clothesApi
      .getClothes()
      .subscribe(res => {
          this.clothesList = res;
        },
        console.error
      );

    this.outlineColor = new OutlineColor('', '')

  }

  ngOnDestroy() {
    this.myslaksListSubs.unsubscribe();
    this.headsListSubs.unsubscribe();
    this.backgroundsListSubs.unsubscribe();
    this.clothesListSubs.unsubscribe()
  }

  onClickOutlineColor() {
    console.log(this.outlineColor)
    this.outlineColorApi.updateOutlineColor(this.outlineColor).subscribe()
  }
}
