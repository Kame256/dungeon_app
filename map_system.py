import random

class Floor:

    def __init__(self):
        self.map_range=[random.randint(2,5),random.randint(2,5)]
        self.start=0

    def set_map(self):
        y_range=self.map_range[0]
        x_range=self.map_range[1]
        start=[random.randint(0,y_range),random.randint(0,x_range)]
        goal=[random.randint(0,y_range),random.randint(0,x_range)]
        while 1:
            if start==goal:
                goal=[random.randint(0,y_range),random.randint(0,x_range)]
            else:
                break
        empty_map=[[0 for x in range(x_range+1)] for x in range(y_range+1)]
        empty_map[start[0]][start[1]]=1
        empty_map[goal[0]][goal[1]]=2
        map=[[random.randint(3,5) if x==0 else x for x in y ] for y in empty_map]
        return [map,start]
# イベントの設定
    def make_event(self,map):
        for　y in map:
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

Class Room(Bottu)
