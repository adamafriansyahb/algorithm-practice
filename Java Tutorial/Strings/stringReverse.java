import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        
        // int count = 0;
        // int strLength = A.length();
        // for (int i=0; i<strLength/2; i++) {
        //     if ( A.charAt(i) == A.charAt(strLength-i-1) ) {
        //         count++;
        //     }
        // }
        
        // System.out.print(count == strLength/2 ? "Yes" : "No");
        
        // Using StringBuilder
        System.out.println(A.equals(new StringBuilder(A).reverse().toString()) ? "Yes" : "No");
        
    }
}