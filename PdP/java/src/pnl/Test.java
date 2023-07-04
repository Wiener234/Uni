package pnl;

import pnl.Point;

public class Test {

	public static void main(String[] args){
		Point point = new Point(2,3);
		Point point1 = new Point(4,5);
		System.out.println(point.distance(point1));

		Triangle tri = new Triangle(0,5,0,0,5,3);
		System.out.println(tri.isDegenerated());
		System.out.println(tri.isEquilateral());
		System.out.println(tri.perimeter());

	}

}
