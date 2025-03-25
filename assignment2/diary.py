# Task 1
import traceback

try:
    with open ('assignment2/diary.txt', "a") as file:
        input_line = ' '
        prompt = "What happened today?"
        
        while True:
            input_line = input(prompt)
            prompt = "what else?"
           
            if input_line.lower() == 'done for now':
                break
        
            file.write(input_line + '\n')
        

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")