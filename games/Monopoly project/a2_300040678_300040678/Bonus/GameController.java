import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.LinkedList;

import javax.swing.*;


/**
 * The class <b>GameController</b> is the controller of the game. It is a listener
 * of the view, and has a method <b>play</b> which computes the next
 * step of the game, and  updates model and view.
 *
 * @author Guy-Vincent Jourdan, University of Ottawa
 */


public class GameController implements ActionListener {

    private GameModel gameModel;
    private GameView gameView;

    /**
     * when the flag mode is activated, when the user clicks on a mine, it gets flagged instead of uncovered
     * when a square is flagged, it cannot be clicked
     */
    private boolean flagMode = false;
    private int flag_bool_var = 0;

    /**
     * Constructor used for initializing the controller. It creates the game's view 
     * and the game's model instances
     * 
     * @param width
     *            the width of the board on which the game will be played
     * @param height
     *            the height of the board on which the game will be played
     * @param numberOfMines
     *            the number of mines hidden in the board
     */
    public GameController(int width, int height, int numberOfMines) {

        StudentInfo.display();

        gameModel = new GameModel(width,height,numberOfMines);
        gameView = new GameView(gameModel,this);
    }


    /**
     * Callback used when the user clicks a button (reset or quit)
     *
     * @param e
     *            the ActionEvent
     */

    public void actionPerformed(ActionEvent e) {
        
        if (e.getSource() instanceof JButton) {

        	if (e.getActionCommand().equals("Set Flag Mode")) {
                if (flag_bool_var==0) {
                	flagMode = true;
                	flag_bool_var=1;
                } else{
                	flagMode = false;
                	flag_bool_var=0;
                }  
                gameView.update();
            }
            else if (e.getActionCommand().equals("Reset")) {
                reset();
            }
            else if (e.getActionCommand().equals("Exit")) {
                System.exit(0);
            }
        }

        if (e.getSource() instanceof DotButton) {

            DotButton src = (DotButton) e.getSource();
            int row = src.getRow();
            int column = src.getColumn();

           	if (flagMode) {
           		gameModel.setFlagged(column,row);
           		gameView.update();
           	} else{
           		play(column,row);
           	}
        }
    }

    /**
     * return true if the flag mode is active
     */
    public boolean getFlagMode(){
    	return flagMode;
    }

    /**
     * resets the game
     */
    private void reset(){

        gameModel.reset();
        gameView.update();
    }

    /**
     * <b>play</b> is the method called when the user clicks on a square.
     * If that square is not already clicked, then it applies the logic
     * of the game to uncover that square, and possibly end the game if
     * that square was mined, or possibly uncover some other squares. 
     * It then checks if the game
     * is finished, and if so, congratulates the player, showing the number of
     * moves, and gives to options: start a new game, or exit
     * @param width
     *            the selected column
     * @param heigth
     *            the selected line
     */
    private void play(int width, int heigth){

        if (gameModel.hasBeenClicked(width,heigth)) {
            System.out.println("Already Clicked");
        }
        else if (gameModel.isMined(width,heigth) && !gameModel.isFlagged(width,heigth)) {
            gameModel.click(width,heigth);
            gameModel.uncover(width,heigth);
            gameModel.step();
            gameModel.uncoverAll();
            gameView.update();

            JOptionPane pane = new JOptionPane();
            Object[] options = {"Play Again", "Quit"};
                String message = "Aouch, you lost in "+gameModel.getNumberOfSteps()+" steps! Would you like to play again?";
            pane.showOptionDialog(null, message, "Boom!", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE,null, options, options[0]);
            Object selectedValue = pane.getValue();
            if (selectedValue=="Play Again") {
                System.exit(0);
                reset();
            }
            else if (selectedValue=="Quit"){
                System.exit(0);
            }
        }
        else if(gameModel.getNeighbooringMines(width,heigth)==0 && !gameModel.isFlagged(width,heigth)){
            gameModel.click(width,heigth);
            gameModel.uncover(width,heigth);
            clearZone(gameModel.get(width,heigth));
            gameModel.step();
        }
        else{
            gameModel.click(width,heigth);
            gameModel.uncover(width,heigth);
            gameModel.step();


            if (gameModel.isFinished()) {
                gameModel.uncoverAll();
                gameView.update();

                JOptionPane pane = new JOptionPane();
                Object[] options = {"Play Again", "Quit"};
                String message = "Congratulations, you won in "+gameModel.getNumberOfSteps()+" steps! Would you like to play again?";
                pane.showOptionDialog(null, message, "Won", JOptionPane.DEFAULT_OPTION, JOptionPane.WARNING_MESSAGE,null, options, options[0]);
                Object selectedValue = pane.getValue();
                if (selectedValue=="Play Again") {
                    System.exit(0);
                    reset();
                }
                else if (selectedValue=="Quit"){
                    System.exit(0);
                }
            }
        }        
        gameView.update();
        }

   /**
     * <b>clearZone</b> is the method that computes which new dots should be ``uncovered'' 
     * when a new square with no mine in its neighborood has been selected
     * @param initialDot
     *      the DotInfo object corresponding to the selected DotButton that
     * had zero neighbouring mines
     */
    private void clearZone(DotInfo initialDot) {

        DotInfo d;
        int i,j;
        int x,y;
        int heigthOfGame = gameModel.getHeigth();
        int widthOfGame = gameModel.getWidth();
        int step;
        int notEmpty = 1;
        
        Stack<DotInfo> stack = new GenericArrayStack<DotInfo>(heigthOfGame*widthOfGame);
        stack.push(initialDot);
        while(!stack.isEmpty()){
            step=0;
            d = stack.pop();
            i = d.getX();
            j = d.getY();

            while (step<8) {
                if(step==0 && i>0 && j>0){
                    x=i-1;
                    y=j-1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==1 && j>0){
                    x=i;
                    y=j-1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==2 && i<heigthOfGame-1 && j>0){
                    x=i+1;
                    y=j-1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==3 && i<heigthOfGame-1){
                    x=i+1;
                    y=j;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==4 && i<heigthOfGame-1 && j<widthOfGame-1){
                    x=i+1;
                    y=j+1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==5 && j<widthOfGame-1){
                    x=i;
                    y=j+1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==6 && i>0 && j<widthOfGame-1){
                    x=i-1;
                    y=j+1;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                } else if(step==7 && i>0){
                    x=i-1;
                    y=j;
                    if (gameModel.isCovered(x,y)) {
                        gameModel.uncover(x,y);
                        if (gameModel.getNeighbooringMines(x,y)==0) {
                            stack.push(gameModel.get(x,y));
                        }
                    }
                }
                step++;
            }
        }
        gameView.update();
    }
}