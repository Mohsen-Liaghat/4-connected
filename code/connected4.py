class ENV4C : 
    def __init__(self , m = 7 , n = 6 , map = None ) :
        if map != None :
            self.__map = [ i.copy() for i in map ]
        else :
            self.__map = [ [ 0 for _ in range(m) ] for _ in range(n) ]
        self.__m = m
        self.__n = n 
    
    def drop( self , m , agent ) :
        if agent == 0 :
            raise Exception("bad agent")
        for i in range( self.__n ) :
            if self.__map[i][m] == 0 :
                self.__map[i][m] = agent
                break
        else :
            raise Exception( "Full column" )
    
    def __isfirstinrowwining( self , r , c ) :
        a = self.__map[r][c]
        if c > self.__m - 4 or a == 0 :
            return False
        for i in range( 1 , 4 ) :
            if self.__map[r][c + i] != a :
                return False
        return True

    def __isfirstincolumnwining( self , r , c ) :
        a = self.__map[r][c]
        if r > self.__n - 4 or a == 0 :
            return False
        for i in range( 1 , 4 ) :
            if self.__map[r + i][c] != a :
                return False
        return True

    def __isfirstindiagonalwining( self , r , c ) :
        a = self.__map[r][c]
        if a == 0 or c > self.__m - 4  :
            return False
        if r <= self.__n - 4 :
            for i in range( 1 , 4 ) :
                if self.__map[r + i][c + i] != a :
                    break
            else :
                return True
        if r > 2 :
            for i in range( 1 , 4 ) :
                if self.__map[r - i][c + i] != a :
                    break
            else :
                return True
        return False

    def copy( self ) :
        return ENV4C( self.numberofcolumns , self.numberofrows , self.__map )

    @property
    def isfull(self) :
        for i in self.__map :
            if 0 in i :
                return False
        return True

    @property
    def winer( self ) :
        for i in range( self.__n ) :
            for j in range(self.__m) :
                if self.__isfirstinrowwining(i, j) or self.__isfirstincolumnwining(i, j) or self.__isfirstindiagonalwining(i, j) :
                    return self.__map[i][j]
        return 0

    def __str__(self) :
        res = ""
        for i in range( self.__n - 1 , -1 , -1 ) :
            res += str(self.__map[i]) + '\n' 
        return res 

    @property
    def numberofrows( self ) :
        return self.__n 
    
    @property
    def numberofcolumns( self ) :
        return self.__m 

    def u ( self , action ) :
        row = 0
        res = 1
        t = 1
        for i in range( self.__n ) :
            if self.__map[i][action] == 0 :
                row = i
                break
        else :
            raise Exception( "Full column" )
        
        if action != 0 :
            if row != 0 :
                if self.__map [ row - 1 ][ action - 1 ] == 0 :
                    res += 1 
                elif self.__map [ row - 1 ][ action - 1 ] == 1 :
                    t += 1 
            if row != self.numberofrows - 1 :
                if self.__map [ row + 1 ][ action - 1 ] == 0 :
                    res += 1 
                elif self.__map [ row + 1 ][ action - 1 ] == 1 :
                    t += 1
            if self.__map [ row ][ action - 1 ] == 0 :
                res += 1 
            elif self.__map [ row ][ action - 1 ] == 1 :
                t += 1
        if action != self.numberofcolumns - 1 :
            if row != 0 :
                if self.__map [ row - 1 ][ action + 1 ] == 0 :
                    res += 1 
                elif self.__map [ row - 1 ][ action + 1 ] == 1 :
                    t += 1 
            if row != self.numberofrows - 1 :
                if self.__map [ row + 1 ][ action + 1 ] == 0 :
                    res += 1 
                elif self.__map [ row + 1 ][ action + 1 ] == 1 :
                    t += 1
            if self.__map [ row ][ action + 1 ] == 0 :
                res += 1 
            elif self.__map [ row ][ action + 1 ] == 1 :
                t += 1
        if row != 0 :
            if self.__map [ row - 1 ][ action ] == 0 :
                res += 1 
            elif self.__map [ row - 1 ][ action ] == 1 :
                t += 1 
        return t * res