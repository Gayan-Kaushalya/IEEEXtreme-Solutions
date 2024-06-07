# ram_size - number of pages that can be maximally present in the OS
# page_requests - number of memory accesses by the application
# pages - pages currently in memory

def calc_fifo_replacements(ram_size, page_size, pages_requests, pages):
    fifo_list = []
    replaces = 0

    for i in range(pages_requests):
        page = pages[i] // page_size  # page number

        # In  FIFO, if the page is already in the list, we do nothing. 
        # If the list is not full and the page is not in the list, we just append the page to the list. 
        if len(fifo_list) < ram_size and page not in fifo_list:
            fifo_list.append(page)
        # If the list is full, we remove the first element and append the new page to the list.
        elif page not in fifo_list and len(fifo_list) == ram_size:
            fifo_list.pop(0)
            fifo_list.append(page)
            replaces += 1

    return replaces


def calc_lru_replacements(ram_size, page_size, pages_requests, pages):
    lru_list = []
    replaces = 0

    for i in range(pages_requests):
        page = pages[i] // page_size  # page number

        # If the list is not full and the page is not in the list, we just append the page to the list. 
        if len(lru_list) < ram_size and page not in lru_list:
            lru_list.append(page)
        # If the page is already in the list, we have to bring it to the end of the list.
        elif page in lru_list:
            lru_list.remove(page)
            lru_list.append(page)
        # If the list is full and the page is not in the list, we remove the first element and append the new page to the list.
        elif page not in lru_list and len(lru_list) == ram_size:
            lru_list.pop(0)
            lru_list.append(page)
            replaces += 1

    return replaces


for i in range(int(input())):
    ram_size, page_size, pages_requests = map(int, input().split())
    pages = []
    
    for j in range(pages_requests):
        pages.append(int(input()))
     
    '''
    If the number of pages requested is less than or equal to the number of pages that can be maximally present in the OS 
    or all the pages are in the same page, we don't need to calculate the number of page faults because
    we surely know that there will be no page faults.  
    ''' 
    if ram_size >= pages_requests or  max(pages)//page_size == min(pages)//page_size:
        print("no 0 0")
    else:
        fifo_replacements = calc_fifo_replacements(ram_size, page_size, pages_requests, pages)
        lru_replacements = calc_lru_replacements(ram_size, page_size, pages_requests, pages)

        if lru_replacements < fifo_replacements:
            print("yes", fifo_replacements, lru_replacements)
        else:
            print("no", fifo_replacements, lru_replacements)