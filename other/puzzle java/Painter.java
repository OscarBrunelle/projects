import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Line2D;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

/**
 * This program demonstrates how to draw lines using Graphics2D object.
 * 
 * @author www.codejava.net
 *
 */
public class Painter extends JFrame {
	public Painter() {
		super("Lines Drawing Demo");
		setSize(480, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
	}

	void drawLines(Graphics g) {
		Graphics2D g2d = (Graphics2D) g;
		/*
		g2d.setColor(Color.RED);

		// creates a solid stroke with line width is 2
		Stroke stroke = new BasicStroke(2f);
		g2d.setStroke(stroke);

		//dashed line
		float[] dashingPattern1 = {2f, 2f};
		Stroke stroke1 = new BasicStroke(2f, BasicStroke.CAP_BUTT,
		BasicStroke.JOIN_MITER, 1.0f, dashingPattern1, 2.0f);
 
		g2d.setStroke(stroke1);
		
		// this stroke with default CAP_SQUARE and JOIN_MITER
		Stroke stroke1 = new BasicStroke(12f);
		// this stroke with CAP_BUTT
		Stroke stroke2 = new BasicStroke(12f, BasicStroke.CAP_BUTT, BasicStroke.JOIN_MITER);
		// this stroke with CAP_ROUND
		Stroke stroke3 = new BasicStroke(12f, BasicStroke.CAP_ROUND, BasicStroke.JOIN_MITER);

		// this stroke with default CAP_SQUARE and JOIN_MITER
		Stroke stroke1 = new BasicStroke(12f);
		// this stroke with JOIN_BEVEL
		Stroke stroke2 = new BasicStroke(12f, BasicStroke.CAP_SQUARE, BasicStroke.JOIN_BEVEL);
		// this stroke with JOIN_ROUND
		Stroke stroke3 = new BasicStroke(12f, BasicStroke.CAP_SQUARE, BasicStroke.JOIN_ROUND);
		*/
		g2d.drawLine(120, 50, 360, 50);

		g2d.draw(new Line2D.Double(59.2d, 99.8d, 419.1d, 99.8d));

		g2d.draw(new Line2D.Float(21.50f, 132.50f, 459.50f, 132.50f));

	}

	public void paint(Graphics g) {
		super.paint(g);
		drawLines(g);
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(new Runnable() {
			@Override
			public void run() {
				new Painter().setVisible(true);
			}
		});
	}
}