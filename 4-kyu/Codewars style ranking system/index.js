class User{
    
    constructor(){
        this.rank = -8
        this.progress = 0
        this.highestRank = 8;
    }

    rank(){
        return this.rank
    }

    progress(){
        return this.progress
    }

    incProgress(taskRank){
        if (taskRank == 0 || Math.abs(taskRank) > this.highestRank) throw new RangeError("rank input out of range");
        if(this.rank == this.highestRank) return
       
        let diff = 0
        if(taskRank > 0 && this.rank < 0) {
            diff = taskRank - this.rank - 1
        }else if(taskRank === -1 && this.rank === 1) diff = -1 
        else diff = taskRank - this.rank 
        
        if(diff === 0) this.progress += 3
        if(diff === -1 ) this.progress += 1
        if(diff >= 1) this.progress += diff * diff * 10

        if (this.progress >= 100 ) {
           this.rank += Math.floor(this.progress / 100)
           if(this.rank === 0) this.rank++
           this.progress %= 100
        }
        if(this.rank === this.highestRank) this.progress = 0
    }
}

