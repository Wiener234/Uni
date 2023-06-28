package u3;

public class Circ extends Square{

	Circ(){
		super();
	}

	Circ(int radius){
		super(radius);
	}

	Circ(int x, int y, int radius){
		super(x, y, radius);
	}

	@Override
	public double calcArea(){
		return Math.PI * getSize() * getSize();
	}

	@Override
	public double calcCircumference(){
		return 2 * Math.PI * getSize();
	}
}
