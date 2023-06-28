package u3;

import u3.Circle;
import u3.Square;
import u3.Circ;

public class Test {

	public static void main(String[] args){
		Circle circle = new Circle(2,3,6);
		System.out.println(circle.calcArea());
		System.out.println(circle.calcCircumference());
		circle.setSize(8);
		System.out.println(circle.getSize());

		Square square = new Square(2,3,6);
		System.out.println(square.calcArea());
		System.out.println(square.calcCircumference());
		square.setSize(8);
		System.out.println(square.getSize());

		Circ circ = new Circ(2,3,6);
		System.out.println(circ.calcArea());
		System.out.println(circ.calcCircumference());
		circ.setSize(8);
		System.out.println(circ.getSize());

	}

}
