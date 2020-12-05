import java.util.Random;

/**
 * @author Oscar Brunelle
 */

public class Monopoly {

public static void main(String[] args){
								System.out.println("Starting a new game");
}

public static int[] initializeGame(String[] players_names){
								Player[] list_of_players = new Player[players_names.length()];
								for (int i=0;i<list_of_players.length();i++) {
																Player new_player = new Player(players_names[i]);
																list_of_players[i] = new_player;
								}
}

public static void playGame(){
}

public static int rollDice(){

								Random randomGenerator = new Random();
								int dice1 = randomGenerator.nextInt(6);
								int dice2 = randomGenerator.nextInt(6);
								return (dice1+dice2);
}


//public static int[] populateArray(int position, int money){

//}

//while time >0 or win==False -> player1.money and player2.money>0:

//pay: if money<0, ennemy.victory==True
}
