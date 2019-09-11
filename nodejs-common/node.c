#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

const unsigned min_version = 4;
const unsigned max_version = 20;
const char *default_version = "-default";

const char * const supported_execs[] = {
	"node",
	"npm",
	"npx",
	NULL
};


static void __attribute__((noreturn)) printInvalidVersion(const char *version) {
	fprintf(stderr, "Invalid node version: %s\n", version);
	exit(-2);
}


int main(int argc, char *argv[])
{
	if (argc < 1) {
		fprintf(stderr, "Invalid parameters ... no basename?\n");
		return 128;
	}

	/* Verify we are called with supported name */
	const char *program_name = basename(argv[0]);
	const char * const * bn = supported_execs;

	for (; *bn!=NULL; bn++) {
		if (strcmp(*bn, program_name) == 0)
			break;
	}

	if (*bn == NULL) {
		fprintf(stderr, "Invalid program called: '%s'\n", program_name);
		return 129;
	}

	/* Verify we have one of probably supported versions */
	const char *version = getenv("NODE_VERSION");
	char *endptr = 0;
	if (version == NULL || strcmp(version, default_version) == 0)
		version = default_version;

	unsigned long node_ver = strtoul(version, &endptr, 10);

	if (*endptr == '\0' &&
	    ( node_ver < min_version || node_ver > max_version))
	{
		printInvalidVersion(version);
	}
	else if (*endptr != '\0' && version != default_version)
	{
		printInvalidVersion(version);
	}

	/* Generate our program path and check that we can execute it */
	char *program_path, *program;
	if (asprintf(&program, "%s%s", *bn, version) == -1 ||
	    asprintf(&program_path, "/usr/bin/%s", program) == -1) {

		fputs("Memory allocation error... terminating\n", stderr);
		return 130;
	}

	if (access(program_path, X_OK) != 0) {
		perror(program_path);
		return -1;
	}

	argv[0] = program;

	execv(program_path, argv);
	perror("execv failed");
	return -1;
}

