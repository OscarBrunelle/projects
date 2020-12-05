/**
 * @author Oscar Brunelle
 */

public class Player {
public Player(/*String name = James,int number = 0,int money = 1500,String[] cards = [],int position = 0*/){
        this.name = name;
        this.number=number;
        this.money=money;
        this.cards=cards;
        this.position=position;
}

public static void movePlayer(Player player, int dices_number){
        int new_position = player.position + dices_number;
        if (new_position>=40) {
                new_position-=40;
        }
        player.position = new_position;
}
}
