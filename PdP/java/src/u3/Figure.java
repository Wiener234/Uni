package u3;

public abstract class Figure {
	private Point point;

	protected Figure(){
		this.point = new Point();
	}

	protected Figure(int x, int y){
		this.point = new Point(x, y);
	}

	public void moveFigAbs(int x, int y){
		this.point.moveAbs(x, y);
	}

	public void moveFigRel(int x, int y){
		this.point.moveRel(x, y);
	}

	public Point getPoint(){
		return this.point;
	}

	public abstract int getSize();
	
	public abstract void setSize(int size);

	public abstract double calcArea();
	 
	public abstract double calcCircumference();
}
