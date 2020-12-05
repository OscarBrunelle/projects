import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

/**
 * The class <b>GameView</b> provides the current view of the entire Game. It extends
 * <b>JFrame</b> and lays out a matrix of <b>DotButton</b> (the actual game) and 
 * two instances of JButton. The action listener for the buttons is the controller.
 *
 * @author Guy-Vincent Jourdan, University of Ottawa
 */

public class GameView extends JFrame {

    private DotButton[][] board;
    private GameModel gameModel;
    private JLabel nbreOfStepsLabel = new JLabel("Number Of Steps: 0");


    /**
     * Constructor used for initializing the Frame
     * 
     * @param gameModel
     *            the model of the game (already initialized)
     * @param gameController
     *            the controller
     */

    public GameView(GameModel gameModel, GameController gameController) {
        
        super("Minesweeper : Assignment 2");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBackground(Color.WHITE);

        this.gameModel=gameModel;
        int w = gameModel.getWidth();
        int h = gameModel.getHeigth();

        JPanel dots = new JPanel();
        dots.setLayout(new GridLayout(h,w));
    
        
        board = new DotButton[h][w];
        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                board[i][j]= new DotButton(i,j,DotButton.COVERED);
                board[i][j].addActionListener(gameController);
                dots.add(board[i][j]);
            }
        }

        JButton reset = new JButton("Reset");
        reset.addActionListener(gameController);

        JButton exit = new JButton("Exit");
        exit.addActionListener(gameController);

        JPanel buttons = new JPanel();
        buttons.setBackground(Color.WHITE);
        buttons.add(reset);
        buttons.add(exit);
        buttons.add(nbreOfStepsLabel);
        
        add(dots, BorderLayout.CENTER);
        add(buttons, BorderLayout.SOUTH);

        pack();
        setVisible(true);

        update();

        repaint();
    }

    /**
     * update the status of the board's DotButton instances based 
     * on the current game model, then redraws the view
     */

    public void update(){

        int icon;
        int w = gameModel.getWidth();
        int h = gameModel.getHeigth();

        for (int i=0; i<h; i++) {
            for (int j=0; j<w; j++) {
                if (gameModel.isMined(i,j) && gameModel.hasBeenClicked(i,j)) {
                    board[i][j].setIconNumber(DotButton.CLICKED_MINE);
                }
                else if(gameModel.hasBeenClicked(i,j) || !gameModel.isCovered(i,j)){
                    icon=getIcon(i,j);
                    board[i][j].setIconNumber(icon);
                }
                else{
                    board[i][j].setIconNumber(DotButton.COVERED);
                }
            }
        }
        nbreOfStepsLabel.setText("Number Of Steps: "+gameModel.toString());

        repaint();
    }

    /**
     * returns the icon value that must be used for a given dot 
     * in the game
     * 
     * @param i
     *            the x coordinate of the dot
     * @param j
     *            the y coordinate of the dot
     * @return the icon to use for the dot at location (i,j)
     */   
    private int getIcon(int i, int j){
        
        int icon;

        if (gameModel.getNeighbooringMines(i,j)==0) { icon=0; }
        else if (gameModel.getNeighbooringMines(i,j)==1) { icon=1; }
        else if (gameModel.getNeighbooringMines(i,j)==2) { icon=2; }
        else if (gameModel.getNeighbooringMines(i,j)==3) { icon=3; }
        else if (gameModel.getNeighbooringMines(i,j)==4) { icon=4; }
        else if (gameModel.getNeighbooringMines(i,j)==5) { icon=5; }
        else if (gameModel.getNeighbooringMines(i,j)==6) { icon=6; }
        else if (gameModel.getNeighbooringMines(i,j)==7) { icon=7; }
        else if (gameModel.getNeighbooringMines(i,j)==8) { icon=8; }
        else if (gameModel.isMined(i,j)==true) { icon=9; }
        else if (gameModel.hasBeenClicked(i,j)==true) { icon=10; }
        else if (gameModel.isCovered(i,j)==true) { icon=11; }
        else{ icon=12; } //if flagged
        return icon;
    }
}