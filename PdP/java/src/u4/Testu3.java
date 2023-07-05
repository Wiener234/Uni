package u4;

import u3.Circle;
import u3.Square;

public class Testu3 {

	public static void main(String[] args){
		Circle circle = new Circle(1,2,4);
		Square square = new Square(1,2,3);	
		square.show();
		Square newsquare = new Square(square);
		newsquare.show();
		System.out.println(square.toString());
		System.out.println(newsquare.toString());
	}
}
