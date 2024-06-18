public class State{
	public String name;
	public String previousnode;
	public int totalcost;
	public int totaldist;
	public State(String name, int totalcost, String previousnode, int totaldist){
		this.name = name;
		this.totalcost = totalcost;
		this.previousnode = previousnode;
		this.totaldist = totaldist;
	}

	public int getTotalCost(){
		return this.totalcost;
	}
}