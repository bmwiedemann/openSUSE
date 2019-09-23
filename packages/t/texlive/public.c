/*
 * Public	For user root run a specific program as user nobody
 *		for user root and others use group public and umask 0002
 *
 * Usage:	public -> [texhash|mktexlsr|mktexmf|mktexpk|mktextfm]
 *
 * Note:	This program has to set sgid public!
 *
 *		Copyright (C) 2010,2012 Werner Fink
 *
 *		This program is free software; you can redistribute it and/or modify
 *		it under the terms of the GNU General Public License as published by
 *		the Free Software Foundation; either version 2 of the License, or
 *		(at your option) any later version.
 *
 *		This program is distributed in the hope that it will be useful,
 *		but WITHOUT ANY WARRANTY; without even the implied warranty of
 *		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *		GNU General Public License for more details.
 *
 *		You should have received a copy of the GNU General Public License
 *		along with this program; if not, write to the Free Software
 *		Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 *
 */

#include <errno.h>
#include <limits.h>
#include <grp.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#ifndef TEXGRP
# define TEXGRP "public"
#endif
#ifndef MKTEX
# define "/usr/lib/mktex"
#endif

extern char **environ;

/*
 * This list is used to authenticate the program running.
 * It is fixed at compile time to avoid a full class of 
 * dangers ...
 */
static struct {
    const char *prog;
    const char *run;
} *lp, list[] =
{   /* prog		run			*/
    { "texhash",	MKTEX "/mktexlsr"	},
    { "mktexlsr",	MKTEX "/mktexlsr"	},
    { "mktexmf",	MKTEX "/mktexmf"	},
    { "mktexpk",	MKTEX "/mktexpk"	},
    { "mktextex",	MKTEX "/mktextex"	},
    { "mktextfm",	MKTEX "/mktextfm"	},
    { "false",		"/bin/false"		},
    { "true",		"/bin/true"		},
    { "public",		"/bin/true"		},
#ifdef DEBUG
    { "id",		"/usr/bin/id"		},
    { "printenv",	"/usr/bin/printenv"	},
#endif
    { 0,		0,			}};

static struct {
    const char *name;
    const char *value;
} *ep, envp[] =
{   { "TERM",		0			},
    { "PATH",		"/bin:/usr/bin"		},
    { "POSIXLY_CORRECT",0			},
    { "NLSPATH",	0			},
    { "LANG",		0			},
    { "LC_ALL",		0			},
    { "LC_CTYPE",	0			},
    { "LC_COLLATE",	0			},
    { "LC_MESSAGES",	0			},
    { "COLUMNS",	0			},
    { "TABSIZE",	0			},
    { "TIME_STYLE",	0			},
    { "LS_COLORS",	0			},
    { "LS_BLOCK_SIZE",	0			},
    { "BLOCK_SIZE",	0			},
    { "BLOCKSIZE",	0			},
    { 0,		0			}};

int main(int argc, char *argv[])
{
    char *program_name, *slash;
    struct passwd *pwd;
    struct group  *grp;
    uid_t ruid = getuid();
    uid_t euid = geteuid();
    gid_t rgid = getgid();
    gid_t egid = getegid();

    if ((slash = strrchr(argv[0], '/'))) {
	program_name = ++slash;
    } else {
	program_name = argv[0];
    }

    for (lp = list; lp->prog && strcmp(program_name, lp->prog); lp++) ;

    if (!lp->prog) {
	errno = EBADRQC;
	fprintf(stderr, "public: Usage:\n");
	fprintf(stderr, "   public linked to one of [");
	for (lp = list; lp->prog; lp++)
	    fprintf(stderr, "%s%c", lp->prog, (lp+1)->prog ? '|' : '\0');
	fprintf(stderr, "] names\n");
	goto err;
    }

    if ((grp = getgrnam(TEXGRP)) == (struct group*)0)
	goto err;

    if (ruid == 0 || euid == 0) {   /* If user is root switch over to nobody:public */
	int initgrp = 0;

	if ((pwd = getpwnam("nobody")) == (struct passwd*)0)
	    goto err;

	if (ruid != pwd->pw_uid)
	    ruid = pwd->pw_uid;

	if (rgid != grp->gr_gid || egid != grp->gr_gid) {
	    initgrp = 1;
	    rgid = grp->gr_gid;
	}

	if (setregid(rgid, pwd->pw_gid))
	    goto err;
	if (initgrp && initgroups(pwd->pw_name, rgid))
	    goto err;
	if (setreuid(ruid, pwd->pw_uid))
	    goto err;

	for (ep = envp; ep->name; ep++) {
	    if (ep->value)
		continue;
	    ep->value = getenv(ep->name);
	}

	clearenv();

	if (setenv("HOME", pwd->pw_dir, 1) < 0)
		goto err;
	if (setenv("USER", pwd->pw_name, 1) < 0)
		goto err;
	if (setenv("LOGNAME", pwd->pw_name, 1) < 0)
		goto err;
	if (setenv("GROUP", pwd->pw_name, 1) < 0)
		goto err;
	if (setenv("SHELL", pwd->pw_shell, 1) < 0)
		goto err;

	for (ep = envp; ep->name; ep++) {
	    if (!ep->value)
		continue;
	    setenv(ep->name, ep->value, 1);
	}

    } else if (rgid != grp->gr_gid && egid == grp->gr_gid) {
	rgid = grp->gr_gid;

	if (setregid(rgid, grp->gr_gid))
	    goto err;

    }

    umask(0002);
    execve(lp->run, argv, environ);
err:
    fprintf(stderr, "public: ");
    perror(program_name);
    return 1;
}
