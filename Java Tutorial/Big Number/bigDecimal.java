import java.math.BigDecimal;
import java.util.*;

class Solution{

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
      	sc.close();

        //Write your code here
        Comparator<String> myComparator = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                BigDecimal a1 = new BigDecimal(s1);
                BigDecimal a2 = new BigDecimal(s2);
                
                return a2.compareTo(a1);
            }
        };
        
        Arrays.sort(s, 0, n, myComparator);

        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }

}