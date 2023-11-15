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
  // topResults:Command[] = [
  //   {
  //     "command": "show lc-cluster load distribution ap",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/sh-lc-clstr-ap.htm",
  //     "score": 85.69
  //   },
  //   {
  //     "command": "show flow-offload status",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/a10-sh-flow-offload.htm",
  //     "score": 82.4
  //   },
  //   {
  //     "command": "show port status",
  //     "link": "https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos10/sh-portstatus.htm",
  //     "score": 80.88
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

  copyCommandToClipboard(command: string): void {
    // Implement logic to copy command to clipboard
    console.log('Command copied to clipboard:', command);
  }

}
