import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ChatLlmComponent } from './chat-llm.component';
import { FormsModule } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('ChatLlmComponent', () => {
  let component: ChatLlmComponent;
  let fixture: ComponentFixture<ChatLlmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ChatLlmComponent],
      imports: [FormsModule, HttpClientTestingModule]
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChatLlmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create component', () => {
    expect(component).toBeTruthy();
  });

  it('should disable Ask button if patientId or question is missing', () => {
    component.patientId = '';
    component.question = '';
    fixture.detectChanges();

    const compiled = fixture.nativeElement as HTMLElement;
    const button = compiled.querySelector('button');
    expect(button?.disabled).toBeTrue();
  });
});
