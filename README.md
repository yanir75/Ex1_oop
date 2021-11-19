# Assignment 1 - Object Oriented Programming :elevator:

**Yanir Cohen**  
**Netanel Levine** 

## Sources:

  - https://www.youtube.com/watch?v=siqiJAJWUVg
  - https://github.com/00111000/Elevator-Scheduling-Simulator
  - https://www.researchgate.net/publication/31595225_Estimated_Time_of_Arrival_ETA_Based_Elevator_Group_Control_Algorithm_with_More_Accurate_Estimation



## Offline Algorithm:

According to a research shown in the sources , it can be seen that zoning has proved to have the best average wait time for each people.
As a result we decided that our offline algorithm will be deviding the calls into zones and assigning the calls according to the speed of the elevator.
Since this is an offline we added a tweak which calculates which zone should have the fastest elevator.

---
## UML

   
   <p align="center">
    <img width="800" height="900" src="https://github.com/yanir75/Ex1_oop/blob/main/Smart%20Elevator%20UML.png" "Smart Elevator UML">
   </p>


## How to use:
```
git clone https://github.com/yanir75/Ex1_oop.git & cd Ex1_oop
```
```
pip install -r requirements.txt
``` 
## To insert your own building and files
```
python Ex1_main.py <building_json_file_name> <calls_csv_file_name> <output_file_name>
```
## To use existing files
```
python Ex1_main.py <output_file_name>
```
