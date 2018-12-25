import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here
import {AppComponent} from './app.component';

import {MyslaksApiService} from './myslaks/myslaks-api.service';
import {HeadsApiService} from "./myslaks/heads-api.service";
import {BackgroundsApiService} from "./myslaks/backgrounds-api.service";
import {ClothesApiService} from "./myslaks/clothes-api.service";
import {OutlineColorApiService} from "./myslaks/outlineColor-api.service";
import {FillingColorApiService} from "./myslaks/fillingColor-api.service";
import {RouterModule, Routes} from "@angular/router";


const appRoutes: Routes = [
  { path: 'save-myslak', component: AppComponent },
  // ... other routes ...
];



@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(
      appRoutes,
    ),
  ],
  providers: [
    MyslaksApiService,
    HeadsApiService,
    BackgroundsApiService,
    ClothesApiService,
    OutlineColorApiService,
    FillingColorApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
  }
}
