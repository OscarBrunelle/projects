import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class GameView extends JFrame {

    private GameModel  gameModel;
    private JLabel nbreOfCookies;
    private JLabel cookiesPerSec;

    public GameView(GameModel gameModel, GameController gameController) {
        super("Cookie Clicker v0.1");

        this.gameModel = gameModel;
 
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    	setBackground(Color.BLACK);
        setLayout(new GridLayout(2,1));

        JPanel panel = new JPanel();
        panel.setBackground(Color.WHITE);
        panel.setLayout(new GridLayout(1,3));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 0, 20));

        CookieButton cookie = new CookieButton();
        cookie.addActionListener(gameController);
        panel.add(cookie);

        /*Minion grandma = new Minion();
        grandma.addActionListener(gameController);
        panel.add(grandma);

        Upgrade up = new Upgrade(gameModel);
        up.addActionListener(gameController);
        panel.add(up);*/

    	add(panel, BorderLayout.CENTER);

        JButton buttonReset = new JButton("Reset");
        buttonReset.setFocusPainted(false);
        buttonReset.addActionListener(gameController);

        JButton buttonExit = new JButton("Quit");
        buttonExit.setFocusPainted(false);
        buttonExit.addActionListener(gameController);


  
        JPanel control = new JPanel();
        control.setBackground(Color.WHITE);
        cookiesPerSec = new JLabel();
        nbreOfCookies = new JLabel();
        control.add(cookiesPerSec);
        control.add(nbreOfCookies);
        control.add(buttonReset);
        control.add(buttonExit);

        add(control, BorderLayout.SOUTH);


    	pack();
    	//setResizable(false);
    	setVisible(true);
    }

    public void update(){
        
        cookiesPerSec.setText("Cookies Per Sec: " + gameModel.getCookiesPerSec());
        nbreOfCookies.setText("Number Of Cookies: " + gameModel.getNumberOfCookies());
        
        repaint();
    }
}