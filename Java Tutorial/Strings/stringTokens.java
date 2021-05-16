import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        
        if (s.trim().length() < 1 || s.trim().length() > 400000) {
            System.out.print(0);
            return;
        }
        
        String[] tokens = s.trim().split("[ !,?.\\_'@]+");
        System.out.println(tokens.length);
        
        for (String token: tokens) {
            System.out.println(token);
        }
        
        scan.close();
    }
}