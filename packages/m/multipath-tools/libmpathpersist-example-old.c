/*
 * This is a minimal skeleton for code using libmpathpersist.
 * Compile with "-lmpathpersist -lmultipath -ludev".
 *
 * Header files for libmultipath are intentionally not included
 * in the multipath-tools-devel package, because libmultipath has
 * no well defined API for external programs at this time.
 */

#include <mpath_persist.h>
#include <libudev.h>

struct udev *udev;
/*
 * logsink determines where libmultipath log messages go
 * 1  - log to syslog only
 * -1 - log to syslog and stderr
 * 0  - log to syslog and stderr, with timestamps
 */
int logsink;

static struct config *conf;

struct config *get_multipath_config(void) {
	return conf;
}

void put_multipath_config(struct config* c)
{
}

int main(void)
{
	udev = udev_new();
	conf = mpath_lib_init();
	if(!conf) {
		udev_unref(udev);
		return 1;
	}
	return 0;
}
