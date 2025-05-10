import { Component, Input } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-recipe-explain',
  templateUrl: './recipe-explain.component.html'
})
export class RecipeExplainComponent {
  @Input() profileId!: number;
  @Input() recipeName!: string;
  explanation: string | null = null;
  constructor(private api: ApiService) {}
  fetch() {
    this.api.getExplanation(this.profileId, this.recipeName)
      .subscribe(res => this.explanation = res.explanation);
  }
}
