import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AddPatientComponent } from './add-patient.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('AddPatientComponent', () => {
  let component: AddPatientComponent;
  let fixture: ComponentFixture<AddPatientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AddPatientComponent],
      imports: [ReactiveFormsModule, HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddPatientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the form with default values', () => {
    expect(component.patientForm).toBeTruthy();
    expect(component.patientForm.get('name')?.value).toBe('');
  });

  it('form should be invalid when required fields are empty', () => {
    expect(component.patientForm.valid).toBeFalse();
  });

  it('should submit valid form', () => {
    component.patientForm.patchValue({
      patient_id: '123',
      name: 'John',
      taste_preferences: ['Sweet'],
      texture_likes: ['Crunchy'],
      dietary_restrictions: 'Lactose-free',
      symptoms: ['Nausea'],
      sensory_scores: {
        sweet: 5,
        salty: 6,
        bitter: 4,
        umami: 7,
        sour: 3
      },
      known_deficits: 'Hypogeusia to bitterness'
    });
    expect(component.patientForm.valid).toBeTrue();
  });
});
