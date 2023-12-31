import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { CommandSearchService } from 'src/app/_services/command-search.service';

interface Product {
  value: string;
  viewValue: string;
}
interface Command {
  command: string;
  link: string;
  score: number;
  description: string
}

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {

  selectedProduct: string = '';
  formGroup: FormGroup;
  isLoading:boolean = false;
  topResults: Command[] = [];
  // topResults:Command[] =  [
  //   {
  //     "command": "show lc-cluster load distribution ap",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/sh-lc-clstr-ap.htm",
  //     "score": 86.51,
  //     "description": "This command displays information related to the current load distribution on the AP."
  //   },
  //   {
  //     "command": "show flow-offload status",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/a10-sh-flow-offload.htm",
  //     "score": 82.51,
  //     "description": "This command displays the current status of flow offload configuration of the AP."
  //   },
  //   {
  //     "command": "show app-services",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/sh-app-services.htm",
  //     "score": 80.97,
  //     "description": "This command displays the list of application services available on AP."
  //   }
  // ]

  timetaken: number = 0;
  copyClipboard = "Copy"


  products: Product[] = [
    {value: 'aos10', viewValue: 'AOS10'},
    {value: 'aos8', viewValue: 'AOS8'},
    {value: 'cppm', viewValue: 'CPPM'},
  ];

  constructor(private fb: FormBuilder, private commandSearch: CommandSearchService) {
    this.formGroup = this.fb.group({
      product: new FormControl(''),
      input_text: new FormControl('')
    });
  }

  ngOnInit(): void {
  }

  fetchCommands(){
    this.topResults = [];
    this.isLoading = true;
    const payload = this.formGroup.value;
    this.commandSearch.retrieveCommands(payload).subscribe(
      (response)=>{
        this.topResults = response.top3;
        this.timetaken = response.time_taken;
        this.isLoading = false;
    },(err)=>{
        console.log(err)
        this.isLoading = false;
    });
  }

}
