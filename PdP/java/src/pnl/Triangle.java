package pnl;

import pnl.Point;

public class Triangle {
	private Point p1,p2,p3;

	public Triangle(int p1x, int p1y, int p2x, int p2y, int p3x, int p3y){
		p1 = new Point(p1x, p1y);
		p2 = new Point(p2x, p2y);
		p3 = new Point(p3x, p3y);
	}

	public boolean isDegenerated(){
		if(p1.getX() == p2.getX() && p2.getX() == p3.getX() && p3.getX() == p1.getX()){
			return true;
		}
		else if(p1.getY() == p2.getY() && p2.getY() == p3.getY() && p3.getY() == p1.getY()){
			return true;
		}
		return false;
	}

	public boolean isEquilateral(){
		if(p1.distance(p2) == p2.distance(p3) && p2.distance(p3) == p3.distance(p1)){
			return true;
		}
		return false;
	}
	public double perimeter(){
		if(isDegenerated()){
			return 0.0;
		}
		return p1.distance(p2) + p2.distance(p3) + p3.distance(p1);
	}
}
