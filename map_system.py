import random

class Floor:

    def __init__(self):
        self.floor_range=[random.randint(2,5),random.randint(2,5)]

        self.start=self.set_floor()[1]
        self.room_list=self.set_floor()[0]

    def set_floor(self):
        y_range=self.floor_range[0]
        x_range=self.floor_range[1]
        start=[random.randint(0,y_range),random.randint(0,x_range)]
        goal=[random.randint(0,y_range),random.randint(0,x_range)]
        while 1:
            if start==goal:
                goal=[random.randint(0,y_range),random.randint(0,x_range)]
            else:
                break
        empty_floor=[[0 for x in range(x_range+1)] for x in range(y_range+1)]
        empty_floor[start[0]][start[1]]=1
        empty_floor[goal[0]][goal[1]]=2
        floor=[[random.randint(3,5) if x==0 else x for x in y ] for y in empty_floor]
        return [floor,start]
# イベントの設定
    def make_event(self,floor):
        for y in floor:
            for x in y:
                if x==4:
                    #敵を作成
                    return 1
                # アイテムを作成
                elif x==5:
                    return 1
                # イベントを作成
                elif x==6:
                    return 1
