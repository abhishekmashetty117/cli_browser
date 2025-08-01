import webbrowser
import datetime
####################################################################################
############# main() FUNCTION IS USED FOR CALLING IT IN OTHER FILE #################
####################################################################################
def main(username):
    ################################################################################
    ###### history() FUNCTION IS DELETING,OPENING AND STORAGE OF HISTORY ###########
    ################################################################################
    def history(username,url=None,key_h='a'):
        if(key_h=='d' or key_h=='D'):
            #file=open('historyfile.txt','   
            file=open(username+'_history.txt','w')
            file.close()
        elif(key_h=='o' or key_h=='O'):
            #file=open('historyfile.txt','a+')
            file=open(username+'_history.txt','a+')
            file.seek(0)
            check=file.read(1)
            if(check==''):
                print('\nNO HISTROY FOUND.......!!!!!!!!!!\n')
            else:
                file.seek(0)
                print('\n\t\t\t HISTORY\n')
                print(file.read())
                file.close()
        elif(key_h=='a'):
            #file=open('historyfile.txt','a')
            #file=open(username+'_history.txt','a')
            file=open(username+'_history.txt','a+')
            file.writelines(url)
            file.close()
    #################################################################################
    ########### bookmark() FUNCTION IS FOR STORING THE URL's OF FAVOURITES ##########
    #################################################################################            
    def bookmark(username,url=None,key_b='o'):
        if(key_b=='F' or key_b=='f'):        
             file=open(username+'_bookmarkfile.txt','a+')
             file.writelines(url)
             file.close()
    #################################################################################
    ############ bookmark_name_s() FUNCTION IS FOR STORING NAMES TO FAVOURITES ######
    #################################################################################
    def bookmark_name_s(username,bookmark_name):
            #file=open('bookmark_name.txt','a')
            file=open(username+'_bookmark_name.txt','a+')
            file.writelines(bookmark_name)
            file.close()
        
    flag=True
    lock='!'
    ur=True

    

    while(ur):
     key_total=input('            H :: HISTORY     F :: FAVOURITES    PRESS ENTER TO CONTINUE')
     flag=True
     if(key_total=='H' or key_total=='h'):
      history(username,key_h='o')
       #################################################################################
       ############  HISTORY FIELD,WITH DELETE,OPEN,BACK OPTIONS #######################
       #################################################################################
      while(flag==True):
        key_h=input('            O :: OPEN,    D :: DELETE,   B :: BACK    PRESS ENTER TO CONTINUE')
    
        key_h=key_h.upper()
        if(key_h=='O'):
             history(username,None,key_h)
        elif(key_h=='D'):
             history(username,None,key_h)
             print('\nHISTORY DELETED............\n')
        elif(key_h=='B'):
            ur=True
            flag=False
        elif(key_h==''):
            ur=False
            flag=False
        else:
            print('INVALID ENTRY')
        
     elif(key_total=='f' or key_total=='F'):
        #################################################################################
        ############  FAVOURITES FIELD,WITH DELETE,OPEN,BACK OPTIONS ####################
        ################################################################################# 
        #appending or creating of new file if new user
        file1=open(username+'_bookmarkfile.txt','a+')
        file2=open(username+'_bookmark_name.txt','a+')
        file1.seek(0)
        file2.seek(0)
        values_1=file1.readlines()
        keys_1=file2.readlines()
        file1.close()
        file2.close()
        output_behind={}
        output={}
        flag_inside=1
    
        while(flag_inside):
         for x in range(len(values_1)):
            output_behind[keys_1[x]]=values_1[x]
     
         if(len(keys_1)==0):
                print('\nNO FAVOURITES FOUND....\n')
         else:
             print('\n\t\t\tYOUR FAVOURITES\n')
             for x in range(1,len(keys_1)+1):
                 output[x]=keys_1[x-1]
                 print(x,output[x])

         lock=input('            O :: OPEN,    D :: DELETE,   B :: BACK    PRESS ENTER TO CONTINUE')
         lock=lock.upper()
         if(lock=='D'):
          if(len(keys_1)==0):
               pass  
          else:
              while(True):
               try:   
                user_input=int(input('ENTER THE NUMBER ,PRESS B FOR BACK'))
                if(user_input<=len(keys_1)):
                    #DELETING OF THE REQUIRED FAVOURITE FIELD
                    del(output_behind[output[user_input]])
                    del(output[user_input])
                    file1.close()
                    file2.close()
                    
                    #NO NEED FOR a+,BECAUSE BY THIS STAGE THE FILE IS CREATED IN LINE 68,69 IF REQUIRED
                    #WRITING INTO FILES AGAIN TO ADD THE EDITED DATA
                    file1=open(username+'_bookmarkfile.txt','w')
                    file2=open(username+'_bookmark_name.txt','w')
                    for keys_2 in output_behind:
                        file1.writelines(output_behind[keys_2])
                        file2.writelines(keys_2)   
                    file1.close()
                    file2.close()

                    #READING OF FILE AGAIN TO READ NEWLY ENTERED DATA AFTER DELETING
                    file1=open(username+'_bookmarkfile.txt','r')
                    file2=open(username+'_bookmark_name.txt','r')
                    values_1=file1.readlines()
                    keys_1=file2.readlines()
                    break
                else:
                    print('INVALID ENTRY')
               except ValueError or KeyError:
                   break 
               
         elif(lock=='O'):
           if(len(keys_1)==0):
               pass
           else: 
            while(True):
             try:   
              user_input=int(input('ENTER THE NUMBER ,PRESS B FOR BACK'))
              #OPENING OF REQUIRED FAVOURITE FIELD
              if(user_input<=len(keys_1)):
                url=output_behind[output[user_input]]
                url_i=url[:-1]+'\t'+str(datetime.datetime.now())+'\n'
                history(username,url_i)
                file1.close()
                file2.close()
                ur=False
                flag_inside=0
                webbrowser.open(url)
                break
              else:
                print('INVALID ENTRY')
             except ValueError or KeyError:
                break      
            
         elif(lock=='B'):
            ur=True
            flag_inside=0
         elif(lock==''):
             ur=False
             flag_inside=0
         else:
             print('INVALID ENTRY')
             ur=True
             flag_inside=0
    
     elif(key_total==''):
         ur=False
     
     else:
         print('INVALID ENTRY')
