from island import Island
from data_structures.bst import BinarySearchTree
class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = BinarySearchTree()  # Create a Binary Search Tree to store the islands
        self.crew = crew
        
        for island in islands:
            self.ratio = island.marines / island.money
            self.islands[self.ratio] = island  # Use the ratio as the key
        

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        selected_islands = []
        current_crew = self.crew
        for island in self.islands:
            
            # print(island)
            selected_crew = min(island.item.marines, current_crew)
            current_crew -= selected_crew
            selected_islands.append([island.item,selected_crew])
        return selected_islands


    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
     
        results = []

        for current_crew in crew_numbers:
                money = 0
                for island in self.islands:
                    selected_crew = min(island.item.marines, current_crew)
                    current_crew -= selected_crew
                    money += selected_crew / island.item.marines * island.item.money
                results.append(money)
        return results
            

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        node = self.islands.get_tree_node_by_key(island.marines / island.money)
        if node is not None:  
            node = self.islands.__delitem__(island.marines/island.money)
            island.money = new_money
            island.marines = new_marines
            self.islands[island.marines / island.money] = island
            

a = Island("A", 400, 100)
b = Island("B", 300, 150)
c = Island("C", 100, 5)
d = Island("D", 350, 90)
e = Island("E", 300, 100)
# navigator = Mode1Navigator([a,b,c,d,e], 50)
# print(navigator.select_islands())
# selected = navigator.select_islands_from_crew_numbers([0, 200, 500, 300, 40])
# print(selected)

islands = [a,b,c,d,e]
nav = Mode1Navigator(islands, 200)
selected = nav.select_islands()
print(selected)

# self.check_solution(self.islands, 200, selected, 865)

# Update Island A to have only 1 marine, rather than 100.
nav.update_island(islands[0], 400, 1)
# Done for testing \/ so check_solution works.
islands[0].marines = 1
selected_again = nav.select_islands()
# print(str(selected_again) + 'a')
# self.check_solution(self.islands, 200, selected_again, 1158)
