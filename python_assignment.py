#python program
class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id}\t{self.name}\t{self.start_time}\t{self.priority}"

def sort_and_print(processes, sort_key):
    if sort_key == 1:
        processes.sort(key=lambda x: x.p_id)
    elif sort_key == 2:
        processes.sort(key=lambda x: x.start_time)
    elif sort_key == 3:
        processes.sort(key=lambda x: x.priority)
    else:
        print("Invalid sort option.")
        return
    
    print("P_ID\tName\tStart Time (ms)\tPriority")
    for process in processes:
        print(process)

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]
    
    while True:
        print("\nMenu:")
        print("1. Sort by Process ID (P_ID) ")
        print("2. Sort by Start Time (ms) ")
        print("3. Sort by Priority ")
        print("4. Quit ")
        
        choice = int(input("Enter your choice :"))
        
        if choice == 4:
            break
        
        sort_and_print(processes.copy(), choice)

if __name__ == "__main__":
    main()
