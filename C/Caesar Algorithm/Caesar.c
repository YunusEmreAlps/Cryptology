// Caesar Algorithm

#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
    char msg[40];
    int i=0, j=0, length=0;
    char A[length], ch;
    int key;

    // input message
    printf("Please enter your message : ");
    gets(msg);

    // uppercase
    while(msg[j]){

        ch = msg[j];
        msg[j] = toupper(ch);
        j++;
    }
    while(msg[i] != '\0')  // string length
    {
        length++;
        i++;
    }

    // input key
    printf("Please enter your key number : ");
    while(1){
        scanf("%d",&key);
        if((key>0)&&(key<27)){
            break;
        }
    }

    // new message
    for (i=0; i<length; i++)
    {
        int B=0;
        B=(int)msg[i];
        int temp = 0;
        if (B > (90-key))
        {
            temp = (B+key)%90;
            temp = temp+64;
            printf("%c",(char)temp);
            A[i] += (char)temp;
        }
        else
        {
            printf("%c",(char)(B+key));
            A[i] += (char)(B+key);
        }
    }

    getch();
    return 0;
}
