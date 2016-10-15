import java.util.Scanner;  

class BaseTest {  
	public static void main(String[] args) {  
		Scanner in = new Scanner(System.in);
		int a;
		System.out.println("请输入一个整数");
		a = in.nextInt();
		char[] rst = ConvertTo2String(a);  
		System.out.println(rst);  
	}  
  
	public static char[] ConvertTo2String(long number) {  
		char[] output = new char[33];  
  
		int i = 0;  
		for (; i < 32; i++) {  
			output[i] = (char) (number & (1 << 31 - i));  
			output[i] = (char) (output[i] >> 31 - i);  
			output[i] = (output[i] == 0) ? '0' : '1';  
		}  
		output[i] = '\0';  
		return output;  
	}  
  
	}  