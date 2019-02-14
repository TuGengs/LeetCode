package medium;

import java.util.Scanner;

/**
 * 
 * 1、深搜，会超时
 * 
 * 2、动态规划！
 * 
 * @author tugeng
 *
 */
public class Unique_Paths {
	
//	public static int[][] direct = {{1, 0}, {0, 1}};
//	
//	public static int times = 0;
//
//	public static boolean judge(int m, int n, int x, int y) {
//		if (x < 0 || x > m - 1)
//			return false;
//		if (y < 0 || y > n - 1)
//			return false;
//		return true;
//	}
//	
//	public static void dfs(int x, int y, int m, int n) {
//		
//		if (x == m - 1 && y == n - 1) {
//			times ++;
//			return;
//		}
//		for (int i = 0; i < direct.length; i++) {
//			if (judge(m, n, x + direct[i][0], y + direct[i][1]))
//				dfs(x + direct[i][0], y + direct[i][1], m, n);
//		}
//	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
//
//		dfs(0, 0, m, n);
//		
//		System.out.println(times);
		
        int[][] dp = new int[m][n];        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0)
                    dp[i][j] = 1;
                else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
	    System.out.println(dp[m - 1][n - 1]);
	}
	
}
