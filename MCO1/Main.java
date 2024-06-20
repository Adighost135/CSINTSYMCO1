import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;

public class Main{

	public static void main(String[] args){
		HashMap<String, VisitedNode> visitedList = new HashMap<String, VisitedNode>();
		HashMap<String, Node> neighborhoodMap = new HashMap<String, Node>();
		Comparator<State> totalCostComparator = Comparator.comparing(State::getTotalCost);
		PriorityQueue<State> frontierQueue = new PriorityQueue<>(totalCostComparator);
		String goal = "Chicago";
		String start = "Dallas";

		neighborhoodMap.put("Dallas", new Node(1200, 
												new HashMap<String, Integer>(){{
													put("Los Angeles", 1700);
													put("New York", 1500);
													put("Miami", 1200); 
												}}));
		neighborhoodMap.put("Los Angeles", new Node(2400, 
												new HashMap<String, Integer>(){{
													put("Dallas", 1700);
													put("New York", 3000);
												}}));
		neighborhoodMap.put("New York", new Node(800, 
												new HashMap<String, Integer>(){{
													put("Dallas", 1500);
													put("Los Angeles", 3000);
													put("Miami", 1000);
													put("Boston", 250);
													put("Chicago", 800);
												}}));
		neighborhoodMap.put("Miami", new Node(2000, 
												new HashMap<String, Integer>(){{
													put("Dallas", 1200);
													put("New York", 1000);
												}}));
		neighborhoodMap.put("San Francisco", new Node(2200, 
												new HashMap<String, Integer>(){{
													put("Los Angeles", 500);
													put("Chicago", 2200);
												}}));
		neighborhoodMap.put("Boston", new Node(900, 
												new HashMap<String, Integer>(){{
													put("New York", 250);
												}}));
		neighborhoodMap.put("Chicago", new Node(0, 
												new HashMap<String, Integer>(){{
													put("New York", 800);
													put("San Francisco", 2200);
												}}));


		frontierQueue.add(new State(start, neighborhoodMap.get(start).heuristic, null, 0));
		while(!frontierQueue.isEmpty()){
			State current = frontierQueue.poll();
			System.out.println("\n===== Visiting: " + current.name + " with total cost " + current.totalcost + "=====");
			visitedList.put(current.name, new VisitedNode(current.previousnode, current.totalcost));
			if(current.name == goal){
				LinkedList<String> path = new LinkedList<>();
				String pathCurrent = goal;
				while(pathCurrent != null){
					path.addFirst(pathCurrent);
					pathCurrent = visitedList.get(pathCurrent).previousNode;
				}
				StringBuffer stringBuffer = new StringBuffer();

				for(String node: path){
					stringBuffer.append(" -> ").append(node);
				}

				System.out.println("Found the goal, reconstructing path: ");
				System.out.println(stringBuffer);
				break;
			}

			neighborhoodMap.get(current.name).neighbors.forEach((neighbor, distance)->{
				System.out.println("\n");
				if(current.previousnode == neighbor){
					System.out.println(neighbor + " is the previous node, skipping...");
					return;
				}

				int newTotalDist = current.totaldist + distance;
				int newTotalCost = newTotalDist + neighborhoodMap.get(neighbor).heuristic;

				System.out.println(neighbor + ":");
				System.out.println("Heuristic: " + neighborhoodMap.get(neighbor).heuristic);
				System.out.println("Distance from " + current.name + ": " + distance);
				System.out.println("New Total Dist: " + newTotalDist);
				System.out.println("New Total Cost: " + newTotalCost);

				if(!visitedList.containsKey(neighbor) || newTotalCost < visitedList.get(neighbor).totalCost){
					if(visitedList.containsKey(neighbor) && newTotalCost < visitedList.get(neighbor).totalCost){
						visitedList.remove(neighbor);
						System.out.println("Found lower cost, replacing known one in Visited List");
					}
					frontierQueue.add(new State(neighbor, newTotalCost, current.name, newTotalDist));
				}
				else{
					System.out.println(neighbor + " is already existing in the visited list with lower cost " + visitedList.get(neighbor).totalCost);
				}
			});
		}
	}
}