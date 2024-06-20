import java.util.HashMap;

public class Node{
	public int heuristic;
	public HashMap<String, Integer> neighbors;
	public Node(int heuristic, HashMap<String, Integer> neighbors){
		this.heuristic = heuristic;
		this.neighbors = neighbors;
	}
}