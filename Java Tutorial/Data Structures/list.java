import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        LinkedList<Integer> list = new LinkedList<>();
        
        for (int i = 0; i < n; i++) {
            int val = scan.nextInt();
            list.add(val);
        }
        
        int q = scan.nextInt();
        for (int i = 0; i < q; i++) {
            String action = scan.next();
            if (action.equals("Insert")) {
                int index = scan.nextInt();
                int newVal = scan.nextInt();
                list.add(index, newVal); 
            }    
            else {
                int index = scan.nextInt();
                list.remove(index);
            }
        }
        
        scan.close();
        
        for (Integer i : list) {
            System.out.print(i + " ");
        }
    }
}