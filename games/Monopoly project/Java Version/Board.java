/**
 * @author Oscar Brunelle
 */

public class Board {

public Card[] board = new Card[40];

public static void createBoard(){
        String card_name;
        for (int i; i<board.length(); i++) {
                card_name = getCardName(i);
                board[i] = new Card(card_name);
        }
}
}
