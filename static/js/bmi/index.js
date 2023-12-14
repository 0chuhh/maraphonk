function calculate(){
    //Need to determine the constant of some id functions.
      var bmi;
      var result = document.getElementById("result");
    //The value of the height slider
      var height = parseInt(document.getElementById("height").value);
    //The value of the weight slider
      var weight = parseInt(document.getElementById("weight").value);

    //The value of height and width should be displayed in the webpage using "textContent".
      document.getElementById("weight-val").textContent = weight + " кг";
      document.getElementById("height-val").textContent = height + " см";

  //Now I have added the formula for calculating BMI in "bmi"
      bmi = (weight / Math.pow( (height/100), 2 )).toFixed(1);
    //With the help of "textContent" we have arranged to display in the result page of BMI
      result.textContent = bmi;


    //Now we have to make arrangements to show the text


    //When the BMI is less than 18.5, you can see the text below
      if(bmi < 18.5){
          category = "Недовес 😒";
          result.style.color = "#ffc44d";
      }

    //If BMI is >=18.5 and <=24.9
      else if( bmi >= 18.5 && bmi <= 24.9 ){
          category = "Нормальный вес 😁";
          result.style.color = "#0be881";
      }

    //If BMI is >= 25 and <= 29.9
      else if( bmi >= 25 && bmi <= 29.9 ){
          category = "Лишний вес 😮";
          result.style.color = "#ff884d";
      }

    //If BMI is <= 30
      else{
          category = "Ожирение 😱";
          result.style.color = "#ff5e57";
      }
    //All of the above text is stored in "category".

  //Now you have to make arrangements to display the information in the webpage with the help of "textContent"
      document.getElementById("category").textContent = category;
  }