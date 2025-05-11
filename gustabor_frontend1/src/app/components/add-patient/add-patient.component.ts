import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  ReactiveFormsModule,
  FormsModule,
  FormBuilder,
  FormGroup,
  Validators
} from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-add-patient',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FormsModule],
  templateUrl: './add-patient.component.html',
  styleUrls: ['./add-patient.component.css']
})
export class AddPatientComponent {
  patientForm!: FormGroup;

  submitted = false;
  successMessage = '';
  errorMessage = '';

  tasteOptions = ['Sweet', 'Salty', 'Bitter', 'Umami', 'Sour'];
  textureOptions = ['Creamy', 'Crunchy', 'Smooth', 'Chewy'];
  symptomOptions = ['Nausea', 'Dry mouth', 'Loss of appetite'];

  constructor(private fb: FormBuilder, private apiService: ApiService) {
    this.patientForm = this.fb.group({
      patient_id: ['', Validators.required],
      name: ['', Validators.required],
      taste_preferences: [[]],
      texture_likes: [[]],
      dietary_restrictions: [''],
      symptoms: [[]],
      sensory_scores: this.fb.group({
        sweet: [null],
        salty: [null],
        bitter: [null],
        umami: [null],
        sour: [null]
      }),
      known_deficits: ['']
    });
  }

  onCheckboxChange(event: any, controlName: string): void {
    const control = this.patientForm.get(controlName);
    if (!control) return;

    const currentValue = control.value as string[];
    const value = event.target.value;

    if (event.target.checked) {
      control.setValue([...currentValue, value]);
    } else {
      control.setValue(currentValue.filter(v => v !== value));
    }
  }

  onSubmit(): void {
    this.submitted = true;
    if (this.patientForm.invalid) return;

    const formData = this.patientForm.value;

    const payload = {
      patient_id: formData.patient_id,
      name: formData.name,
      subjective_input: {
        taste_preferences: formData.taste_preferences,
        texture_likes: formData.texture_likes,
        dietary_restrictions: formData.dietary_restrictions
          ? [formData.dietary_restrictions]
          : [],
        symptoms: formData.symptoms
      },
      objective_input: {
        sweet: formData.sensory_scores.sweet,
        salty: formData.sensory_scores.salty,
        bitter: formData.sensory_scores.bitter,
        umami: formData.sensory_scores.umami,
        sour: formData.sensory_scores.sour,
        deficits: formData.known_deficits
          ? [formData.known_deficits]
          : []
      }
    };

    this.apiService.addPatient(payload).subscribe({
      next: () => {
        this.successMessage = 'Patient data saved successfully.';
        this.errorMessage = '';
        this.patientForm.reset();
        this.submitted = false;
      },
      error: (err) => {
        console.error(err);
        this.errorMessage = 'Failed to save patient data.';
        this.successMessage = '';
      }
    });
  }
}
