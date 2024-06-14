public class Node{
	private String name;
	private int heuristic;

	public Node(name, heuristic){
		this.name = name;
		this.heuristic = heuristic;
	}

	public String getName(){
		return this.name;
	}

	public float getHeuristic(){
		return this.heuristic;
	}
}