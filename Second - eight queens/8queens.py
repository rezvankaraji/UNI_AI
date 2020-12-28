import random


class Board:
    def __init__(self, board_dim):
        self.board_dim = board_dim

    def lineal_threats(self, gene):
        threats = 0
        for dim in range(1, self.board_dim + 1):
            dim_count = gene.count(dim)
            threats += (dim_count * (dim_count - 1)) // 2
        return threats

    def diagonal_threats(self, gene):
        threats = 0
        for index, position in enumerate(gene):
            for prv_index in range(index - 1, -1, -1):
                if abs(position - gene[prv_index]) == abs(index - prv_index):
                    threats += 1
            for nxt_index in range(index + 1, self.board_dim):
                if abs(position - gene[nxt_index]) == abs(index - nxt_index):
                    threats += 1
        return threats // 2

    def queens_genetic_algorithm(self, chance, num_initial_gene):
        self.chance = chance
        self.max_fit = (self.board_dim * (self.board_dim - 1)) // 2
        genes = self.initial_genes(num_initial_gene)
        selected_genes = self.select(genes)
        new_genes = self.cross_over(selected_genes)
        mutated_genes = self.mutation(new_genes)
        dominant_gene, prob = self.dominant(mutated_genes)
        return dominant_gene, prob

    def initial_genes(self, count):
        genes = []
        for counter in range(count):
            random_gene = [
                random.randint(1, self.board_dim) for counter in range(self.board_dim)
            ]
            genes.append(random_gene)
        return genes

    def select(self, genes):
        probs = list(map(self.probability, genes))
        selected_genes = []
        for index in range(len(genes)):
            r = random.uniform(0, 1)
            accumulated_fitness = probs[index]
            for index in range(len(probs)):
                if accumulated_fitness < r:
                    accumulated_fitness += probs[index]
                else:
                    selected_genes.append(genes[index])
                    break
        return selected_genes

    def probability(self, gene):
        threats = self.lineal_threats(gene) + self.diagonal_threats(gene)
        return 1 - threats / self.max_fit

    def cross_over(self, genes):
        new_genes = []
        groups = [2 * counter for counter in range(len(genes) // 2)]
        for index in groups:
            pivot = random.randint(0, self.board_dim - 1)
            first_new_gene = genes[index][0:pivot]
            second_new_gene = genes[index + 1][0:pivot]
            first_new_gene.extend(genes[index + 1][pivot:])
            second_new_gene.extend(genes[index][pivot:])
            crossed_over_genes = [first_new_gene, second_new_gene]
            new_genes.extend(crossed_over_genes)
        return new_genes

    def mutation(self, new_genes):
        mutated_genes = []
        for gene in new_genes:

            prob = random.uniform(0, 1)
            if prob < self.chance:
                index = random.randint(0, self.board_dim - 1)
                value = random.randint(1, self.board_dim)
                gene[index] = value

            mutated_genes.append(gene)
        return mutated_genes

    def dominant(self, mutated_genes):
        probs = list(map(self.probability, mutated_genes))
        max_prob = max(probs)
        max_index = probs.index(max_prob)
        return mutated_genes[max_index], max_prob


######################## main #######################
# set value to parameters
board_dim = 8
chance = 0.3
num_initial_gene = 100

# build an instance of the class
Board = Board(board_dim)

# run the genetic algorithm until the positions of the queens are completely unthreatening
prob = 0
solution = []
counter = 0
while not prob == 1:
    solution, prob = Board.queens_genetic_algorithm(chance, num_initial_gene)
    counter += 1
print("the algorithm ran ", counter, " times")

# visualize the final board
print("the final board:")
board = [["-----" for i in range(board_dim)] for _ in range(board_dim)]
for i in range(board_dim):
    board[solution[i] - 1][i] = "Queen"
for row in board:
    print(row)
