/*
 * This is a minimal skeleton for code using libmpathpersist.
 * Compile with "-lmpathpersist -lmultipath -lmpathcmd".
 *
 * Header files for libmultipath are intentionally not included
 * in the multipath-tools-devel package, because libmultipath has
 * no well defined API for external programs at this time.
 *
 * With multipath-tools 0.8.6, the sample program can be drastically
 * simplified, see below. Compare with libmpathpersist-example-old.c
 * for 0.8.5 and older. Note that the old code can still be used.
 */

#include <mpath_persist.h>
#include <libudev.h>

struct config *conf;

int main(void)
{
	conf = mpath_lib_init();
	if(!conf) {
		return 1;
	}
	return 0;
}
