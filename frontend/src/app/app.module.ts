import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {MyslaksApiService} from './myslaks/myslaks-api.service';

import {HeadsApiService} from "./myslaks/heads-api.service";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
  ],
  providers: [MyslaksApiService, HeadsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
