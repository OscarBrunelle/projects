import java.awt.Color;
import java.awt.Dimension;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.BorderFactory;
import javax.swing.border.Border;

public class Upgrade extends JButton{

	public Upgrade(GameModel gameModel){

		gameModel.increaseCookiesPerClick(gameModel.getCookiesPerClick());
		gameModel.increaseNumberOfCookies(-10);
	}
}