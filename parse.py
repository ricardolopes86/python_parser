import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
from datetime import datetime

def read_from_file():
    print 'Provide name of the file:'
    name_arquivo = raw_input()
    return name_arquivo

def write_to_file():
    print 'Provide final name of the file generated:'
    final_arquivo = raw_input()
    return final_arquivo

def cpu():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    #cpu
    usr_level = []
    sys_level = []
    idle = []
    wa = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            usr_level.append(valores[12])
            sys_level.append(valores[13])
            idle.append(valores[14])
            wa.append(valores[15])

            Data.append(valores[17]+' '+valores[18])

    #define the traces
    usr_level_trace = Scatter(
        x = Data,
        y = usr_level,
        name = 'CPU User Level',
        line = dict(
            color = ('rgb(255, 250, 0)'),
            width = 1)
    )

    sys_level_trace = Scatter(
        x = Data,
        y = sys_level,
        name = 'CPU Sys Level',
        line = dict(
            color = ('rgb(102, 0, 88)'),
            width = 1)
    )

    idle_trace = Scatter(
        x = Data,
        y = idle,
        name = 'CPU Idle',
        line = dict(
            color = ('rgb(0, 102, 11)'),
            width = 1)
    )

    wa_trace = Scatter(
        x = Data,
        y = wa,
        name = 'CPU Waiting I/O',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )


    # Plot and embed in ipython notebook!
    layout = dict(title = 'CPU Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [usr_level_trace, sys_level_trace, idle_trace, wa_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_cpu')

