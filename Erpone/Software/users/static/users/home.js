//get data from django, check the html side as well to see how you pass data
const django_data = JSON.parse(document.getElementById('results').textContent);
console.log(django_data);

// Get the modal
var modal = document.getElementById("myModal");
var modal_content = document.getElementById("modal_content");



class Result {
  constructor(data) {
    //div for type 
    this.type_Div = document.createElement("div");
    this.type_p = document.createElement("p");
    this.type_p.innerText = "Type = " + data['type'];
    this.type_Div.appendChild(this.type_p);
    modal_content.appendChild(this.type_Div);

    //div for sample number 
    this.sample_number_Div = document.createElement("div");
    this.sample_n = document.createElement("p");
    this.sample_n.innerText = "Sample number = " + data['nsample'][0] + ' and ' + data['nsample'] [1]
    this.sample_number_Div.appendChild(this.sample_n);
    modal_content.appendChild(this.sample_number_Div);

    //div for alimit 
    this.alimit_Div = document.createElement("div");
    this.alimit_p = document.createElement("p");
    this.alimit_p.innerText = "Acceptation limit = " + data['alimit'][0] + ' and ' + data['alimit'] [1]
    this.sample_number_Div.appendChild(this.alimit_p);
    modal_content.appendChild(this.alimit_Div);

    //div for rlimit 
    this.rlimit_Div = document.createElement("div");
    this.rlimit_p = document.createElement("p");
    this.rlimit_p.innerText = "Risk limit = " + data['rlimit'][0] + ' and ' + data['rlimit'] [1]
    this.rlimit_Div.appendChild(this.rlimit_p);
    modal_content.appendChild(this.rlimit_Div);

    //div for frisk 
    this.frisk_Div = document.createElement("div");
    this.frisk_p = document.createElement("p");
    this.frisk_p.innerText = "Distributor risk  = " + data['frisk']
    this.frisk_Div.appendChild(this.frisk_p);
    modal_content.appendChild(this.frisk_Div);

    //div for crisk 
    this.crisk_Div = document.createElement("div");
    this.crisk_p = document.createElement("p");
    this.crisk_p.innerText = "Distributor risk  = " + data['crisk']
    this.frisk_Div.appendChild(this.crisk_p);
    modal_content.appendChild(this.frisk_Div);

    


  }
}


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
if(django_data ['type']!= undefined)
{
  var result = new Result(django_data);
  modal.style.display = "block";
}


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


function get_mqa_list(sample_number) {
  var NQA = [];
  if (sample_number == 0){

  }
  else if (sample_number >= 2 && sample_number <=8) {
    NQA = [6.5];

  }
  else if (sample_number >= 9 && sample_number <=15) {
    NQA = [4];

  }
  else if (sample_number >= 16 && sample_number <=25) {
    NQA = [10,2.5];

  }

  else if (sample_number >= 26 && sample_number <=50) {
    NQA = [10,6.5,1.5];

  }
  else if (sample_number >= 51 && sample_number <=90) {
    NQA = [10,6.5,4,1];

  }
  else if (sample_number >= 91 && sample_number <=150) {
    NQA = [10,6.5,4,2.5,0.65];

  }

  else if (sample_number >= 151 && sample_number <=280) {
    NQA = [10,6.5,4,2.5,1.5,0.4];

  } 
  
  else if (sample_number >= 281 && sample_number <=500) {
    NQA = [10,6.5,4,2.5,1.5,1,0.25];

  }

  else if (sample_number >= 501 && sample_number <=1200) {
    NQA = [10,6.5,4,2.5,1.5,1,0.65,0.15];

  }

  else if (sample_number >= 1201 && sample_number <=3200) {
    NQA = [10,6.5,4,2.5,1.5,1,0.65,0.4,0.1];

  }

  else if (sample_number >= 3201 && sample_number <=10000) {
    NQA = [6.5,4,2.5,1.5,1,0.65,0.4,0.25,0.065];

  }

  else if (sample_number >= 10001 && sample_number <=35000) {
    NQA = [4,2.5,1.5,1,0.65,0.4,0.25,0.15,0.04];
  }
 
  else if (sample_number >= 35001 && sample_number <=150000) {
    NQA = [2.5,1.5,1,0.65,0.4,0.25,0.15,0.1,0.025];
  }

  else if (sample_number >= 150001 && sample_number <=500000) {
    NQA = [1.5,1,0.65,0.4,0.25,0.15,0.1,0.065,0.015];
    }

    else{
      NQA = [1,0.65,0.4,0.25,0.15,0.1,0.065,0.04,0.01];

    }
  console.log(NQA);
  return NQA
    
}

function set_mqa() {

  mqa_select = document.getElementById('aqualityl');
  mqa_select.innerHTML = '';

  lot_q = document.getElementById('Lot');

  var t = parseInt(lot_q.value);
  
  to_append = get_mqa_list(t);
  
  to_append.forEach(function(element,key) {

    mqa_select[key] = new Option(element,key);
});
  
  console.log(mqa_select);

}

function is_form_valid() {
  
 var lot = document.getElementById('Lot');
if (lot.value <= 0 )
{
  set_modal_text('Lot quantity is not correct');
  return false
}
else
return true


}

function set_modal_text(message) {
  modal_content.innerHTML = '';
  modal_content.innerText = '';
  modal_content.innerText = message ;
  modal.style.display = "block";
}
