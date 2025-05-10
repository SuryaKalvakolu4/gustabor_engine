import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-recipe-result',
  templateUrl: './recipe-result.component.html'
})
export class RecipeResultComponent {
  @Input() recipes: any[] = [];
}
