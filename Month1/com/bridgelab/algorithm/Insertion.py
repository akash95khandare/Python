import com.bridgelab.util.Utility as u

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
stringArr = ["akash", "shubham", "rohan", "sham", "nikhil", "rahul", "arvind"]

start = u.start_watch()
print(u.insertion_sort(arr))
print("Elapse time : ", u.stop_watch(start))

start = u.start_watch()
print(u.insertion_sort(list(stringArr)))
print("Elapse time : ", u.stop_watch(start))