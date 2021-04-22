/*
 Copyright (c) 2019,2020 SUSE LLC

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
*/

#define _GNU_SOURCE

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>
#include <limits.h>
#include <sys/stat.h>
#include <unistd.h>
#include <errno.h>
#include <getopt.h>
#include <libintl.h>

#include <rpm/rpmts.h>
#include <rpm/rpmdb.h>
#include <rpm/rpmlib.h>
#include <fcntl.h>
#include <rpm/rpmcli.h>
#include <rpm/header.h>
#include <rpm/rpmfiles.h>

static int verbose = 0;

const char *dirs[] = {
	"/usr/bin",
	"/usr/lib",
#if __WORDSIZE == 64
       	"/usr/lib64",
#endif
	"/usr/sbin",
	NULL
};

// rpmdb stores dirs with slash
const char *rpmdirs[] = {
	"/bin/",
	"/lib/",
#if __WORDSIZE == 64
	"/lib64/",
#endif
	"/sbin/",
	NULL
};



static inline int startswith(const char* s, const char* pfx) {
	return strncmp(s, pfx, strlen(pfx)) == 0;
}

static inline char stm(mode_t m) {
	switch (m & S_IFMT) {
		case S_IFBLK:  return 'b';
		case S_IFCHR:  return 'c';
		case S_IFDIR:  return 'd';
		case S_IFIFO:  return 'p';
		case S_IFLNK:  return 'l';
		case S_IFREG:  return 'f';
		case S_IFSOCK: return 'S';
	}
	return '?';
}

int check_directory(const char* dir);

int check_entry(const char* p)
{
	struct stat st, stu;
	const char* rp = p+strlen("/usr");
	// if the file doesn't exist in /usr we're safe
	if(lstat(p, &stu)) {
		if (errno != ENOENT) {
			perror(p);
			return 1;
		}
		if (verbose > 1) printf("%s unique\n", p);
		return 0;
	}
	if(lstat(rp, &st)) {
		perror(rp);
		return 1;
	}
	// differnt file type, check if one is link and can be dropped
	if ((st.st_mode & S_IFMT) != (stu.st_mode & S_IFMT) || (S_ISLNK(st.st_mode) && S_ISLNK(stu.st_mode))) {
		if (S_ISLNK(st.st_mode) || S_ISLNK(stu.st_mode)) {
			struct stat sb1, sb2;
			// if the link in / points to the file in /usr it's fine
			// XXX: in theory there could be a weird
			// chain of links pointing back and forth
			// between /usr and /, we ignore that here
			if(!stat(rp, &sb1) && !stat(p, &sb2) && sb1.st_ino == sb2.st_ino) {
				if (verbose) printf("%s same file, ok\n", rp);
				return 0;
			}
		}
		fprintf(stderr, "%s mode mismatch %c vs %c\n", rp, stm(st.st_mode), stm(stu.st_mode));
		return 1;
	} else {
		if (S_ISLNK(st.st_mode)) {
			char t1[PATH_MAX] = {0};
			char t2[PATH_MAX] = {0};
			if(readlink(rp, t1, sizeof(t1)) == -1) {
				perror(rp);
				return 1;
			}
			if(readlink(p, t2, sizeof(t2)) == -1) {
				perror(p);
				return 1;
			}

			if (!strcmp(t1, t2)) {
				if (verbose) {
					printf("%s and %s both point %s, ok\n", rp, p, t1);
				}
				return 0;
			} else {
				fprintf(stderr, "%s link mismatch %s vs %s\n", rp, t1, t2);
			}
		} else if (!S_ISDIR(st.st_mode)) {
			fprintf(stderr, "%s duplicated\n", rp);
			return 1;
		}
		// both are directories, check recursive
		return check_directory(p);
	}
}

int check_directory(const char* dir)
{
	DIR* dh;
	struct dirent* d;
	unsigned failed = 0;

	dh = opendir(dir+strlen("/usr"));
	if (!dh) {
		perror(dir);
		return 1;
	}
	while ((d = readdir(dh))) {
		char p[PATH_MAX] = {0};

		if (!strcmp(d->d_name, ".") || !strcmp(d->d_name, ".."))
			continue;

		stpcpy(stpcpy(stpcpy(p, dir), "/"), d->d_name);

		failed += check_entry(p);
	}

	return failed;
}

int check_filesystem(const char* rootdir)
{
	unsigned failed = 0;
	if (rootdir) {
		if (chroot(rootdir)) {
			perror("chroot");
			return 1;
		}
	}
	for (int i = 0; dirs[i]; ++i) {
		struct stat st;
		const char* d = dirs[i]+strlen("/usr");
		if (lstat(d, &st)) {
			if (errno != ENOENT)
				perror(d);
			continue;
		}
		if (S_ISDIR(st.st_mode)) {
			failed += check_directory(dirs[i]);
		} else if (S_ISLNK(st.st_mode)) {
			char buf[PATH_MAX] = {0};
			if(readlink(d, buf, sizeof(buf)) == -1) {
				perror(d);
				continue;
			}
			if (strcmp(buf, dirs[i]+1)) {
				fprintf(stderr, "wrong link %s: %s should be %s\n", d, buf, dirs[i]+1);
			}
		}
	}
	if (failed) {
		fprintf(stderr, ngettext("%u file prevents usrmerge\n", "%u files prevent usrmerge\n", failed), failed);
	}

	return failed == 0;
}

