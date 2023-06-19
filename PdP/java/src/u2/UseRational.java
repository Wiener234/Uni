package u2;

import u2.Gcd;

public class UseRational {

	public static void main(String[] args){
		int num = Integer.parseInt(args[0]);
		int denum = Integer.parseInt(args[1]);

		Rational rational = new Rational(num, denum);

		System.out.println(Gcd.gcd(num, denum));
		System.out.println(rational.toString());
		System.out.println(rational.toStringReduced());
		rational.extend(3);
		System.out.println(rational.toString());
	}

}
