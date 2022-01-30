import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

public class main {
	
	public static int n = 5;
	public static Map<Integer, Integer[]> result = new HashMap<Integer, Integer[]>();
	
	public static boolean CheckRow(int[][] board, int x, int y) {
		
		IntStream range = IntStream.range(0, n);
		
		Map<Integer, Boolean> cont = new HashMap<Integer, Boolean>();
		range.parallel().forEach(i->{
			Boolean conti = true;
			if(y!=i) {
				if(board[x][i] == 1) {
					conti = false;
				}
			}
			cont.put(i, conti);
		});
		
		for (Map.Entry<Integer, Boolean> entries : cont.entrySet()) {
			if(entries.getValue() == false) {
				return false;
			}
		}
		return true;
		
		/*
		for(int i = 0; i<n; i++) {
			if(y!=i) {
				if(board[x][i] == 1) {
					return false;
				}
			}
		}
		return true;*/
	}
	
	public static boolean CheckCol(int[][] board, int x, int y) {
		IntStream range = IntStream.range(0, n);
		
		Map<Integer, Boolean> cont = new HashMap<Integer, Boolean>();
		range.parallel().forEach(i->{
			Boolean conti = true;
			if(x!=i) {
				if(board[i][y] == 1) {
					conti = false;
				}
			}
			cont.put(i, conti);
		});
		
		for (Map.Entry<Integer, Boolean> entries : cont.entrySet()) {
			if(entries.getValue() == false) {
				return false;
			}
		}
		return true;
	}
	
	public static boolean CheckF(int[][] board, int x1, int x2, int y1, int y2) {
		if(x1<n && y1<n) {
			if(board[x1][y1] == 1) {
				return false;
			}
		}
		if(x2>=0 && y1<n) {
			if(board[x2][y1] == 1) {
				return false;
			}
		}
		if(x1<n && y2>=0) {
			if(board[x1][y2] == 1) {
				return false;
			}
		}
		if(x2>=0 && y2>=0) {
			if(board[x2][y2] == 1) {
				return false;
			}
		}
		return true;
	}
	
	public static boolean CheckDiag(int[][] board, int x, int y) {
		
		Map<Integer, Boolean> cont = new HashMap<Integer, Boolean>();
		
		IntStream range = IntStream.range(0, n);
				range.parallel().forEach(i->{
					
			
			Boolean con = true;
			//System.out.println("Thread: " + Thread.currentThread().getName() + " " + i);
			int x1 = x + (i+1);
			int x2 = x - (i+1);
			int y1 = y + (i+1);
			int y2 = y - (i+1);
			
			if(!CheckF(board,x1,x2,y1,y2)) {
				con = false;
			}
			
			cont.put(i, con);
		});
		
		for (Map.Entry<Integer, Boolean> entries : cont.entrySet()) {
			if(entries.getValue() == false) {
				return false;
			}
		}
		return true;
	}
	
	
	public static boolean Solve(int[][] board, int col) {
		if (col == n) {
			Integer[] v = new Integer[n];
			for(int i = 0; i<n;i++) {
				for(int j = 0; j<n; j++) {
					if(board[i][j] == 1){
						v[i] = j+1;						
					}
				}
			}
			
			
			int size;
			try {
				size = result.size();
			}
			catch(Exception e) {
				size = 0;
			}
			
			result.put(size,v);
			return true;
		}
		boolean res = false;
		
		
		for(int i = 0; i<n; i++) {
			//System.out.println(board.length  + " " + col);
			boolean c1 = CheckRow(board, i, col);
			boolean c2 = CheckCol(board, i, col);
			boolean c3 = CheckDiag(board, i, col);
			
			if(c1 && c2 && c3) {
				board[i][col] = 1;
				res = Solve(board, col+1) || res;
				board[i][col] = 0;
			}
		}
		
		return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
 
		int[][] board = new int[n][n];
		
		for(int i = 0; i<n; i++) {
			for(int j = 0; j<n; j++) {
				board[i][j] = 0;
			}
		}
		
		Solve(board, 0);
		System.out.println("Result:");
		for (Map.Entry<Integer, Integer[]> entries : result.entrySet()) {
			System.out.print("[");
			Integer[] entryset = entries.getValue();
			for(int i = 0; i < entryset.length; i++) {
					System.out.print(entryset[i]);
					if(i!=entryset.length-1)
						System.out.print(",");
			}
			System.out.print("] ");
		}
		
	}

}
