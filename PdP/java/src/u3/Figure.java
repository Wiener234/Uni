package u3;

abstract class Figure {
	private Point point;

	private Figure(){
		this.point = new Point();
	}

	private Figure(int x, int y, int size){
		this.point = new Point(x, y);
	}

	public void moveFigAbs(int x, int y){
		this.point.moveAbs(x, y);
	}

	public void moveFigRel(int x, int y){
		this.point.moveRel(x, y);
	}

	abstract int getSize();
	
	abstract void setSize(int size);

	abstract int calcArea();
	 
	abstract int calcCircumference();
}
