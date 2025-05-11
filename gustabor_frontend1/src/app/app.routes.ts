import { Routes } from '@angular/router';
import { AddPatientComponent } from './components/add-patient/add-patient.component';
import { ChatLlmComponent } from './components/chat-llm/chat-llm.component';

export const routes: Routes = [
  { path: '', redirectTo: 'add-patient', pathMatch: 'full' },
  { path: 'add-patient', component: AddPatientComponent },
  { path: 'chat-llm', component: ChatLlmComponent },
  { path: '**', redirectTo: 'add-patient' }
];
