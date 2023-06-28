package u3;

public class Square extends Figure{
	private int side;

	public Square(){
		super();
	}

	public Square(int side){
		this.side = side;
	}
	
	public Square(int x, int y, int side){
		super(x, y);
		this.side = side;
	}

	public int getSize(){
		return this.side;
	}

	public void setSize(int side){
		this.side = side;
	}

	public double calcArea(){
		return this.side * this.side;
	}

	public double calcCircumference(){
		return this.side * 4;
	}



}
