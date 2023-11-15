import { TestBed } from '@angular/core/testing';

import { CommandSearchService } from './command-search.service';

describe('CommandSearchService', () => {
  let service: CommandSearchService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CommandSearchService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
