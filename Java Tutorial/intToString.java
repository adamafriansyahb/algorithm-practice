import java.util.*;

public class Solution {
  
	public static void main(String[] args) {
		try {
			Scanner in = new Scanner(System.in);
			int n = in .nextInt();
			in.close();

			// 1. First approach.
			String s = Integer.toString(n);

			// 2. Second approach.
			// String s = "" + n; 

			// 3. Third approach.
			// String s = String.valueOf(n);

		   if (n == Integer.parseInt(s)) {
			System.out.println("Good job");
		   } else {
			System.out.println("Wrong answer.");
		   }
		} 
		catch (DoNotTerminate.ExitTrappedException e) {
			System.out.println("Unsuccessful Termination!!");
		}
	}
}