#################################################################################
#################################################################################
########## net CLASS IS FOR SEARCHING OF QUERY ,OPENING OF WEBSITES #############
#################################################################################
#################################################################################         
    class net:
        #########################################################################
        ################# anything() FUNCTION IS FOR QUERIES ####################
        #########################################################################
        def anything(self,username):
            query=input('ENTER YOUR QUERY')
            url='https://www.google.co.in/search?q='+query+'\n'
            url_i='https://www.google.co.in/search?q='+query
            url_i=url_i+'\t'+str(datetime.datetime.now())+'\n'
            history(username,url_i)
            return url
        ##########################################################################
        ######### bookmark_entry() FUNCTION IS FOR OPENING  OF WEBSITES  #########
        ########## AND ALSO SAVING AS FAVOURITES WITH NAME  ######################
        ##########################################################################
        def bookmark_entry(self,username,s):
            while(True):
                try:
                    key_b=input('PRESS F TO SET AS FAVOURITES , PRESS ENTER TO CONTINUE ')
                    if (key_b=='F' or key_b=='f'):
                        bookmark(username,s,key_b)
                        bookmark_name=input('ENTER THE BOOKMARK NAME')
                        bookmark_name=bookmark_name+'\n'
                        bookmark_name_s(username,bookmark_name)
                        webbrowser.open_new(s)
                        break
                    elif(key_b==''):
                        webbrowser.open(s)
                        break
                    else:
                        print('INVALID ENTRY')
                except ValueError:
                    print('INVALID ENTRY')
        ##########################################################################
        ################## website() FUNCTION IS FOR WEBSITES ####################
        ##########################################################################
        def website(self,username):
            url_w=input("ENTER THE WEBSITE ")
            url=url_w +'\n'
            url_w=url_w+'\t'+str(datetime.datetime.now())+'\n' 
            history(username,url_w)
            return url
    search=net()
    ##############################################################################
    ############## HERE IT CALLS THE ABOVE FUNCTIONS AS REQUIRED #################
    ##############################################################################
    if(lock!='O'):
         while(True):
             try:
                 k=int(input("ENTER   1 :: SURFING   2 :: WEBSITE ,ENTER TO CLOSE"))
                 if(k==1):
                   ret=search.anything(username)
                   search.bookmark_entry(username,ret)
                   break
                 elif(k==2):
                   ret=search.website(username) 
                   search.bookmark_entry(username,ret)
                   break
                 else:
                   print('INVALID ENTRY')
             except ValueError or KeyError:
                 print('INVALID ENTRY')


###########################################################################
############ THIS SECTION IS FOR LOG IN ,SIGN UP AND PUBLIC USE ###########
###########################################################################

def browse():
 flag_3=1
 while(flag_3):
    try:
        forward=input('     L  :: LOGIN     S  ::  SIGN UP     K  ::   SKIP')
        ###########################################################################
        ###################### THIS FILE IS FOR PUBLIC USE ########################
        ###########################################################################
        forward=forward.upper()
        if(forward=='K'):
            username='PUBLIC'
            main(username)
            break
        elif(forward=='S'):
            ########################################################################
            ####################### THIS FILE IS FOR SIGN UP #######################
            ########################################################################
            username=input('USERNAME  ')
            password=input('PASSWORD  ')
            #user=open('user.txt','a')
            user=open('user.txt','a')
            pas=open('pass.txt','a')
            username_i=username+'\n'
            password_i=password+'\n'
            user.writelines(username_i)
            pas.writelines(password_i)
            user.close()
            pas.close()
            main(username)
            break
        elif(forward=='L'):
            ########################################################################
            ####################### THIS FILE IS FOR LOG IN ########################
            ########################################################################
            flag_2=1
            while(flag_2):
                try:
                    username=input('USERNAME  ')
                    password=input('PASSWORD  ')
                    username_i=username+'\n'
                    password_i=password+'\n'
    
                    file1=open('user.txt','r')
                    file2=open('pass.txt','r')
    
                    pas=file2.readlines()
                    user=file1.readlines()
                    file1.close()
                    file2.close()
                    output_behind={}
                    output={}
                    if(username_i in user):                
                        for x in range(len(pas)):
                            output_behind[user[x]]=pas[x]
                        for x in range(len(pas)):
                            if(output_behind[username_i]==password_i):
                                main(username)
                                flag_2=0
                                flag_3=0
                                break                            
                            elif(x==len(pas)-1):
                                print('INCORRECT PASSWORD TRY AGAIN')                                
                    else:
                        print('INCORRECT USERNAME ,TRY SIGNING UP')
                        flag_2=0                        
                        break
                except FileNotFoundError:
                    print('TRY SIGNING UP')
                    flag_2=0
        else:
            print('INVALID ENTRY')
    except KeyError:
                print('INVALID ENTRY')

if __name__ == "__main__":
    browse()
