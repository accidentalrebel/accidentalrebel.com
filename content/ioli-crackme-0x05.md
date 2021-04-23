
#include <stdio.h>

int main()
{
    char* pattern = "\x39\x37\x31"; //"\xD0\xFE\x28"; 
    printf("Hello World [%s]\n", pattern);
    
    int i = 88;
    int sret = sscanf(pattern, "%d", &i);
    printf("Ret %d [%d]", sret, i);

    return 0;
}
