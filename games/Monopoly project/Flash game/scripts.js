var selected_property=undefined;
var number_of_players=0;
var players=[];
////////////////////////////////////////
function dayMode(){
  document.body.style.backgroundColor="white";/*rgba(0,0,0,1)*/
}

function nightMode(){
  document.body.style.backgroundColor="grey";/*rgba(255,255,255,1);*/
}
////////////////////////////////////////
function startTheGame(){
  ableBtn("buy");
  number_of_players = prompt("How many players will there be?", "ex: 4");
  var num, name, color;
  for (var i = 0; i < number_of_players; i++) {
    num=i+1;
    name=prompt("Enter the name of the player "+(num),"ex: James Bond");
    color=prompt("Which color do you want to take "+name+"?","ex: black, red, green...");
    players[i] = new Player(name,color);
  }
}

function endOfTurn(){
  active_player=0;
}

function Player(name,color="black"){
  this.active=false;
  this.money=250;
  this.name=name;
  this.color=color;
  this.outputMoney = function(){alert("This player money is: "+this.money)}
}

function ableBtn() {
  if (document.getElementById("buy").innerHTML == "hh") {
    document.getElementById("buy").innerHTML = "ii";
  }
  else {
    document.getElementById("buy").innerHTML = '<button class="green_button" id="buy" onclick="ableBtn()">hihi</button>';
  }
}
/*
document.getElementById("buy").addEventListener("click",ableBtn("buy"));
document.getElementById("buy").disabled = true;
*/
function buy(){
  /*player=String(active_player)+"_money";
  +=50;
  document.getElementById(player).innerHTML = "Player 1 money: "+p1_money;
  p1.outputMoney();*/
}

/*
https://codepen.io/johnnycopes/pen/yzQyMp
*/
