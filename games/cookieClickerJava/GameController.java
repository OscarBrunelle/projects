import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class GameController implements ActionListener{

	 private GameView gameView;
	 private GameModel gameModel;

	 public GameController() {
        gameModel = new GameModel();
        gameView = new GameView(gameModel, this);
        gameView.update();
    }

    public void actionPerformed(ActionEvent e) {

        if (e.getSource() instanceof CookieButton) {
            play();
            System.out.println(gameModel);
        } else if (e.getSource() instanceof JButton) {
            JButton clicked = (JButton)(e.getSource());

            if (clicked.getText().equals("Quit")) {
                System.exit(0);
            } else if (clicked.getText().equals("Reset")){
                reset();
            }
        }
        gameView.update();
    }

    private void reset(){
        gameModel.reset();
        gameView.update();
    }

    private void play(){
        
        double click = gameModel.getCookiesPerClick();
        System.out.println(click);
        gameModel.increaseNumberOfCookies(click);
    }
}