
def heapify(arr, n, i, changes):
    smallest = i 
    l_child = 2 * i + 1   # kreisais bērns
    r_child = 2 * i + 2   # labais bērns
    
    if l_child < n and arr[l_child] < arr[smallest]:
        smallest = l_child
 
    if r_child < n and arr[r_child] < arr[smallest]:
        smallest = r_child
 
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])
        changes.append(i)          # pievieno saraktā maināmo elementu indeksus
        changes.append(smallest)   # pievieno saraktā maināmo elementu indeksus
        heapify(arr, n, smallest, changes)
        
 
def heapSort(arr, n, changes):
     
    for i in range(int(n / 2) -1, -1, -1):
        heapify(arr, n, i, changes)


def printAnswer(changes):
    print()
    print("Output:")
    print()
    changeCount = int(len(changes)/2)
    if (changeCount == 0):
       print("The input array is already a heap, because it is sorted in increasing order.") 
    else:  
       print(int(len(changes)/2)) # izdrukā maiņu skaitu
       print()
       #print(*changes)  # izdrukā sarakstu bez kvadrātiekavām un atstarpi starp elementiem                  #print(changes)  # izdrukā sarakstu ar kvadrātiekavām un elementus atdala ar komatu           
       changeString="".join(map(str,changes)) # sarakstu pārveido stringā
       for i in range(0,len(changes),2): # ciklā drukā maiņu pārīšus
         print(changeString[i:i+2])
         print()
 
if __name__ == '__main__':
        
  changes = []   # saraksts, kas satur veikto maiņu indeksus

  #apstradePabeigta = False
  #while not(apstradePabeigta):
  IevadesVeids = input("Izvēlieties veidu, kā ievadīt datus - no ekrāna vai faila (I/F): ")
  if "I" in IevadesVeids:
        n = int(input("Ievadiet masīva elementu skaitu: "))
        arr = list(map(int, input().split()))
        heapSort(arr, n, changes)
        printAnswer(changes)
        #apstradePabeigta = True
  elif "F" in IevadesVeids: 
        failaNos = input("Ievadiet faila nosaukumu: ")
        failaNos = "tests/" + failaNos
        if "a" not in failaNos:
         with open(failaNos, 'r') as f:
         #with open('dati.txt', 'r') as f:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
            heapSort(arr, n, changes)
            printAnswer(changes)
            #apstradePabeigta = True
  else:
      print("Šādu simbolu ievadīt nav paredzēts")
      print("Ievadiet kādu no (I/F)")
      #apstradePabeigta = False
         
    