int rpm_findusrfile(rpmts ts, Header hdr, rpmfi orig_fi)
{
	char fn[PATH_MAX] = "/usr";
	strcpy(fn+strlen(fn), rpmfiFN(orig_fi));

	rpmdbMatchIterator mi = rpmtsInitIterator(ts, RPMDBI_INSTFILENAMES, fn, 0);
	if (mi) {
		Header h;
		int conflict = 1;
		while ((h = rpmdbNextIterator(mi)) != NULL) {
			rpmfiles files = rpmfilesNew(NULL, hdr, 0, 0);
			rpmfi fi = rpmfilesIter(files, 0);

			int fx = rpmfiFindFN(fi, fn);
			if (fx != -1) {
				rpmfiSetFX(fi, fx);
				if (S_ISDIR(rpmfiFMode(fi)) && S_ISDIR(rpmfiFMode(orig_fi))) {
					conflict = 2;
				}
			}
			rpmfiFree(fi);
			rpmfilesFree(files);
		}
		// we just look at the first one. If there's a
		// second match and that is somewhow conflicting the
		// system was screwed already.
		rpmdbFreeIterator(mi);
		return conflict;
	}
	return 0;
}

int check_rpmdb(char* rootdir)
{
	unsigned failed = 0;

	rpmcliConfigured();

	rpmts ts = rpmtsCreate();
	if (!ts) {
		fprintf(stderr, "failed to create RPM transaction\n");
		return -1;
	}

	if (rootdir)
		rpmtsSetRootDir(ts, rootdir);

	if (rpmtsOpenDB(ts, O_RDONLY) != 0) {
		fprintf(stderr, "failed to open RPM database\n");
		return -1;
	}

	rpmdbMatchIterator iter = rpmtsInitIterator(ts, RPMDBI_PACKAGES, NULL, 0);
	Header hdr;
	while ((hdr = rpmdbNextIterator(iter)) != NULL) {
		rpmfiles files = rpmfilesNew(NULL, hdr, 0, 0);
		rpmfi fi = rpmfilesIter(files, 0);
		char skipdir[PATH_MAX] = {0};
		int conflict = 0;
		while (rpmfiNext(fi) >= 0) {
			if (skipdir[0] && startswith(rpmfiFN(fi), skipdir)) {
				if (verbose > 2)
					printf("skipping %s as %s is known\n", rpmfiFN(fi), skipdir);
				continue;
			} else {
				skipdir[0] = 0;
			}
			for (int i = 0; rpmdirs[i]; ++i) {
				if(startswith(rpmfiODN(fi), rpmdirs[i])) {
					rpm_mode_t m = rpmfiFMode(fi);
					conflict = rpm_findusrfile(ts, hdr, fi);
					if (conflict) {
						if (conflict == 2) {
							if (verbose > 2) {
								fprintf(stderr, "directory %s ok\n", rpmfiFN(fi));
							}
							conflict = 0;
						} else if (verbose > 1) {
							char* n = headerGetAsString(hdr, RPMTAG_NEVRA);
							fprintf(stderr, "%s: %s conflict\n", n, rpmfiFN(fi));
							free(n);
						}
					} else if (S_ISDIR(m)) {
						// an optimization so we don't have to check hundreds
						// of kernel modules. If the file at hand is a directory
						// and does not exist in /usr we can just skip the rest.
						strcpy(skipdir, rpmfiFN(fi));
					}
					break;
				}
			}
		}
		rpmfiFree(fi);
		rpmfilesFree(files);

		if (conflict) {
			++failed;
			if (verbose == 1) {
				char* n = headerGetAsString(hdr, RPMTAG_NEVRA);
				printf("%s breaks\n", n);
				free(n);
			}
		}

	}

	if (failed) {
		fprintf(stderr, ngettext("%u package prevents usrmerge\n", "%u packages prevent usrmerge\n", failed), failed);
	}

	return failed == 0;
}

int main(int argc, char** argv)
{
	enum { fs, rpmdb } mode = fs;
	int c;
	char* rootdir = NULL;

	static struct option long_options[] = {
		{"verbose", no_argument,       0,  'v' },
		{"rpmdb",   no_argument,       0,  128 },
		{"root",    required_argument, 0,  129 },
		{0,         0,                 0,  0 }
	};

        while ((c = getopt_long(argc, argv, "v", long_options, NULL)) != -1) {
		switch(c) {
			case 'v': ++verbose; break;
			case 128: mode = rpmdb; break;
			case 129: rootdir=strdup(optarg); break;
		}
	}

	if (mode == rpmdb)
		return check_rpmdb(rootdir) == 0;

	return check_filesystem(rootdir) == 0;
}
