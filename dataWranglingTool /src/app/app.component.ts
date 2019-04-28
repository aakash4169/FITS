import { Component } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { ApiService } from './shared/api.service';
import { single } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  showHistogram:boolean = true
  showPiechart:boolean = false

  single: Object[] = [
    {
      "name": "10",
      "value": 894
    },
    {
      "name": "20",
      "value": 500
    },
    {
      "name": "30",
      "value": 478
    },
    {
      "name": "40",
      "value": 750
    },
    {
      "name": "50",
      "value": 200
    },
    {
      "name": "60",
      "value": 520
    },
    {
      "name": "70",
      "value": 500
    }
  ];

  view: any[] = [700, 400];

  //histo options
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = true;
  showXAxisLabel = true;
  xAxisLabel = '';
  showYAxisLabel = true;
  yAxisLabel = 'Count';

  //pie
  showLabels = true;
  explodeSlices = false;
  doughnut = false;

  colorScheme = {
    domain: ['#028FFB', '#00E396', '#FEB020', '#FF4560', '#775DD0']
    //['#F08080', '#F5B041', '#58D68D', '#808bdd']
  };

  handleChange(evt){
    console.log(evt)
    if(evt.target.value=="option1"){
      console.log("in radio")
      this.showHistogram = true
      this.showPiechart = false
    }else if(evt.target.value=="option2"){
      this.showPiechart = true
      this.showHistogram = false
    }
  }

  constructor(private apiService:ApiService) {}
  onChangeSelectDataOptions(e){
    console.log(e)
    console.log("selected")
    this.apiService.onGetRequest(e).subscribe(
      (result)=>{
          console.log(result)
          console.log()
      },
      (error)=>{
        console.log(error)
      }
    )
  }
  onChangeSelectOptions(e){
    console.log(e)
    this.apiService.onGetRequest(e).subscribe(
      (result)=>{
          console.log(result)
          this.single = Object(result)
          this.xAxisLabel = e
      },
      (error)=>{
        console.log(error)
      }
    )
  }
  


   // events
  public chartClicked(e:any):void {
    // console.log(e);
  }

  public onSelect(e:any):void {
    // console.log(e);
  }

  public chartHovered(e:any):void {
    // console.log(e);
  }
}
