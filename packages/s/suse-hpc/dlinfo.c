#define _GNU_SOURCE
#include <dlfcn.h>
#include <link.h>
#include <stdio.h>
#include <stdlib.h>

int
main(int argc, char *argv[])
{
    void *dlh;
    struct link_map *linkmap;

    if (argc != 2) {
	fprintf(stderr, "Usage: %s <library>\n", argv[0]);
	exit(EXIT_FAILURE);
    }

    if ((dlh = dlopen(argv[1], RTLD_NOW)) == NULL)
	exit(EXIT_FAILURE);

    if (dlinfo(dlh, RTLD_DI_LINKMAP, &linkmap) == -1)
	exit(EXIT_FAILURE);

    printf("%s\n",linkmap->l_name);

    exit(EXIT_SUCCESS);
}