def memory():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    #memory
    swap_memory = []
    free_memory = []
    buffered_memory = []
    cached_memory = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            swap_memory.append(valores[2])
            free_memory.append(valores[3])
            buffered_memory.append(valores[4])
            cached_memory.append(valores[5])
            
            Data.append(valores[17]+' '+valores[18])


    swap_memory_trace = Scatter(
        x = Data,
        y = swap_memory,
        name = 'Swapped Memory',
        line = dict(
            color = ('rgb(255, 144, 0)'),
            width = 1)
    )

    free_memory_trace = Scatter(
        x = Data,
        y = free_memory,
        name = 'Free Memory',
        line = dict(
            color = ('rgb(130, 76, 0)'),
            width = 1)
    )

    buffered_memory_trace = Scatter(
        x = Data,
        y = buffered_memory,
        name = 'Buffered Memory',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    cached_memory_trace = Scatter(
        x = Data,
        y = cached_memory,
        name = 'Cached Memory',
        line = dict(
            color = ('rgb(153, 0, 0)'),
            width = 1)
    )

    # Plot and embed in ipython notebook!
    layout = dict(title = 'Memory Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [swap_memory_trace, free_memory_trace, cached_memory_trace, buffered_memory_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_memory')

def swap():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    #swap
    swap_in = []
    swap_out = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            swap_in.append(valores[6])
            swap_out.append(valores[7])
            
            Data.append(valores[17]+' '+valores[18])

    swap_in_trace = Scatter(
        x = Data,
        y = swap_in,
        name = 'Swap In',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    swap_out_trace = Scatter(
        x = Data,
        y = swap_out,
        name = 'Swap Out',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )


    # Plot and embed in ipython notebook!
    layout = dict(title = 'Swap Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [swap_in_trace, swap_out_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_swap')    

def blocks():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    #block I/O
    bi = []
    bo = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            bi.append(valores[8])
            bo.append(valores[9])

            Data.append(valores[17]+' '+valores[18])   

    bi_trace = Scatter(
        x = Data,
        y = bi,
        name = 'Block In',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    bo_trace = Scatter(
        x = Data,
        y = bo,
        name = 'Block Out',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )

    # Plot and embed in ipython notebook!
    layout = dict(title = 'Blocks Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [bi_trace, bo_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_blocks')  

def process():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()
    
    #processos lists
    r_queue = []
    b_interrupt = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:
            r_queue.append(valores[0])
            b_interrupt.append(valores[1])
            Data.append(valores[17]+' '+valores[18])

    r_queue_trace = Scatter(
        x = Data,
        y = r_queue,
        name = 'Run Queue',
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 1)
    )

    b_interrupt_trace = Scatter(
        x = Data,
        y = b_interrupt,
        name = 'Process Interruptions',
        line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 1)
    )
    # Plot and embed in ipython notebook!
    layout = dict(title = 'Processes Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [r_queue_trace, b_interrupt_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_process')

def system():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    #system
    cs = []
    interruptions = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            interruptions.append(valores[11])
            cs.append(valores[10])

            Data.append(valores[17]+' '+valores[18])

    cs_trace = Scatter(
        x = Data,
        y = cs,
        name = 'Context Switches/s',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    interruptions_trace = Scatter(
        x = Data,
        y = interruptions,
        name = 'Number of Interruptions/s',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )

    # Plot and embed in ipython notebook!
    layout = dict(title = 'System Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [cs_trace, interruptions_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_system')

def all_vmstat_stats():
    #ler aquivo
    name_arquivo = read_from_file()
    final_arquivo = write_to_file()

    usr_level = []
    sys_level = []
    idle= []
    wa= []
    swap_memory= []
    free_memory= []
    buffered_memory= []
    cached_memory= []
    swap_in= []
    swap_out= []
    bi = []
    bo = []
    interruptions= []
    cs= []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:

            usr_level.append(valores[12])
            sys_level.append(valores[13])
            idle.append(valores[14])
            wa.append(valores[15])

            swap_memory.append(valores[2])
            free_memory.append(valores[3])
            buffered_memory.append(valores[4])
            cached_memory.append(valores[5])

            swap_in.append(valores[6])
            swap_out.append(valores[7])

            bi.append(valores[8])
            bo.append(valores[9])

            interruptions.append(valores[11])
            cs.append(valores[10])

            Data.append(valores[17]+' '+valores[18])

    usr_level_trace = Scatter(
        x = Data,
        y = usr_level,
        name = 'CPU User Level',
        line = dict(
            color = ('rgb(255, 250, 0)'),
            width = 1)
    )

    sys_level_trace = Scatter(
        x = Data,
        y = sys_level,
        name = 'CPU Sys Level',
        line = dict(
            color = ('rgb(102, 0, 88)'),
            width = 1)
    )

    idle_trace = Scatter(
        x = Data,
        y = idle,
        name = 'CPU Idle',
        line = dict(
            color = ('rgb(0, 102, 11)'),
            width = 1)
    )

    wa_trace = Scatter(
        x = Data,
        y = wa,
        name = 'CPU Waiting I/O',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    swap_memory_trace = Scatter(
        x = Data,
        y = swap_memory,
        name = 'Swapped Memory',
        line = dict(
            color = ('rgb(255, 144, 0)'),
            width = 1)
    )

    free_memory_trace = Scatter(
        x = Data,
        y = free_memory,
        name = 'Free Memory',
        line = dict(
            color = ('rgb(130, 76, 0)'),
            width = 1)
    )

    buffered_memory_trace = Scatter(
        x = Data,
        y = buffered_memory,
        name = 'Buffered Memory',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    cached_memory_trace = Scatter(
        x = Data,
        y = cached_memory,
        name = 'Cached Memory',
        line = dict(
            color = ('rgb(153, 0, 0)'),
            width = 1)
    )

    swap_in_trace = Scatter(
        x = Data,
        y = swap_in,
        name = 'Swap In',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    swap_out_trace = Scatter(
        x = Data,
        y = swap_out,
        name = 'Swap Out',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )
    bi_trace = Scatter(
        x = Data,
        y = bi,
        name = 'Block In',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    bo_trace = Scatter(
        x = Data,
        y = bo,
        name = 'Block Out',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )
    r_queue_trace = Scatter(
        x = Data,
        y = r_queue,
        name = 'Run Queue',
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 1)
    )

    b_interrupt_trace = Scatter(
        x = Data,
        y = b_interrupt,
        name = 'Process Interruptions',
        line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 1)
    )
    cs_trace = Scatter(
        x = Data,
        y = cs,
        name = 'Context Switches/s',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )

    interruptions_trace = Scatter(
        x = Data,
        y = interruptions,
        name = 'Number of Interruptions/s',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )


    # Plot and embed in ipython notebook!
    layout = dict(title = 'vmstat Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [r_queue_trace, b_interrupt_trace, cs_trace, interruptions_trace, swap_memory_trace, free_memory_trace, cached_memory_trace, buffered_memory_trace, usr_level_trace, sys_level_trace, idle_trace, wa_trace, swap_in_trace, swap_out_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=final_arquivo+'_all')

def vmstat_menu():

    menu_vmstat = {}
    menu_vmstat['1']="CPU Informatoin." 
    menu_vmstat['2']="Memory Information."
    menu_vmstat['3']="SWAP Information."
    menu_vmstat['4']="Processes Information."
    menu_vmstat['5']="System Information."
    menu_vmstat['6']="Blocks."
    menu_vmstat['7']="Exit"



    while True:
        options=menu_vmstat.keys()
        options.sort()
        for entry in options: 
            print entry, menu_vmstat[entry]

        selection=raw_input("Please Select:") 
        if selection =='1': 
            cpu()
        elif selection == '2': 
            memory()
        elif selection == '3':
            swap()
        elif selection == '4': 
            process()
        elif selection == '5': 
            system()
        elif selection == '6': 
            blocks()
        elif selection == '7':
            break
        else: 
            print "Unknown Option Selected!" 

def parse_mpstat():
    #ler aquivo
    name_arquivo = read_from_file()
    
    #processos lists
    usr = []
    nice = []
    sys = []
    iowait = []
    irq = []
    soft = []
    steal = []
    guest = []
    idle = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:
            usr.append(valores[3])
            nice.append(valores[4])
            sys.append(valores[5])
            iowait.append(valores[6])
            irq.append(valores[7])
            soft.append(valores[8])
            steal.append(valores[9])
            guest.append(valores[10])
            idle.append(valores[11])
            Data.append(valores[0]+' '+valores[1])

    usr_trace = Scatter(
        x = Data,
        y = usr,
        name = 'User',
        line = dict(
            color = ('rgb(0, 21, 255)'),
            width = 1)
    )

    nice_trace = Scatter(
        x = Data,
        y = nice,
        name = 'Nice',
        line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 1)
    )
    sys_trace = Scatter(
        x = Data,
        y = sys,
        name = 'Sys',
        line = dict(
            color = ('rgb(255, 255, 0)'),
            width = 1)
    )
    iowait_trace = Scatter(
        x = Data,
        y = iowait,
        name = 'Waint I/O',
        line = dict(
            color = ('rgb(255, 0, 0)'),
            width = 1)
    )
    irq_trace = Scatter(
        x = Data,
        y = irq,
        name = 'IRQ',
        line = dict(
            color = ('rgb(32, 12, 24)'),
            width = 1)
    )
    soft_trace = Scatter(
        x = Data,
        y = soft,
        name = 'Soft',
        line = dict(
            color = ('rgb(90, 123, 234)'),
            width = 1)
    )

    steal_trace = Scatter(
        x = Data,
        y = steal,
        name = 'Steal',
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 1)
    )

    guest_trace = Scatter(
        x = Data,
        y = guest,
        name = 'Guest',
        line = dict(
            color = ('rgb(255, 174, 0)'),
            width = 1)
    )

    idle_trace = Scatter(
        x = Data,
        y = idle,
        name = 'Idle',
        line = dict(
            color = ('rgb(0, 222, 0)'),
            width = 1)
    )

    # Plot and embed in ipython notebook!
    layout = dict(title = 'CPU Stats Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [usr_trace, sys_trace, nice_trace, iowait_trace, irq_trace, soft_trace, steal_trace, guest_trace, idle_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=name_arquivo+'_mpstat')
    
def parse_sar():
    #ler aquivo
    name_arquivo = read_from_file()
    
    #processos lists
    run_queue = []
    list_size = []
    loadagv_1 = []
    loadagv_5 = []
    loadagv_15 = []
    Data = []

    #read the file which is the dataset
    arquivo = open(name_arquivo,'r')

    #parse the file into small variables
    for i in arquivo:
        valores = i.split()
        for n in valores:
            run_queue.append(valores[2])
            list_size.append(valores[3])
            loadagv_1.append(valores[4])
            loadagv_5.append(valores[5])
            loadagv_15.append(valores[6])
            Data.append(valores[0]+' '+valores[1])

    run_queue_trace = Scatter(
        x = Data,
        y = run_queue,
        name = 'Run Queue',
        line = dict(
            color = ('rgb(0, 0, 0)'),
            width = 1)
    )

    #not included in the graph
    list_size_trace = go.Bar(
        x = Data,
        y = list_size,
        name = 'Task List size',
        marker = dict(
            color = ('rgb(150, 255, 167)'),
            line = dict(
                color = ('rgb(150, 255, 167)'),
                width = 1
            )
        )
    )
    loadagv_1_trace = Scatter(
        x = Data,
        y = loadagv_1,
        name = 'CPU Load last 1min',
        line = dict(
            color = ('rgb(200, 30, 50)'),
            width = 1)
    )
    loadagv_5_trace = Scatter(
        x = Data,
        y = loadagv_5,
        name = 'CPU Load last 5min',
        line = dict(
            color = ('rgb(220, 30, 50)'),
            width = 1)
    )
    loadagv_15_trace = Scatter(
        x = Data,
        y = loadagv_15,
        name = 'CPU Load last 15min',
        line = dict(
            color = ('rgb(230, 30, 50)'),
            width = 1)
    )
    # Plot and embed in ipython notebook!
    layout = dict(title = 'Processes Data',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Values'),
              )
    data = [run_queue_trace, loadagv_1_trace, loadagv_5_trace, loadagv_15_trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename=name_arquivo+'_sar')

def parse_pidstat():
    print "Not implemented yet!"

def parse_iostat():
    print "Working on it"

def clear_file_menu():
    clear_file = {}
    clear_file['1'] = "Clear mpstat file"
    clear_file['2'] = "Clear vmstat file"
    clear_file['3'] = "Clear iostat file"
    clear_file['4'] = "Clear gc file"
    clear_file['5'] = "Clear sar file"
    clear_file['6'] = "Clear pidstat file"
    clear_file['7'] = "Go back"

    while True:
        options = clear_file.keys()
        options.sort()
        for entry in options:
            print entry, clear_file[entry]

        selected_option = raw_input("Please select an option:")
        if selected_option == '1':
            clear_file_all('mpstat')
        elif selected_option == '2':
            clear_file_all('vmstat')
        elif selected_option == '3':
            clear_file_all('iostat')
        elif selected_option == '4':
            clear_file_all('gc')
        elif selected_option == '5':
            clear_file_all('sar')
        elif selected_option == '6':
            clear_file_all('pidstat')
        elif selected_option == '7':
            break
        else:
            print "Wrong selection, please, try again"

def clear_file_all(flag_option):
    
    if flag_option == 'vmstat':
        words_remove = ['procs', 'r']
    elif flag_option == 'mpstat':
        words_remove = ['Linux', 'CPU']
    elif flag_option == 'iostat':
        clear_file_iostat()
        break
    elif flag_option == 'pidstat':
        words_remove = ['procs', 'r']
    elif flag_option == 'gc':
        words_remove = ['S0', 'S1']
    elif flag_option == 'sar':
        words_remove = ['Linux', 'runq-sz']
    else:
        print "Wrong option"
    
    name_arquivo = raw_input('Provide name of the file:')
    final_file = raw_input("Final file name:")

    with open(name_arquivo) as oldfile, open(final_file, 'w') as newfile:
        for line in oldfile:
            if not any(word_chaging in line for word_chaging in words_remove):
                newfile.write(line)

def clear_file_iostat():
    name_arquivo = raw_input('Provide name of the file:')
    final_file = raw_input("Final file name:")

    words_remove = ['sda', 'sdb' ,'dm-0','dm-1','dm-2','dm-3','dm-4','dm-5','dm-6','dm-7','dm-8','dm-9','dm-10','dm-11','dm-12','dm-13']

    with open(name_arquivo) as oldfile, open(final_file, 'w') as newfile:
        for line in oldfile:
            if any(word_chaging in line for word_chaging in words_remove):
                newfile.write(line)
    

menu_main = {}
menu_main['1'] = "Parse vmstat file"
menu_main['2'] = "Parse mpstat file"
menu_main['3'] = "Parse iostat file"
menu_main['4'] = "Parse pidstat file"
menu_main['5'] = "Parse sar file"
menu_main['6'] = "Parse GC file"
menu_main['8'] = "Clear File"
menu_main['9'] = "Exit"

while True:
        options=menu_main.keys()
        options.sort()
        for entry in options: 
            print entry, menu_main[entry]

        selection=raw_input("Please Select:") 
        if selection =='1': 
            vmstat_menu()
        elif selection == '2': 
            parse_mpstat()
        elif selection == '3':
            parse_iostat()
        elif selection == '4': 
            parse_pidstat()
        elif selection == '5': 
            parse_sar()
        elif selection == '6': 
            gc_menu()
        elif selection == '8':
            clear_file_menu()
        elif selection == '9':
            break
        else: 
            print "Unknown Option Selected!" 

