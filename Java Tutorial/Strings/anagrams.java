import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        int sum = 0;
        for (char x='a'; x<='z'; x++) {
            for (int i=0; i<a.length(); i++) {
                if (x == a.charAt(i)) {
                    sum += 1;
                }
                if (x == b.charAt(i)) {
                    sum -= 1;                    
                }
            }
            
            if (sum != 0) {
                return false;
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}