from connected4 import ENV4C as ENV 

neginf = -100
inf = 100

def min_max ( env , order = "MAX" ) :
    winer = env.winer 
    if winer == 1 :
        return ( "" , 1 )
    if winer == 2 : 
        return ( "" , -1)
    if env.isfull :
        return ( "" , 0 )

    tmp = []
    if order == "MAX" :
        for i in range( env.numberofcolumns ) :
            try :
                newenv = env.copy()
                newenv.drop( i , 1 )
                prize = min_max( newenv , "MIN" )
                tmp.append( (str(i) + prize[0] , prize[1]) ) 
            except Exception as er :
                if str(er) != "Full column" :
                    raise er 
        tmp1 = [ i[1] for i in tmp ]
        prize = max( tmp1 )
        for i in tmp :
            if i[1] == prize :
                return i 
    elif order == "MIN" :
        for i in range( env.numberofcolumns ) :
            try :
                newenv = env.copy()
                newenv.drop( i , 2 )
                prize = min_max( newenv , "MAX" )
                tmp.append( (str(i) + prize[0] , prize[1]) ) 
            except Exception as er :
                if str(er) != "Full column" :
                    raise er 
        tmp1 = [ i[1] for i in tmp ]
        prize = min( tmp1 )
        for i in tmp :
            if i[1] == prize :
                return i
    else : 
        raise Exception("Bad Order.\n there is only two orders : \n \t MAX \n \t MIN")

###################################################################################################################

#alpha beta search
def abs ( env ) :
    return max_value( env , neginf , inf ) 

def max_value ( env , alpha , beta ) :
    winer = env.winer 
    if winer == 1 :
        return ( "" , 1 )
    if winer == 2 : 
        return ( "" , -1)
    if env.isfull :
        return ( "" , 0 )

    v = ("" , neginf)
    for i in range( env.numberofcolumns ) :
        try :
            newenv = env.copy()
            newenv.drop( i , 1 )
            tmp = min_value ( newenv , alpha , beta )
            tmp = ( str(i) + tmp[0] , tmp[1] )
            if tmp[1] > v[1] :
                v = tmp 
            if tmp[1] >= beta :
                return tmp 
            alpha = max( alpha , tmp[1] )
        except Exception as er : 
            if str(er) != "Full column" :
                raise er 
    return v

def min_value ( env , alpha , beta ) :
    winer = env.winer 
    if winer == 1 :
        return ( "" , 1 )
    if winer == 2 : 
        return ( "" , -1)
    if env.isfull :
        return ( "" , 0 )

    v = ("" , inf)
    for i in range( env.numberofcolumns ) :
        try :
            newenv = env.copy()
            newenv.drop( i , 2 )
            tmp = max_value ( newenv , alpha , beta )
            tmp = ( str(i) + tmp[0] , tmp[1] )
            if tmp[1] < v[1] :
                v = tmp 
            if tmp[1] <= alpha :
                return tmp 
            beta = min( beta , tmp[1] )
        except Exception as er : 
            if str(er) != "Full column" :
                raise er 
    return v

#####################################################################

def utility ( env , max_move , turn = None , move_counter = 0 ) :
    u = 0 
    winer = env.winer 
    if winer == 1 :
        return ( "" , inf )
    if winer == 2 : 
        return ( "" , neginf )
    if move_counter >= max_move or env.isfull :
        return ( "" , 0 )

    if turn == None :
        turn = env.turn
    
    for i in range(stop)