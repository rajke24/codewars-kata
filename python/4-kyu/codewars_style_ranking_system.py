class User:

    def __init__(self):
        self.rank = -8
        self.max_rank = 8
        self.progress = 0


    def inc_progress(self, task_rank):
        assert(task_rank >= -8 and task_rank <= 8 and task_rank != 0)
        
        if self.rank == self.max_rank:
            return
        else:
            if self.rank == task_rank:
                self.progress += 3
            
            diff = task_rank - self.rank
            if task_rank > 0 and self.rank < 0:
                diff -= 1
            if task_rank == -1 and self.rank == 1:
                diff += 1
            if diff > 0:
                self.progress += 10 * diff ** 2
            elif diff == -1:
                self.progress += 1 

            while self.progress >= 100:
                if self.rank == -1:
                    self.rank += 2
                else:
                    self.rank += 1
                
                if self.rank == 8:
                    self.progress = 0
                    break

                self.progress -= 100

                
                
            