import queue
import time


class agent:
    def __init__(self, address, weights):
        with open(address, "r") as env_file:
            raw_env = env_file.read().split("\n")
            raw_env = raw_env[:-1]
            self.set_env(raw_env)

        self.weights = weights
        self.row_size = 30
        self.col_size = 30

    def set_env(self, raw_env):
        self.env = {}
        for i in range(len(raw_env)):
            row = raw_env[i].split(",")
            for j in range(len(row)):
                coordinate = (i, j)
                if row[j] == "0.0":
                    self.env[coordinate] = "open"
                else:
                    self.env[coordinate] = "blocked"

    def search(self, src, dst, is_UCS=False):
        frontier = queue.PriorityQueue()
        src_priority = self.heuristic(src, dst, is_UCS)
        frontier.put((src_priority, src))  # (priority, cell)
        explored = set()
        parents = {src: None}

        while not frontier.empty():
            current_priority, current_cell = frontier.get()
            if current_cell not in explored:
                explored.add(current_cell)

                if current_cell == dst:
                    return (
                        current_priority,
                        self.obtain_path(src, current_cell, parents),
                    )

                next_cells = self.next_cells(current_cell)

                for cell in next_cells:
                    new_cell_weight, new_cell = cell
                    if new_cell not in explored and self.env[new_cell] == "open":
                        next_priority = (
                            current_priority
                            - self.heuristic(current_cell, dst, is_UCS)
                            + self.heuristic(new_cell, dst, is_UCS)
                            + new_cell_weight
                        )
                        parents[new_cell] = current_cell
                        frontier.put((next_priority, new_cell))

    def next_cells(self, current_cell):
        row, col = current_cell
        next_cells = []
        coordinates = [
            (row - 1, col, self.weights["top"]),
            (row, col - 1, self.weights["left"]),
            (row, col + 1, self.weights["right"]),
            (row + 1, col, self.weights["bottom"]),
        ]
        for coordinate in coordinates:
            next_row = coordinate[0]
            next_col = coordinate[1]
            weight = coordinate[2]
            if (
                next_row >= 0
                and next_col >= 0
                and next_row < self.row_size
                and next_col < self.col_size
            ):
                next_cells.append((weight, (next_row, next_col)))
        return next_cells

    def obtain_path(self, src, dst, parents):
        path = [dst]
        next_cell = dst

        while next_cell != src:
            parent = parents[next_cell]
            path.append(parent)
            next_cell = parent

        path.reverse()
        return path

    # based on Euclidean distance from destination and weights of the moves.
    def heuristic(self, cell, dst, is_UCS):
        if is_UCS:
            return 0

        cell_row, cell_col = cell
        dst_row, dst_col = dst
        row_diff = dst_row - cell_row
        if row_diff < 0:
            row_diff *= self.weights["top"]
        else:
            row_diff *= self.weights["bottom"]
        col_diff = dst_col - cell_col
        if col_diff < 0:
            col_diff *= self.weights["left"]
        else:
            col_diff *= self.weights["right"]
        cell_dst = int((abs(row_diff) ** 2 + abs(col_diff) ** 2) ** 0.5)
        return cell_dst


def run(src, dst, is_UCS=False):
    start = time.time()
    cost, path = agent.search(src, dst, is_UCS)
    stop = time.time()
    print("source is: ", src, "and destination is:", dst)
    if is_UCS:
        print("BY UCS ALGORITHM")
    else:
        print("BY A* ALGORITHM")
    print("time(ms): ", (stop - start) * 100)
    print("cost: ", cost)
    print("path: ", path)
    print()


weights = {"top": 2, "bottom": 3, "left": 1, "right": 1}
agent = agent("/home/rezvan/Downloads/hw1/Environment.txt", weights)

# run((0, 0), (23, 24), is_UCS=True)
# run((17, 1), (17, 29), is_UCS=True)
# run((0, 0), (23, 24))
# run((17, 1), (17, 29))

src = input("enter src coordinates like: 0, 0  :  ").split(", ")
src = (int(src[0]), int(src[1]))
dst = input("enter dst coordinates like: 29, 29  :  ").split(", ")
dst = (int(dst[0]), int(dst[1]))
is_UCS = "yes" == input("do you want UCS algorithm results? yes/no  :  ")
run(src, dst, is_UCS)

