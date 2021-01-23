//get data from django, check the html side as well to see how you pass data
const django_data = JSON.parse(document.getElementById('results').textContent);
console.log(django_data);
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
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

