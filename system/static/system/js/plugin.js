
function printContent(el,el1){
  var restorepage = document.body.innerHTML;
  var printcontent= document.getElementById(el).innerHTML;
  var printcontent1= document.getElementById(el1).innerHTML;
  var allcontent = printcontent+printcontent1;
  document.body.innerHTML =allcontent;
  window.print();
  console.log("Done");
  document.body.innerHTML =restorepage;

}
function printContent1(el){
  var restorepage = document.body.innerHTML;
  var printcontent= document.getElementById(el).innerHTML;
  document.body.innerHTML =printcontent;
  window.print();
  console.log("Done");
  document.body.innerHTML =restorepage;

}
