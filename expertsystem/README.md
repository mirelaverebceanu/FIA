# Laboratory work Nr 1 - Expert System
## Tabel of Content
1. [ Description ](#desc)
2. [ Getting Started](#start)
3. [ How to run](#running)

<a name="desc"></a>
## 1. Description
This is an expert system that has aim to solve a particular lunar problem – detecting tourists. This project is implemented to be able to distinguish between tourists (six types) and the Loonies from Luna-City. It has implemented both methods of reasoning, backward chaning and forward chaining.
The project receives an input file describing a set of rules, initial facts and queries. See in the below section steps how to run it.
<a name="start"></a>
## 2.  Getting Started
### This is a system created using Prolog language, therefore for local running you should:
- have downloaded SWIPL (https://www.swi-prolog.org/download/stable), which offers a comprehensive free Prolog environment, so that you could run it from your CMD.

### Running with Docked file:
Build an image with your application:
```python
FROM swipl

COPY . /

CMD ["swipl", "./shell.pl" ]
```
<a name="running"></a>
## 3. How to run
Once you installed SWIPL (in case of local running not with an Docker Image), open you cmd and route to the directory where is your system implemented.

Type the command highlighted below with yellow:
![alt text](https://github.com/mirelaverebceanu/FIA/blob/main/expertsystem/screenshot/run%20shell.PNG)

Then you should be able to run as followed:
![alt text](https://github.com/mirelaverebceanu/FIA/blob/main/expertsystem/screenshot/forward.PNG)

Available commands and more detailed information you could find in the report posted here: https://drive.google.com/drive/folders/1BS-F-TUKKN366nqshAArbauDA-06NtQ5?usp=sharing
