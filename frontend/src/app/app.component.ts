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
import {FillingColor} from "./myslaks/fillingColor.model";
import {FillingColorApiService} from "./myslaks/fillingColor-api.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Wonderful Myslak World';

  fillingColorSubs: Subscription;
  fillingColor: FillingColor;

  outlineColorSubs: Subscription;
  outlineColor: OutlineColor;

  myslaksListSubs: Subscription;
  myslaksList: Myslak[];

  headsListSubs: Subscription;
  headsList: Head[];
  currentHead = 0;

  backgroundsListSubs: Subscription;
  backgroundsList: Background[];
  currentBackground = 0;

  clothesListSubs: Subscription;
  clothesList: Cloth[];
  currentCloth = 0

  constructor(
    private myslaksApi: MyslaksApiService,
    private headsApi: HeadsApiService,
    private backgroundsApi: BackgroundsApiService,
    private clothesApi: ClothesApiService,
    private outlineColorApi: OutlineColorApiService,
    private fillingColorApi: FillingColorApiService
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
          console.log('elo')
        },
        console.error
      );

    console.log('kolor to', this.outlineColor)
    this.outlineColorSubs = this.outlineColorApi
      .getOutlineColor()
      .subscribe(res => {
          this.outlineColor = res
        },
        console.error)

    this.fillingColorSubs = this.fillingColorApi
      .getFillingColor()
      .subscribe(res => {
          this.fillingColor = res
        },
        console.error)
  };

  ngOnDestroy() {
    this.myslaksListSubs.unsubscribe();
    this.headsListSubs.unsubscribe();
    this.backgroundsListSubs.unsubscribe();
    this.clothesListSubs.unsubscribe();
    this.outlineColorSubs.unsubscribe();
    this.fillingColorSubs.unsubscribe();
  };

  onClickOutlineColor() {
    this.outlineColorApi.updateOutlineColor(this.outlineColor)
      .subscribe(res => {
        this.outlineColor = res;
      }, err => {
        console.log(err)
      })
  }

  onClickFillingColor() {
    console.log('weszlem!')
    this.fillingColorApi.updateFillingColor(this.fillingColor)
      .subscribe(res => {
        console.log('weszlem2!', res)
        this.fillingColor = res;
      }, err => {
        console.log(err)
      })
  }


  OnClickNextBackground() {
    if (this.currentBackground != this.backgroundsList.length - 1) {
      this.currentBackground++
    }
  }

  OnClickPreviousBackground() {
    if (this.currentBackground != 0) {
      this.currentBackground--
    }
  }

  OnClickNextHead() {
    if (this.currentHead != this.headsList.length - 1) {
      this.currentHead++
    }
  }

  OnClickPreviousHead() {
    if (this.currentHead != 0) {
      this.currentHead--
    }
  }

  OnClickNextCloth() {
    if (this.currentCloth != this.clothesList.length - 1) {
      this.currentCloth++
    }
  }

  OnClickPreviousCloth() {
    if (this.currentCloth != 0) {
      this.currentCloth--
    }
  }
}
