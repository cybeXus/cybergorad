window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar").style.padding = "5px 5px";
    document.getElementById("logo").style.padding = "20px 10px";
    document.getElementById("navbar").style.backgroundColor = "white";
    document.getElementById("navbar").style.boxShadow = "0 2px 5px rgba(0, 0, 0, 0.1)";
    
    // Sélectionner tous les éléments avec la classe 'test' et modifier leur couleur
    const elements = document.querySelectorAll(".test");
    elements.forEach(element => {
      element.style.color = "black";
    });

  } else {
    document.getElementById("navbar").style.padding = "5px 5px";
    document.getElementById("logo").style.padding = "30px 10px";
    document.getElementById("navbar").style.backgroundColor = "rgba(250, 241, 241, 0)";
    document.getElementById("navbar").style.boxShadow = "0 0px 0px rgba(0, 0, 0, 0.0)";
    
    // Sélectionner tous les éléments avec la classe 'test' et modifier leur couleur
    const elements = document.querySelectorAll(".test");
    elements.forEach(element => {
      element.style.color = "white";
    });
  }
}

  






  
