import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
interface Product {
  value: string;
  viewValue: string;
}
@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {

  selectedProduct: string = '';
  formGroup: FormGroup;

  products: Product[] = [
    {value: 'aos10', viewValue: 'AOS10'},
    {value: 'aos8', viewValue: 'AOS8'},
    {value: 'cppm', viewValue: 'CPPM'},
  ];
  constructor(private fb: FormBuilder) {
    this.formGroup = this.fb.group({
      product: new FormControl(''),
      input_text: new FormControl('')
    });
  }

  ngOnInit(): void {
  }

  fetchCommands(){
    console.log(this.formGroup.value);
  }

}
