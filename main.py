from reports import *

                             
def main():
    print('Conquer Club: Extra Analytics')
    print('Enter a username for their elimination report,\n'+
          'or enter "Shens" for the whole Shenannigans group:')

    u = input();
    
    while u != 'quit':

        if u=="Shens":
            shensReport()
        else:
            killsReport(u)

        print('-----------------')
        u = input('Enter another username, or type "quit" to quit: ')

if __name__ == "__main__":
    main()

    
    






    
