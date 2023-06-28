package u3;


public class Circle extends Figure{
	private int radius;

	Circle(){
		super();
		this.radius = 0;
	}

	Circle(int radius){
		super();
		this.radius = radius;
	}

	Circle(int x, int y, int radius){
		super(x, y);
		this.radius = radius;
	}

	public int getSize(){
		return this.radius;
	}

	public void setSize(int radius){
		this.radius = radius;
	}

	public double calcArea(){
		return Math.PI * this.radius * this.radius;
	}

	public double calcCircumference(){
		return 2 * Math.PI * this.radius;
	}

}
