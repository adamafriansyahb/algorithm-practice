import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i = 0; i < 3; i++){
                String s1 = sc.next();
                int x = sc.nextInt();
                
                /* 
                    "-" -> Left indentation,
                    15s -> Min size of string,
                    0 -> Zero padding,
                    3 -> Min size of digit,
                    n -> New line
                */
                System.out.printf("%-15s%03d%n", s1, x);
            }
            System.out.println("================================");

    }
}