import java.util.Scanner;

public class Main{
	
	// menu
	public static int menu(){
		Scanner scan2 = new Scanner(System.in);
		System.out.println("1. Decode");
		System.out.println("2. Encode");
		System.out.println("3. Quit");
		int chs = 0;
		while (true){
			System.out.printf("Please enter your choise : ");
			chs = scan2.nextInt();
			if((chs == 1)||(chs == 2)||(chs == 3)) {		
				break;
			}
		}
		return chs;
	}
	// decode (decipher)
	public static void decode(){
		Scanner scan3 = new Scanner(System.in);
		System.out.printf("Please enter your message : ");
		String msg = scan3.nextLine();
		msg = msg.toUpperCase(); // MESSAGE
		
		int key;
		System.out.printf("Please enter your key : ");
		while (true) {
			key=scan3.nextInt();
			if (key > 0){
				break;
			}
		}
		String A = "";
		int temp;
		for (int i=0 ; i<msg.length();i++){
			
			if  ((((int)msg.charAt(i)) > (64)) && (((int)msg.charAt(i)) < (65+key))){
				temp = ((int)msg.charAt(i)-key);
				temp = 64 - temp;
				temp = 90-temp;
				A += (char)(temp);		
			}
			else if(((int)msg.charAt(i)) < (65)){
				A += " ";
			}
			else{
				A += (char)((int)msg.charAt(i)-key);  
			}
		}
		System.out.println(A);	
	}
	
	// encode (cipher)
	public static void encode(){
		Scanner scan = new Scanner(System.in);
		System.out.printf("Please enter your message : ");
		String msg = scan.nextLine();
		msg = msg.toUpperCase(); // MESSAGE
		
		int key;
		System.out.printf("Please enter your key : ");
		while (true) {
			key=scan.nextInt();
			if (key > 0){
				break;
			}
		}
		String A = "";
		for (int i=0 ; i<msg.length();i++){
			if (((int)msg.charAt(i)) > (90-key)){
				int temp = ((int)msg.charAt(i)+key)%90;
				temp = temp + 64;
				A += (char)(temp);		
		}
		else if(((int)msg.charAt(i)) < (65)){
			A += " ";
		}
		
		else{
			A += (char)((int)msg.charAt(i)+key);  
		}
			
	    }
		System.out.println(A);	
	}
	
	
	
	public static void main(String[] args){
		
		int res;
		while (true) {
			
			res = menu();
			if(res == 1) {
				decode();
			}
			else if(res == 2){
				encode();
			}
			else if(res == 3){
				break;
			}
		}
		
	}
}