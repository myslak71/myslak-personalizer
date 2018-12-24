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
import {Router} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  authenticated = false;
  title = 'Create your own Myslak!';

  fillingColorSubs: Subscription;
  fillingColor = new FillingColor('#f0f034', '')

  outlineColorSubs: Subscription;
  outlineColor = new OutlineColor('#000000', '')

  myslaksListSubs: Subscription;
  myslaksList: Myslak[];
  myslakSubs: Subscription;
  myslak = new Myslak('Myslak', 'Your own Myslak', '#000000', '#f0f034', 1, 1, 1);

  headsListSubs: Subscription;
  headsList: Head[];
  currentHead = 0;

  backgroundsListSubs: Subscription;
  backgroundsList: Background[];
  currentBackground = 0;

  clothesListSubs: Subscription;
  clothesList: Cloth[];
  currentCloth = 0;

  constructor(
    private myslaksApi: MyslaksApiService,
    private headsApi: HeadsApiService,
    private backgroundsApi: BackgroundsApiService,
    private clothesApi: ClothesApiService,
    private outlineColorApi: OutlineColorApiService,
    private fillingColorApi: FillingColorApiService,
    private router: Router
  ) {
  }


  ngOnInit() {

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


    const self = this;


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
        this.myslak.outline_color = this.outlineColor.color
      }, err => {
        console.log(err)
      })
  }

  onClickFillingColor() {
    this.fillingColorApi.updateFillingColor(this.fillingColor)
      .subscribe(res => {
        this.fillingColor = res;
        this.myslak.filling_color = this.fillingColor.color

      }, err => {
        console.log(err)
      })
  }


  OnClickNextBackground() {
    if (this.currentBackground != this.backgroundsList.length - 1) {
      this.currentBackground++
      this.myslak.background = this.backgroundsList[this.currentBackground].id
    }
  }

  OnClickPreviousBackground() {
    if (this.currentBackground != 0) {
      this.currentBackground--
      this.myslak.background = this.backgroundsList[this.currentBackground].id
    }
  }

  OnClickNextHead() {
    if (this.currentHead != this.headsList.length - 1) {
      this.currentHead++
      this.myslak.head = this.headsList[this.currentHead].id

    }
  }

  OnClickPreviousHead() {
    if (this.currentHead != 0) {
      this.currentHead--
      this.myslak.head = this.headsList[this.currentHead].id
    }
  }

  OnClickNextCloth() {
    if (this.currentCloth != this.clothesList.length - 1) {
      this.currentCloth++
      this.myslak.cloth = this.clothesList[this.currentCloth].id
      console.log(this.myslak)
    }
  }

  OnClickPreviousCloth() {
    if (this.currentCloth != 0) {
      this.currentCloth--
      this.myslak.cloth = this.clothesList[this.currentCloth].id

    }
  }

  OnClickSaveMyslak() {
    console.log('siemanko')

  }
}
