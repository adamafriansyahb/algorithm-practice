public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        for (int i=0; i+k<=s.length(); i++) {
            String currentSubStr = s.substring(i, i+k);
            if (currentSubStr.compareTo(smallest) < 0) smallest = currentSubStr;
            if (currentSubStr.compareTo(largest) > 0) largest = currentSubStr;
        }
        
        return smallest + "\n" + largest;
    }