# Khali list banayi jisme tasks save honge
tasks = []

while True:
    print("\n==== MERA TODO APP ====")
    print("1. Naya Task Add karo")
    print("2. Saare Tasks dekho")
    print("3. Task Complete karo")
    print("4. Task Delete karo")
    print("5. Bahar niklo")

    choice = input("Apna option likho 1-5: ")

    # 1. Add Task
    if choice == "1":
        task = input("Task kya hai? ")
        tasks.append({"task": task, "done": False})
        print("✅ Task add ho gaya!")

    # 2. View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("Abhi koi task nahi hai")
        else:
            print("\n--- Tumhare Tasks ---")
            for i, t in enumerate(tasks, 1):  # 1 se counting start
                status = "✓" if t["done"] else " "
                print(f"{i}. [{status}] {t['task']}")

    # 3. Complete Task
    elif choice == "3":
        num = int(input("Konsa number wala task complete hua? "))
        tasks[num-1]["done"] = True  # -1 isliye kyunki list 0 se start hoti
        print("Shabash! Task complete kar diya 🎉")

    # 4. Delete Task
    elif choice == "4":
        num = int(input("Konsa number wala task delete karna hai? "))
        tasks.pop(num-1)
        print("🗑️ Task delete ho gaya")

    # 5. Exit
    elif choice == "5":
        print("Allah Hafiz!")
        break
    
    else:
        print("Ye option nahi hai. 1 se 5 tak likho")