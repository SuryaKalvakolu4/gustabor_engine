import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-patient-form',
  templateUrl: './patient-form.component.html'
})
export class PatientFormComponent {
  form = this.fb.group({
    sweet: [0.5, Validators.required],
    sour: [0.5, Validators.required],
    bitter: [0.5, Validators.required],
    salty: [0.5, Validators.required],
    umami: [0.5, Validators.required],
    dislikes: ['']
  });
  profileId?: number;
  constructor(private fb: FormBuilder, private api: ApiService) {}

  onSubmit() {
    const payload = { ...this.form.value, dislikes: this.form.value.dislikes.split(',').map(s=>s.trim()) };
    this.api.submitProfile(payload).subscribe(res => this.profileId = res.profile_id);
  }
}
