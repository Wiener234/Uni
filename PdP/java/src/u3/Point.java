package u3;

public class Point {

	private int x,y;

	public Point(){
		this.x = 0;
		this.y = 0;
	}

	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}

	getX(){
		return this.x;
	}

	getY(){
		return this.y;
	}

	moveAbs(int x, int y){
		this.x = x;
		this.y = y;
	}

	moveRel(int x, int y){
		this.x += x;
		this.y += y;
	}


}
