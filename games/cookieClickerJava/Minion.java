import java.awt.Color;
import java.awt.Dimension;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.BorderFactory;
import javax.swing.border.Border;

public class Minion extends JButton{
	
	int numberOfMinions;
	double cost;

	public Minion(){

		numberOfMinions=0;
		cost=10;
	}

	public void newMinion(){

		numberOfMinions++;
		cost*=1.5;
	}

	public double getCost(){

		return cost;
	}

	public double getIncome(){

		return 2*numberOfMinions;
	}
}