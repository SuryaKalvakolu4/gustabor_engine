import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { PatientFormComponent } from './components/patient-form/patient-form.component';
import { RecipeResultComponent } from './components/recipe-result/recipe-result.component';
import { RecipeExplainComponent } from './components/recipe-explain/recipe-explain.component';

@NgModule({
  declarations: [
    AppComponent,
    PatientFormComponent,
    RecipeResultComponent,
    RecipeExplainComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
