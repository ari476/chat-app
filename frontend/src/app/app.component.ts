import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TesComponent } from "./tes/tes.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TesComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'chat-project';
}
