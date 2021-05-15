import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        
        String capitalisedA = A.substring(0, 1).toUpperCase() + A.substring(1);
        String capitalisedB = B.substring(0, 1).toUpperCase() + B.substring(1);
        
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.printf("%s %s", capitalisedA, capitalisedB);
        
    }
}