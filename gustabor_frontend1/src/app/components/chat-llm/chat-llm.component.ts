import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-chat-llm',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat-llm.component.html',
  styleUrls: ['./chat-llm.component.css']
})
export class ChatLlmComponent {
  patientId = '';
  question = '';
  responseText = '';
  loading = false;
  errorMessage = '';

  constructor(private apiService: ApiService) {}

  onSubmit(): void {
    if (!this.patientId || !this.question) return;

    this.loading = true;
    this.responseText = '';
    this.errorMessage = '';

    this.apiService.askLlm(this.patientId, this.question).subscribe({
      next: (res: any) => {
        this.responseText = res.response || 'No response from model.';
        this.loading = false;
      },
      error: (err: any) => {
        console.error('LLM Error:', err);
        this.errorMessage = 'Something went wrong. Please try again.';
        this.loading = false;
      }
    });
  }

  onDownload(): void {
    if (!this.patientId) return;

    this.apiService.downloadReport(this.patientId).subscribe({
      next: (fileBlob: Blob) => {
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(fileBlob);
        link.download = `${this.patientId}_suggested_recipes.pdf`;
        link.click();
      },
      error: (err: any) => {
        console.error('PDF Download Error:', err);
        this.errorMessage = 'Failed to download PDF.';
      }
    });
  }
}
