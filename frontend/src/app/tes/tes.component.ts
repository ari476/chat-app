import { Component } from '@angular/core'
import { MyApiService } from '../my-api.service'

@Component({
  selector: 'app-tes',
  standalone: true,
  imports: [],
  templateUrl: './tes.component.html',
  styleUrl: './tes.component.scss'
})
export class TesComponent {
  constructor (private api: MyApiService) {}

  a () {
    this.api.getData().subscribe(d => {
      console.log(d)
    })
  }
}
