import java.util.Random;

/**
 * The class <b>GameModel</b> holds the model, the state of the systems. 
 * It stores the following information:
 * - the state of all the ``dots'' on the board (mined or not, clicked
 * or not, number of neighbooring mines...)
 * - the size of the board
 * - the number of steps since the last reset
 *
 * The model provides all of this informations to the other classes trough 
 *  appropriate Getters. 
 * The controller can also update the model through Setters.
 * Finally, the model is also in charge of initializing the game
 *
 * @author Guy-Vincent Jourdan, University of Ottawa
 */
public class GameModel {

    private java.util.Random generator;
    private int heigthOfGame;
    private DotInfo[][] model;
    private int numberOfMines;
    private int numberOfSteps;
    private int numberUncovered;
    private int widthOfGame;


    /**
     * Constructor to initialize the model to a given size of board.
     * 
     * @param width
     *            the width of the board
     * 
     * @param heigth
     *            the heigth of the board
     * 
     * @param numberOfMines
     *            the number of mines to hide in the board
     */
    public GameModel(int width, int heigth, int numberOfMines) {
        
        widthOfGame=width;
        heigthOfGame=heigth;
        this.numberOfMines=numberOfMines;

        model= new DotInfo[heigth][width];
        reset();
    }

 
    /**
     * Resets the model to (re)start a game. The previous game (if there is one)
     * is cleared up . 
     */
    public void reset(){

        for (int i=0;i<heigthOfGame;i++) {
            for (int j=0;j<widthOfGame;j++) {
                model[i][j]=new DotInfo(i,j);
            }
        }

        int minesPlaced=0;
        int x;
        int y;
        generator = new java.util.Random();

        while(minesPlaced<numberOfMines){
            x = generator.nextInt(heigthOfGame);
            y = generator.nextInt(widthOfGame);
            if (!isMined(x,y)) {
                model[x][y].setMined();
                minesPlaced++;
            }
        }

        numberOfSteps=0;
    }


    /**
     * Getter method for the heigth of the game
     * 
     * @return the value of the attribute heigthOfGame
     */   
    public int getHeigth(){

        return heigthOfGame;
    }

    /**
     * Getter method for the width of the game
     * 
     * @return the value of the attribute widthOfGame
     */   
    public int getWidth(){

        return widthOfGame;
    }


    /**
     * returns true if the dot at location (i,j) is mined, false otherwise
    * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the status of the dot at location (i,j)
     */   
    public boolean isMined(int i, int j){

        return model[i][j].isMined();
    }


    /**
     * returns true if the dot  at location (i,j) has 
     * been clicked, false otherwise
     * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the status of the dot at location (i,j)
     */   
    public boolean hasBeenClicked(int i, int j){

        return model[i][j].hasBeenClicked();
    }


  /**
     * returns true if the dot  at location (i,j) has zero mined 
     * neighboor, false otherwise
     * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the status of the dot at location (i,j)
     */   
    public boolean isBlank(int i, int j){

        return getNeighbooringMines(i,j)==0;
    }


    /**
     * returns true if the dot is covered, false otherwise
    * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the status of the dot at location (i,j)
     */   
    public boolean isCovered(int i, int j){

        return model[i][j].isCovered();
    }


    /**
     * returns the number of neighbooring mines os the dot  
     * at location (i,j)
     *
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the number of neighbooring mines at location (i,j)
     */   
    public int getNeighbooringMines(int i, int j){

        int n=0;
        int step=0;
        int x=0;
        int y=0;

        while (step<8) {
            if(step==0 && i>0 && j>0){
                x=i-1;
                y=j-1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==1 && j>0){
                x=i;
                y=j-1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==2 && i<heigthOfGame-1 && j>0){
                x=i+1;
                y=j-1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==3 && i<heigthOfGame-1){
                x=i+1;
                y=j;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==4 && i<heigthOfGame-1 && j<widthOfGame-1){
                x=i+1;
                y=j+1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==5 && j<widthOfGame-1){
                x=i;
                y=j+1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==6 && i>0 && j<widthOfGame-1){
                x=i-1;
                y=j+1;
                if (isMined(x,y)==true) {
                    n++;
                }
            } else if(step==7 && i>0){
                x=i-1;
                y=j;
                if (isMined(x,y)==true) {
                    n++;
                }
            }
            
            step++;
        }
        return n;
    }


    /**
     * Sets the status of the dot at location (i,j) to uncovered
     * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     */   
    public void uncover(int i, int j){
        
        model[i][j].uncover();
    }


    /**
     * Sets the status of the dot at location (i,j) to clicked
     * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     */   
    public void click(int i, int j){
        
        model[i][j].click();
    }


     /**
     * Uncover all remaining covered dot
     */   
    public void uncoverAll(){
        
        for (int i=0;i<heigthOfGame;i++) {
            for (int j=0;j<widthOfGame;j++) {
                uncover(i,j);
            }
        }
    }


    /**
     * Getter method for the current number of steps
     * 
     * @return the current number of steps
     */   
    public int getNumberOfSteps(){
        
        return numberOfSteps;
    }
  

    /**
     * Getter method for the model's dotInfo reference
     * at location (i,j)
     *
      * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     *
     * @return model[i][j]
     */   
    public DotInfo get(int i, int j) {
        
        return model[i][j];
    }


   /**
     * The metod <b>step</b> updates the number of steps. It must be called 
     * once the model has been updated after the payer selected a new square.
     */
     public void step(){
        
        numberOfSteps++;
    }

 
   /**
     * The metod <b>isFinished</b> returns true if the game is finished, that
     * is, all the nonmined dots are uncovered.
     *
     * @return true if the game is finished, false otherwise
     */
    public boolean isFinished(){
        
        boolean flag=true;
        
        for (int i=0;i<heigthOfGame;i++) {
            for (int j=0;j<widthOfGame;j++) {
                if (!isMined(i,j)) {
                    if (isCovered(i,j)) {
                        flag=false;
                    }
                }
            }
        }
        return flag;
    }


   /**
     * Builds a String representation of the model
     *
     * @return String representation of the model
     */
    public String toString(){
        
        String s = Integer.toString(numberOfSteps);
        return s;
    }
}