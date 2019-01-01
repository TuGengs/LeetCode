package medium;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class Longest_Substring_Without_Repeating_Characters {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		int max = 0;
		String s = new Scanner(System.in).nextLine();
		List<Character> st = new ArrayList<Character>();
		
		st.forEach((x) -> System.out.println(x));
		
		for (int i = 0; i < s.length(); i++) {
			if (!st.contains(s.charAt(i))) {
				st.add(s.charAt(i));
				continue;
			}
			
			max = max > st.size() ? max : st.size();
			
			Iterator<Character> it = st.iterator();
			System.out.println("bf: " + st);
			System.out.println("delet: " + s.charAt(i));
			while (it.hasNext()) {
				Character cr = it.next();
				if (!cr.equals(s.charAt(i))) {
					it.remove();
				} else {
					break;
				}
			}
			it.remove();
			st.add(s.charAt(i));
		}
		System.out.println(Math.max(max, st.size()));
	}
	
}
