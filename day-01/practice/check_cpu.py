#aapko kaam karna hai mi user se CPU threshold lo
#Current CPU usage pata karo
#agar cpu usage threshold se zyada hua, email kar do


import psutil #for getting CPU usage imported library psutil
def check_cpu_threshold():
    threshold = int(input("Enter your CPU Threshold: "))

    cpu_usage = psutil.cpu_percent(interval=1) #interval=1 means it will take 1 second to calculate CPU usage
    print(f"Current CPU Usage: {cpu_usage}%") # % - percentage or can write: print("Current CPU %:, cpu_usage))
    if cpu_usage > threshold:
        print("CPU usage Alert sent to Email!")
    else:        
        print("CPU usage is normal.")
check_cpu_threshold()