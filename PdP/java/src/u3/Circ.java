package u3;

public class Circ extends Square{

	public Circ(){
		super();
	}

	public Circ(int radius){
		super(radius);
	}

	public Circ(int x, int y, int radius){
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
