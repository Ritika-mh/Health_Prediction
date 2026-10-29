import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PatientComponent } from './component/patient/patient.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,PatientComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('health_prediction_A');
}
