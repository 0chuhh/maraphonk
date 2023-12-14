function calculate(){
      var bmr;
      var result = document.getElementById("result");

      var age = document.getElementById("age").value;
      var gender = document.querySelector('input[name="gender"]:checked').value;
      var height = parseInt(document.getElementById("height").value);
      var weight = parseInt(document.getElementById("weight").value);

      document.getElementById("age-val").textContent = age + " лет";
      document.getElementById("weight-val").textContent = weight + " кг";
      document.getElementById("height-val").textContent = height + " см";

    if(gender === "fem"){
        bmr = (655 + (9.6*weight)+(1.8*height)-(4.7*age)).toFixed(1)
    }else{
        bmr = (66 + (13.7*weight)+(5*height)-(6.8*age)).toFixed(1)
    }
    result.textContent = bmr + " калорий/день";
  }