#complexity-O(N)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result=0
        boxes=0
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        for j in boxTypes:
            if(boxes<truckSize):
                if(truckSize-boxes>=j[0]):
                    result+=j[0]*j[1]
                    boxes+=j[0]
                else:
                    result+=j[1]*(truckSize-boxes)
                    boxes+=j[0]
        return result
