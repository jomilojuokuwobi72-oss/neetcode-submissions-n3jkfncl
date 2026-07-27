class Solution {
    public boolean hasDuplicate(int[] nums) {
        /*
        while iterating, store number in a set
        as you continue iterating, if a number appears again 
        return true. Return false out of the loop 
        */
        Set<Integer> duplicates = new HashSet<>();

        for(int num: nums) {
            if(duplicates.contains(num)) {
                return true; 
            }
            duplicates.add(num);
        }
        return false;
    }
}