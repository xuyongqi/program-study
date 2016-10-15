import java.util.*;

class shuzhi {
	public static void main(String[] args) {
		
		int x=(int)(Math.random()*100);
		Scanner il =new Scanner(System.in);
		while (true) {
			System.out.println("请输入一个数字:");
			int b = il.nextInt();
			if (b == x) { //如果b的值=x的值，输出“正确”并跳出循环
			   System.out.println("正确");
			   break;
			} else if (b < x) {
			   System.out.println("小了");
			} else if (b > x) {
			   System.out.println("大了");
			}
		}				
	}
}