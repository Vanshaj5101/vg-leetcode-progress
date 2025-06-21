class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        pos_spd_arr = []
        for i in range(len(position)):
            pos_spd_arr.append((position[i], speed[i]))

        pos_spd_arr = sorted(pos_spd_arr, key = lambda x:x[0])
        print(pos_spd_arr)
        for i in range(len(pos_spd_arr)-1, -1, -1):
            pos = pos_spd_arr[i][0]
            spd = pos_spd_arr[i][1]
            time = (target - pos)/spd
            if not stk or time > stk[-1]:
                stk.append(time)
                print(stk)
        
        return len(stk)
            