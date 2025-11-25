import time
import json
"""
 Toto je muj ukolníček všechna práva vyhrazena.
 1. nový ukoly
 2. ukoly, probíhající, hotové
 3. DAta ukolu - deadline, priorita, popis, nazev, kategorie, checklist
 4. ukládání
 5. spuštení ukolu
 6. dokončení ukolu
 7. smazání ukolu
 8. úprava ukolu
 9. zobrazení ukolu"""

tasks = []
running = []
completed = []

def load_all_tasks():
    global tasks, running, completed
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")
    try:
        with open("running.json", "r", encoding="utf-8") as f:
            running = json.load(f)
    except FileNotFoundError:
        print("No saved running tasks found. Starting fresh.")
    try:
        with open("completed.json", "r", encoding="utf-8") as f:
            completed = json.load(f)
    except FileNotFoundError:
        print("No saved completed tasks found. Starting fresh.")

def new_task():
    name = input("Název úkolu: ")
    description = input("Popis úkolu: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    priority = input("Priorita (nízká/střední/vysoká):")
    category = input("Kategorie: ")
    checklist = []
    if input("Přidat položky do checklistu? (a/n): ").lower() == 'a':
        while True:
            item = input("Položka checklistu (nebo 'konec' pro ukončení): ")
            if item.lower() == 'konec':
                break
            checklist.append(item)
    task={
        "name": name,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "category": category,
        "checklist": checklist
    }
    tasks.apend(task)



def main():
    print("Ahoj světe!")
    time.sleep(2)
    print("Toto je můj ukolníček v Pythonu.")



if __name__ == "__main__":
    main()