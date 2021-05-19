import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int n = scan.nextInt();
        int[] arr = new int[n];
        for (int i=0; i<n; i++) {
            arr[i] = scan.nextInt();    
        }
        
        int count = 0;
        for (int x = 0; x < n; x++) {
            int sum = 0;
            for (int y = x; y < n; y++) {
                sum = arr[y] + sum;
                if (sum < 0) count++;
            }
        }
        
        System.out.print(count);
    }
}