/*
   Copyright (C) Dan Winship                    2006
   Copyright (C) Jeremy Allison                 2006

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
*/

#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

#ifndef DEBUG_ERROR
#define DEBUG_ERROR printf
#endif

/* Usage:
 *
 *   get_printing_ticket <smbspool cups args.>
 *
 * The cups args look like :
 *
 * [DEVICE_URI] job-id user title copies options [file]

 * Sets its uid to the given username and then invokes smbspool.
 */

#if 0
/* NEVER ENABLE THIS IT IS A SECURITY HOLE. USE ONLY FOR DEBUGGING. JRA. */
int printargs(const char *name, int argc, char **argv)
{
	FILE *fp;
	int i;
	fp = fopen(name, "w");
	for ( i = 0; i < argc; i++) {
		fprintf(fp, "argv[%d] = '%s'\n", i, argv[i]);
	}
	fclose(fp);
}
#endif

char *null_envp[] = { NULL };

int main (int argc, char **argv)
{
	uid_t uid, LP_UID;
	gid_t gid, LP_GID;
	struct passwd *pw;

	/* Get uid and gid of user lp */
	pw = getpwnam( "lp");
	if (!pw) {
		DEBUG_ERROR ( "Unknown username lp\n");
		return 1;
	}
	LP_UID = pw->pw_uid;
	if (LP_UID == (uid_t)-1) {
		DEBUG_ERROR ("Bad uid %lu for user lp\n", (unsigned long)LP_UID);
		return 1;
	}
	LP_GID = pw->pw_gid;
	if (LP_GID == (gid_t)-1) {
		DEBUG_ERROR ("Bad gid %lu for user lp\n", (unsigned long)LP_GID);
		return 1;
	}

	/* Check that calling uid/gid is "lp" or 0. (This hack doesn't have to
	 * survive beyond CODE10, so we can safely hardcode the ids.)
	 */

	/*
	 * THE FOLLOWING IS DONE AS ROOT. BEWARE !!!!!!!
	 */

	if (getuid() != LP_UID && getuid() != 0) {
		DEBUG_ERROR ("Bad invoking uid %lu\n", (unsigned long)getuid ());
		return 1;
	}
	if (getgid() != LP_GID && getgid() != 0) {
		DEBUG_ERROR ("Bad invoking gid %lu\n", (unsigned long)getgid ());
		return 1;
	}

	if (argc == 1) {
		uid = LP_UID; /* Invoke as uid lp to do a query-only. */
		gid = LP_GID; /* define gid too to suppress a warning */
	} else if (argc == 6 || argc == 7) {
		pw = getpwnam(argv[2]);
		if (!pw) {
			DEBUG_ERROR ("Unknown username %s\n", argv[3]);
			return 1;
		}
		uid = pw->pw_uid;
		if (uid == (uid_t)-1) {
			DEBUG_ERROR ("Bad uid %lu\n", (unsigned long)uid);
			return 1;
		}
		gid = pw->pw_gid;
		if (gid == (gid_t)-1) {
			DEBUG_ERROR ("Bad gid %lu\n", (unsigned long)gid);
			return 1;
		}
	} else {
		DEBUG_ERROR ("Bad number of args %u\n", (unsigned int)argc);
		return 1;
	}

	if (uid != LP_UID && uid < 500) {
		DEBUG_ERROR ("Bad uid %lu\n", (unsigned long)uid);
		return 1;
	}
	if (setgroups (0, NULL) != 0) {
		DEBUG_ERROR ("Couldn't clear groups: %s\n", strerror (errno));
		return 1;
	}
	if (setresgid (gid, gid, gid) != 0) {
		DEBUG_ERROR ("Couldn't set gid: %s\n", strerror (errno));
		return 1;
	}
	if (setresuid (uid, uid, uid) != 0) {
		DEBUG_ERROR ("Couldn't set uid: %s\n", strerror (errno));
		return 1;
	}

	/* Clear the environment to ensure nothing can
	   be loaded via LD_PRELOAD. Thanks to Sebastian Krahmer
	   from the SuSE security Team for reviewing this. */
	clearenv();

	/*
	 * We are now the requested user.
	 * From cups arg[0] is the smb:// uri and smbspool expects this
	 */

	return execve ("/usr/bin/smbspool", argv, null_envp);
}
