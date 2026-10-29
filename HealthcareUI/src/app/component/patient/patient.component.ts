import { Component, OnInit } from '@angular/core';
import { PatientService } from '../../services/patient.service';
import { Patient } from '../../models/patient.model';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-patient',
  imports: [FormsModule,CommonModule],
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css',
})
export class PatientComponent implements OnInit {

today: string = '';
  message = '';
errormessage = '';
errors: any = {};

isViewMode = false;
// selectedPatient: any = {};


  selectedPatient: any = null;
  showPopup: boolean = false;
  patient=new Patient();
  showPopupD: boolean = false;
popupMessage: string = '';
popupType: 'success' | 'error' = 'success';
  patients: any[] = [];
  // message: string = '';
  loading: boolean = false;

  constructor(private patientService: PatientService) { }

  ngOnInit(): void {
    this.getAll();
      this.today = new Date().toISOString().split('T')[0];
  }
openPopup(message: string, type: 'success' | 'error') {
  this.popupMessage = message;
  this.popupType = type;
  this.showPopupD = true;

  setTimeout(() => {
    this.showPopupD = false;
  }, 3000); // auto close after 3 sec
}

  // VIEW SINGLE PATIENT
viewPatient(id: number) {
  this.patientService.getPatientById(id).subscribe(res => {
    this.selectedPatient = res.data;
    this.showPopup = true;
  });
}

// CLOSE POPUP
closePopup() {
  this.showPopup = false;
  this.selectedPatient = null;
}
  // CREATE
  createPatient() {
     this.loading = true;
    this.patientService.createPatient(this.patient).subscribe({
  next: (res) => {
    this.loading =false;
    this.openPopup(res.message, 'success');
    this.patient = {};
    this.getAll();
    this.resetForm();
  },
  error: (error) => {
     this.loading =false;
    this.openPopup('Something went wrong', 'error');
    console.log("res",error);
    
    // this.errormessage = error.error.message || 'Something went wrong';
    this.errors = error.error.data;  // ✅ store field errors
    this.errorKeys
  }
});
  }

  // UPDATE
  updatePatient() {
     this.loading = true;
    this.patientService.updatePatient(this.patient).subscribe({
  next: (res) => {
     this.loading =false;
    this.openPopup(res.message, 'success');
    this.patient = {};
    this.getAll();
    this.resetForm();
    console.log("resp",res);
    
  },
  error: (error) => {
    console.log("res",error);
    this.loading =false;
    this.openPopup('Update failed', 'error');
    console.log("res",error);
    
    // this.errormessage = error.error.message || 'Something went wrong';
    this.errors = error.error.data;  // ✅ store field errors
    this.errorKeys
  }
});
  }

get errorKeys(): string[] {
  return this.errors ? Object.keys(this.errors) : [];
}

  // GET ALL
  getAll() {
    this.patientService.getAllPatients().subscribe(res => {
      this.patients = res.data;
    });
  }

  // EDIT
  edit(p: any) {
    this.patient = { ...p };
    this.errors = {}; // Clear previous errors when editing a new patient
  }

  // DELETE
  delete(id: number) {
    this.patientService.deletePatient(id).subscribe({
  next: (res) => {
    this.openPopup(res.message, 'success');
    this.getAll();
  },
  error: (error) => {
    this.loading =false;  
    this.openPopup('Delete failed', 'error');
  }
});
  }

  resetForm() {
    this.patient = {};
    this.errors = {};
  }
}
