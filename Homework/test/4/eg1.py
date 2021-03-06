def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)
        
def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

def change2str(std):# turn a list matrix into a string matrix
    matrix_str = ''
    for i in range(len(std)):
        element = str(std[i]).replace('(','').replace(')','').replace(' ','').strip('[').strip(']')
        matrix_str = matrix_str + element + ';'
    matrix_str = '[' + matrix_str.rstrip(';') + ']'
    return matrix_str


class program:
    
    def __init__(self,s):
        self.origin = s
        self.code = self.origin.split('\n')
        del self.code[0]
        del self.code[-1]
        for i in range(len(self.code)):
            self.code[i] = self.code[i].replace(' ','').rstrip(';')
            if 'if' in self.code[i]:
                self.code[i] = self.code[i].replace('if','if ')
            if 'while' in self.code[i]:
                self.code[i] = self.code[i].replace('while','while ')
            if 'return' in self.code[i]:
                self.code[i] = self.code[i].replace('return','return ')
        
        # First, type in all the variables
        position = 0
        for i in range(len(self.code)):
            if self.code[i] == 'main()':
                position = i
        start = ''
        for i in range(position):
            self.code[i] = self.code[i].lstrip('bool')
            start = start + self.code[i] + '\n'
        start = start.rstrip('\n')
        exec(start)

        # Second, divide every part
        div_part = []
        position = 0
        for i in range(len(self.code)):
            if self.code[i] == 'main()':
                position = i + 2
        while position <= len(self.code) - 1:
            if 'while' in self.code[position]:
                i = position
                #element = []
                #element.append([self.code[i]])
                #element.append('while')
                #div_part.append(element)
                while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                    i = i - 1
                position_start = i + 1
                element = []
                element.append(self.code[position_start:position])
                div_part.append(element)
                
                i = position
                element = []
                element.append([self.code[i]])
                element.append('while')
                div_part.append(element)

                i = position + 1
                while 'done' not in self.code[i]:
                    i = i + 1
                position_end = i
                element = []
                element.append(self.code[position + 1:position_end])
                div_part.append(element)
                position = position_end + 1
                
            elif 'if' in self.code[position]:
                i = position
                while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                    i = i - 1
                position_start = i + 1
                element = []
                element.append(self.code[position_start:position + 1])
                element.append('if')
                div_part.append(element)

                i = position
                while 'fi' not in self.code[i]:
                    i = i + 1
                position_end = i
                element = []
                element.append(self.code[position + 1:position_end])
                div_part.append(element)
                position = position_end + 1

            else:
                position = position + 1
                if position == len(self.code) - 1:
                    while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                        i = i - 1
                    position_start = i + 1
                    element = []
                    element.append(self.code[position_start:position])
                    div_part.append(element)
            
        print(div_part)

        # Third, draw CFG
        for i in range(len(div_part)):
            pos = div_part[i][0][0].find(':')
            num = div_part[i][0][0][0:pos]
            div_part[i].append(num)
        print(div_part)
        
        # draw each route in the graph, stored in the list 'connection'
        connection =[]
        for i in range(len(div_part) - 1):
            connection.append([div_part[i][-1],div_part[i+1][-1]])
        for i in range(len(div_part)):
            if 'if' in div_part[i]:
                connection.append([div_part[i][-1],div_part[i+2][-1]])
            elif 'while' in div_part[i]:
                connection.append([div_part[i][-1],div_part[i+2][-1]])
                connection.append([div_part[i+1][-1],div_part[i][-1]])
                pos = 0
                for k in range(len(connection)):
                    if connection[k] == [div_part[i+1][-1],div_part[i+2][-1]]:
                        pos = k
        del connection[pos]
        print(connection)
        
        # change the list into the graph matrix
        graph = [[0 for x in range(len(div_part))] for y in range(len(div_part))]
        num = []
        for i in range(len(div_part)):
            num.append(div_part[i][-1])
        quick_sort(num)
        rank = {}
        for i in range(len(num)):
            rank[num[i]] = i
        for i in range(len(connection)):
            graph[rank[connection[i][0]]][rank[connection[i][1]]] = 1
        self.graph = change2str(graph)

        # Finally, calculate the result
        for 
                        
    def getCFG(self):
        return self.graph

    def evaluate(self):
        pass

s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= !y;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( ( x | y) & (a | z) )
    9:      a=!y;
    10:     y=!z;
        done
    11: return x;
    } 
""" 
p =  program(s)
        
            
