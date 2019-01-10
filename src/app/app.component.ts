import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {saveAs as importedSaveAs} from 'file-saver';

import {MyslaksApiService} from './myslaks/myslaks-api.service';
import {Myslak} from './myslaks/myslak.model';
import {HeadsApiService} from './myslaks/heads-api.service';
import {Head} from './myslaks/head.model';
import {BackgroundsApiService} from './myslaks/backgrounds-api.service';
import {Background} from './myslaks/background.model';
import {Cloth} from './myslaks/cloth.model';
import {ClothesApiService} from './myslaks/clothes-api.service';
import {OutlineColor} from './myslaks/outlineColor.model';
import {OutlineColorApiService} from './myslaks/outlineColor-api.service';
import {FillingColor} from './myslaks/fillingColor.model';
import {FillingColorApiService} from './myslaks/fillingColor-api.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  fillingColorSubs: Subscription;
  fillingColor: FillingColor;

  outlineColorSubs: Subscription;
  outlineColor: OutlineColor;

  myslakSubs: Subscription;
  myslak: Myslak;

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
  ) {
  }


  ngOnInit() {

    this.headsListSubs = this.headsApi
      .getHeads()
      .subscribe(res => {
          this.headsList = res;
          this.currentHead = Math.floor(Math.random() * (this.headsList.length));
        },
        console.error
      );

    this.backgroundsListSubs = this.backgroundsApi
      .getBackgrounds()
      .subscribe(res => {
          this.backgroundsList = res;
          this.currentBackground = Math.floor(Math.random() * (this.headsList.length));
        },
        console.error
      );

    this.clothesListSubs = this.clothesApi
      .getClothes()
      .subscribe(res => {
          this.clothesList = res;
          this.currentCloth = Math.floor(Math.random() * (this.headsList.length));
        },
        console.error
      );

    this.outlineColorSubs = this.outlineColorApi
      .getOutlineColor()
      .subscribe(res => {
          this.outlineColor = res;
        },
        console.error);

    this.fillingColorSubs = this.fillingColorApi
      .getFillingColor()
      .subscribe(res => {
          this.fillingColor = res;

        },
        console.error);

  };

  ngOnDestroy() {
    this.myslakSubs.unsubscribe();
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
        console.log(err);
      });
  }

  onClickFillingColor() {
    this.fillingColorApi.updateFillingColor(this.fillingColor)
      .subscribe(res => {
        this.fillingColor = res;
      }, err => {
        console.log(err)
      })
  }


  OnClickNextBackground() {
    if (this.currentBackground != this.backgroundsList.length - 1) {
      this.currentBackground++;
    } else {
      this.currentBackground = 0
    }
  }

  OnClickPreviousBackground() {
    if (this.currentBackground != 0) {
      this.currentBackground--
    }
  }

  OnClickNextHead() {
    if (this.currentHead != this.headsList.length - 1) {
      this.currentHead++;

    } else {
      this.currentHead = 0
    }
  }

  OnClickPreviousHead() {
    if (this.currentHead != 0) {
      this.currentHead--;
    }
  }

  OnClickNextCloth() {
    if (this.currentCloth != this.clothesList.length - 1) {
      this.currentCloth++;
    } else {
      this.currentCloth = 0
    }
  }

  OnClickPreviousCloth() {
    if (this.currentCloth != 0) {
      this.currentCloth--;
    }
  }

  OnClickSaveMyslak() {
    this.myslak = new Myslak('name', 'description',
      this.outlineColor.color, this.fillingColor.color, this.backgroundsList[this.currentBackground].id,
      this.clothesList[this.currentCloth].id, this.headsList[this.currentHead].id)
    console.log(this.myslak)
    this.myslaksApi
      .saveMyslak(this.myslak)
      .subscribe(
        myslakImage => {
          importedSaveAs(myslakImage, 'myslak');
        },
        error => alert(error.message)
      );
  }
}
