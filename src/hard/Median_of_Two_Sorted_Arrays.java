package hard;

public class Median_of_Two_Sorted_Arrays {
	
	static int findKthHelper(int[] A, int aStart, int[] B, int bStart, int k){
        if(aStart >= A.length){
            return B[bStart + k - 1];
        }
        if(bStart >= B.length){
            return A[aStart + k - 1];
        }
        if(k == 1){
            return Math.min(A[aStart], B[bStart]);
        }
        int aMid = aStart + k/2 - 1;
        int bMid = bStart + k/2 - 1;
        int aVal = aMid >= A.length ? Integer.MAX_VALUE : A[aMid];
        int bVal = bMid >= B.length ? Integer.MAX_VALUE : B[bMid];
        if(aVal <= bVal){
            return findKthHelper(A, aMid + 1, B, bStart, k - k/2);
        }else{
            return findKthHelper(A, aStart, B, bMid + 1, k - k/2);
        }
    }

	public static void main(String[] args) {
		
		int[] nums1 = {1, 2};
		int[] nums2 = {3, 4};
		
        int m = nums1.length;
        int n = nums2.length;
        int len = m + n;
        
        if(len % 2 == 0){
            double left =  (double)findKthHelper(nums1, 0, nums2, 0, len/2);
            double right =  (double)findKthHelper(nums1, 0, nums2, 0, len/2 + 1);
            System.out.println((left + right)/2);
//            return (double)(left + right)/2;
        }else{
//            return findKthHelper(nums1, 0, nums2, 0, len/2 + 1);
        	System.out.println(findKthHelper(nums1, 0, nums2, 0, len/2 + 1));
        }
		
	}
	
	
}
