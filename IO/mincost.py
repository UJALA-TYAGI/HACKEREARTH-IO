def Solve (k, arr):

    sum1=0

    counter=0

    m=k



    for i in arr:



        if(i>=0):

            counter+=1

            sum1+=i

            m=k

        else:

            if(counter==0):

                return abs(sum(arr)+i)



            else:

                m-=1

                if(m<0):

                    sum1+=abs(i)

                else:

                    sum1+=i



    return abs(sum1)



n,k = map(int, input().split())

arr = map(int, input().split())



out_ = Solve(k, arr)

print (out_)
