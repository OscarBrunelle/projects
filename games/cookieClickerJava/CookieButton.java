import java.awt.Color;
import java.awt.Dimension;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.BorderFactory;
import javax.swing.border.Border;

public class CookieButton extends JButton{

	public CookieButton(){

		ImageIcon cookie = new ImageIcon("Cookie.png");
		setIcon(cookie);
		Border emptyBorder = BorderFactory.createEmptyBorder(0, 0, 0, 0);
    	setBorder(emptyBorder);
    	setBorderPainted(false);
	}
}