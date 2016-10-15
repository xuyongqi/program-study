import java.util.*;
class Untitled {
	public static void main(String[] args) {
		int sum = 0;
		int count = 0;
		int number;
		Scanner a =new Scanner(System.in);
		System.out.print("请输入一个整数");
		number=a.nextInt();
		while (number!=-1) {
			sum=sum+number;
			count++;
			System.out.print("请输入一个整数");
			number=a.nextInt();
			}
			if (true)
			System.out.println("平均数");
			System.out.println(sum/count);
			}
}