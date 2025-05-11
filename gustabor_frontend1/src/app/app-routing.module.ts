import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddPatientComponent } from './components/add-patient/add-patient.component';
import { ChatLlmComponent } from './components/chat-llm/chat-llm.component';

const routes: Routes = [
  { path: 'add-patient', component: AddPatientComponent },
  { path: 'chat-llm', component: ChatLlmComponent },
  { path: '', redirectTo: 'add-patient', pathMatch: 'full' }, // Default route
  { path: '**', redirectTo: 'add-patient' } // Fallback route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
