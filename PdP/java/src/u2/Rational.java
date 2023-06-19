package u2;

import u2.Gcd;

public class Rational {
	private int num;
	private int denum;

	public Rational(){
		this.num = 0;
		this.denum = 1;
	}

	public Rational(int num){
		this.num = num;
		this.denum = 1;
	}

	public Rational(int num, int denum){
		this.num = num;
		this.denum = denum;
	}

	// public int gcd(){
	// 	int x = this.num;
	// 	int y = this.denum;
	// 	if(x == 0){
	// 		return y;
	// 	}
	// 	if(y == 0){
	// 		return x;
	// 	}

	// 	if(x < 0){
	// 		x = -x;
	// 	}
	// 	if(y < 0){
	// 		y = -y;
	// 	}

	// 	while(x != y){
	// 		if(x > y){
	// 			x = x - y;
	// 		}
	// 		else{
	// 			y = y - x;
	// 		}
	// 	}
	// 	return x;
	// }
	
	public Rational mult(Rational rational){
		// TODO: Aufgabe 6 
		return rational;
	}

	public void reduce(){
		int red = Gcd.gcd(this.num, this.denum);
		this.num = this.num / red;
		this.denum = this.denum / red;
	}

	public void extend(int ext){
		this.num = this.num * ext;
		this.denum = this.denum * ext;
	}

	public String toString(){
		return String.valueOf(this.num) + '/' + String.valueOf(this.denum);
	}

	public String toStringReduced(){
		reduce();
		return String.valueOf(this.num) + '/' + String.valueOf(this.denum);
	}
}
