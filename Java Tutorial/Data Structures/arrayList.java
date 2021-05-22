import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int n = scan.nextInt();
        ArrayList<ArrayList<Integer>> lists = new ArrayList<>();
        
        for (int r=0; r<n; r++) {
            int d = scan.nextInt();
            ArrayList<Integer> list = new ArrayList<>();
            for (int c=0; c<d; c++) {
                list.add(scan.nextInt());
            }
            
            lists.add(list);
        }
        
        int q = scan.nextInt();
        for (int i=0; i<q; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            ArrayList<Integer> list = lists.get(x-1);
            if (y <= list.size()) {
                System.out.println(list.get(y-1));     
            }
            else {
                System.out.println("ERROR!");
            }
        }
        
        scan.close();
    }
}