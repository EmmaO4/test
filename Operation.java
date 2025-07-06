import java.util.Scanner;

public class Operation {

	public static void main(String [] args) {
		char ch = args[0].charAt(0);
		Scanner scan = new Scanner(System.in);
		System.out.print ("Please enter first number: ");
		int num1 = scan.nextInt();
		System.out.print ("Please enter second number: ");
		int num2 = scan.nextInt();

		switch(ch) {
			case '+':
				System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
				break;
			case '-':
				System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
				break;
			case 'x':
				System.out.println(num1 + " x " + num2 + " = " + (num1 * num2));
				break;
			case '/':
				System.out.println(num1 + " / " + num2 + " = " + ((float)num1 / (float)num2));
				break;
			case '%':
				System.out.println(num1 + " % " + num2 + " = " + (num1 % num2));
				break;	
		}
		scan.close();
	}
}
