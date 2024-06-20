public class VisitedNode{
	public String previousNode;
	public int totalCost;
	public VisitedNode(String previousNode, int totalCost){
		this.previousNode = previousNode;
		this.totalCost = totalCost;
	}
}