/* ***** BEGIN COPYRIGHT BLOCK *****
 * Copyright (C) 2006 Red Hat, Inc.
 * All rights reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation version
 * 2.1 of the License.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 * ***** END COPYRIGHT BLOCK ***** */

#include <stdio.h>
#include <string.h>
#include <pkcs11.h>
#include <pkcs11n.h>

/*
 * windows specific globing search
 */
#ifdef WIN32 
#include <windows.h>
#include <winver.h>
#include <winreg.h>
#include <direct.h>
#include <shlobj.h>

#define PINST_FILE_DATA WIN32_FIND_DATA
#define PINST_ITERATOR  HANDLE
#define PINST_FIRST(pattern, data) FindFirstFile(pattern, &data)
#define PINST_PATH(iter, data)  (data).cFileName
#define PINST_NEXT(iter, data)  FindNextFile(iter, &data)
#define PINST_FREE_ITER(iter, data)	FindClose(iter)
#define PINST_INVALID_ITERATOR INVALID_HANDLE_VALUE
#define PINST_IS_DIRECTORY(iter, data) \
	((data).dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
#define PINST_IS_HIDDEN(iter, data) \
	((data).dwFileAttributes & FILE_ATTRIBUTE_HIDDEN) 
#define PINST_FULLPATH(tempPath,path) tempPath
#define PINST_ERROR DWORD
#define PINST_NO_MORE ERROR_NO_MORE_FILES
#define PINST_SET_ERROR(x) SetLastError(x)
#define PINST_GET_ERROR() GetLastError()
#define PINST_FS "\\"


/*#define NETSCAPE_KEY "Software\\Netscape\\Netscape Navigator\\Main" */
#define NETSCAPE_KEY "Software\\Netscape\\Netscape Navigator"
#define NETSCAPE_SUBKEY_1 "Main"
#define NETSCAPE_SUBKEY_2 "Install Directory"

/* capture the window's error string */
static void
winPerror(FILE *outFile, DWORD error, const char *msgString)
{
     char buffer[256];
     char *cp;
     DWORD ret;

     fprintf(outFile,"*** %s: ",msgString);
     sprintf(buffer,"Format message problem, error = %d (0x%x)\n", error, error);
     ret=FormatMessage(FORMAT_MESSAGE_FROM_SYSTEM, NULL, error, 0, buffer, 
							sizeof(buffer), NULL);
     for (cp=buffer; *cp; cp++) {
	if (*cp == '\r') *cp = ' ';
     }
     fprintf(outFile, buffer);
}
#endif

/*
 * otherwise we are assuming unix (posix)
 */
#ifndef PINST_FILE_DATA
#define UNIX
#include <stdlib.h>
#include <limits.h>
#include <glob.h>
#define PINST_FILE_DATA glob_t
#define PINST_ITERATOR  int
#define PINST_INVALID_ITERATOR  -1
#define PINST_FIRST(pattern, data) \
   ((glob(pattern, GLOB_MARK, NULL, &data) == 0) ? 0 : PINST_INVALID_ITERATOR)
#define PINST_PATH(iter, data) \
       (((data).gl_pathv == NULL) ? 0 : (data).gl_pathv[iter] )
#define PINST_NEXT(iter, data) (((data).gl_pathc > ++iter) ?  iter : 0)
#define PINST_FREE_ITER(iter, data) globfree(&data)
#define PINST_IS_DIRECTORY(iter, data) pinst_isdir(PINST_PATH(iter,data))
#define PINST_IS_HIDDEN(iter, data) (0)
#define PINST_FULLPATH(tempPath,path) path
#define PINST_ERROR int
#define NO_ERROR 0
#define PINST_NO_MORE NO_ERROR
#define PINST_SET_ERROR(x)
#define PINST_GET_ERROR() NO_ERROR
#define PINST_FS "/"


#define MAX_PATH PATH_MAX 

static int
pinst_isdir(const char *path)
{
    int len = strlen(path);


    return (len > 0) && (path[len-1] == '/');
}

#endif
	

typedef enum _InstType {
    Install,
    UnInstall,
} InstType;

typedef enum _DirType {
   AppDataDir = 0,
   HomeDir,
   NetscapeInstallDir,
   MaxDirType,
} DirType;

char *dirPaths[MaxDirType] = { NULL };

typedef struct _DirList {
    DirType dirType;
    char *search;
    char *tail;
} DirList;

DirList dirList[] = {
#ifdef WIN32 
    { AppDataDir, "Mozilla\\Profiles\\*", "*.slt" },
    { AppDataDir, "Mozilla\\Firefox\\Profiles\\*", NULL },
    { AppDataDir, "Thunderbird\\Profiles\\*", NULL },
    { NetscapeInstallDir, "..\\Users\\*", NULL },
#endif
#ifndef MAC 
#ifdef UNIX
    { HomeDir, ".mozilla/firefox/*", NULL },
    { HomeDir, ".mozilla/*", NULL },
    { HomeDir, ".thunderbird/*", NULL },
    { HomeDir, ".netscape", NULL },
#endif
#endif
#ifdef MAC 

    { HomeDir, "Library/Mozilla/Profiles/*", "*.slt"},
    { HomeDir, "Library/Application Support/Firefox/Profiles/*", NULL },
    { HomeDir, "Library/Thunderbird/Profiles/*", NULL },


#endif


};

int verbose = 0;

int dirListCount = sizeof(dirList)/sizeof(dirList[0]);

static void
usage(char *prog)
{
    fprintf(stderr,"usage: %s [-u][-v][-s][-l] [-p path] module\n", prog);
    return;
}

/* Utility printing functions */



#define CONFIG_TAG "configDir="
int
installPKCS11(char *dirPath, char *dbType, InstType type, char *module)
{
    char *paramString = (char *)malloc(strlen(dbType)+strlen(dirPath)+sizeof(CONFIG_TAG)+3);
    char *cp;
    char **rc;

    if (paramString == NULL) {
	PINST_SET_ERROR(ERROR_NOT_ENOUGH_MEMORY);
	return 0;
    }
    sprintf(paramString,CONFIG_TAG"\"%s%s\" ",dbType,dirPath);

    /* translate all the \'s to /'s */
    for (cp=paramString; *cp; cp++) {
	if (*cp == '\\') *cp='/';
    }

    /* don't call this if you have NSS initialized!!, use SECMOD_AddModule
     * or SECMOD_AddUserModule instead */

    /* Ignore this missing in the header for gcc14 */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wimplicit-function-declaration"
    rc = (char **) NSC_ModuleDBFunc(type == Install ? 
			SECMOD_MODULE_DB_FUNCTION_ADD :
			SECMOD_MODULE_DB_FUNCTION_DEL, paramString, module); 
#pragma GCC diagnostic pop
    if (verbose) {
	fprintf(stderr, "Install \"%s\" in %s : %s\n", module, dirPath, 
							rc ? *rc : "Fail" );
    }
	
    free(paramString);
    return 1;
}


int
installAllPKCS11(char *dirPath, char *dbType, char *search, char *tail,
					InstType type, char *module)
{
    char *searchString;
    unsigned long searchStringLen;
    int len;
    char *tempPath, *fileStart;
    PINST_FILE_DATA fileData;
    PINST_ITERATOR iter;
    PINST_ERROR err = NO_ERROR;

    char *myPath = NULL;

    searchString = (char *)malloc(strlen(dirPath)+2+strlen(search));

    if (searchString == NULL) {
	PINST_SET_ERROR(ERROR_NOT_ENOUGH_MEMORY);
	return 0;
    }
    sprintf(searchString,"%s" PINST_FS "%s",dirPath,search);

    searchStringLen = strlen(searchString);
    tempPath=malloc(searchStringLen+MAX_PATH+1);
    if (tempPath == NULL) {
	free(searchString);
	PINST_SET_ERROR(ERROR_NOT_ENOUGH_MEMORY);
	return 0;
    }
    strcpy(tempPath, searchString);
    fileStart = strrchr(tempPath, *PINST_FS);
    if (fileStart == NULL) {
	tempPath[searchStringLen] = *PINST_FS;
	fileStart = &tempPath[searchStringLen];
    }
    fileStart++;

    iter = PINST_FIRST(searchString, fileData);
    free(searchString);
    if (iter == PINST_INVALID_ITERATOR) {
	/* error set by PINST_FIRST */
	free(tempPath);
	return 0;
    }

    len=1;

    do {
	char *path = PINST_PATH(iter, fileData);
        if(!path)
        {
            break;
        }

	if (!PINST_IS_DIRECTORY(iter, fileData)) {
	    continue;
	}
	if (PINST_IS_HIDDEN(iter, fileData)) {
	    continue;
	}
 	/* skip . and .. */
	if ((path[0] == '.') && ((path[1] == 0) || 
				 (path[1] == '.' && path[2] == 0)) ) {
	    continue;
	}
	strcpy(fileStart,path);

	myPath=PINST_FULLPATH(tempPath,path);
	if (tail) {
	    installAllPKCS11(myPath, dbType, tail, NULL, type, module);
	} else {
	    installPKCS11(myPath, dbType, type, module);
	}
    } while (PINST_NEXT(iter, fileData));
    free(tempPath);

    err = PINST_GET_ERROR();
    PINST_FREE_ITER(iter,fileData);

    if (err != PINST_NO_MORE) {
	/* restore the previous error (in case FindClose trashes it) */
	PINST_SET_ERROR(err);
	return 0;
    }
    return 1;
}
	
int main(int argc, char **argv)
{
    char *module = NULL;
    char *prog = *argv++;
    char *cp;
    int argCount = 0;
    int i;
    InstType type = Install;
    char * path = NULL;
    char *dbType = "";
#ifdef WIN32
    BOOL brc;
    HKEY regKey;
    unsigned long lrc;
    TCHAR appData[MAX_PATH];
    char netscapeInstall[MAX_PATH];
    unsigned long nsInstallSize = MAX_PATH;
#endif

    /*
     * parse the arglist;
     */
    while ((cp = *argv++) != 0) {
	if (*cp == '-') {
	    while (*++cp) switch (*cp) {
	    case 'i':
		type = Install;
		break;
	    case 'u':
		type = UnInstall;
		break;
	    case 'v':
		verbose = 1;
		break;
	    case 'l':
		dbType = "dbm:";
		break;
	    case 's':
		dbType = "sql:";
		break;
	    case 'p':
		path = *argv++;
		if (path == NULL) {
		    usage(prog);
		    return 2;
		}
		break;
	    default:
		usage(prog);
		return 2;
	    }
	} else switch (argCount++) {
	case 0:
	    module = cp;
	    break;
	default:
	    usage(prog);
	    return 2;
	}
    }

    if (module == NULL) {
	usage(prog);
    }

    if (path) {
	installAllPKCS11(path, dbType, "", NULL, type, module);
	return 0;
    }

#ifdef WIN32 
    /* App Data Dir */
    brc = SHGetSpecialFolderPath(NULL, appData, CSIDL_APPDATA, FALSE);
    if (brc) {
	dirPaths[AppDataDir] = appData;
    } else {
	if (verbose) {
	    winPerror(stderr, GetLastError(), "Reading App Directory");
	}
    }

    /* Netscape Install Dir */
    lrc = RegOpenKeyEx(HKEY_LOCAL_MACHINE, NETSCAPE_KEY, 0, 
					KEY_ENUMERATE_SUB_KEYS, &regKey);
    if (lrc == ERROR_SUCCESS) {
	int i = 0;
	TCHAR productName[255];
	HKEY prodKey;
	HKEY mainKey;

	while ((lrc = RegEnumKey(regKey, i, productName, sizeof(productName)))
							 == ERROR_SUCCESS) {
	    i++;
	    lrc = RegOpenKeyEx(regKey, productName, 0, 
					KEY_ENUMERATE_SUB_KEYS, &prodKey);
	    if (lrc != ERROR_SUCCESS) {
		if (verbose) {
		    winPerror(stderr, GetLastError(), 
					"Reading Netscape 4.0 prodkey");
		    fprintf(stderr,"Product = %s\n",productName);
		}
		continue;
	    }
	    lrc = RegOpenKeyEx(prodKey, NETSCAPE_SUBKEY_1, 0, 
						KEY_QUERY_VALUE, &mainKey);
	    if (lrc != ERROR_SUCCESS) {
	        RegCloseKey(prodKey);
		continue;
	    }
	    /* open main */
	    lrc = RegQueryValueEx(mainKey, NETSCAPE_SUBKEY_2, NULL, NULL, 
					netscapeInstall, &nsInstallSize);
	    RegCloseKey(mainKey);
	    RegCloseKey(prodKey);
	    if (lrc == ERROR_SUCCESS)  {
		if (netscapeInstall[nsInstallSize-1] == 0) {
		    if (verbose) {
		        fprintf(stderr, 
		   	   "Found Netscape 4.0 Install directory\n");
		    }
		    dirPaths[NetscapeInstallDir] = netscapeInstall;
		    break;
		} else {
		    fprintf(stderr, 
			"Reading Netscape 4.0 key: Value too large\n");
		}
	    } else {
		if (verbose) {
		    winPerror(stderr, lrc, "Reading Netscape 4.0 key");
		}
	   }
	}
	if ((lrc != ERROR_SUCCESS) && (lrc != ERROR_NO_MORE_ITEMS)) {
	    winPerror(stderr, lrc, "EnumKey on Netscape Registry Key failed");
	}
    } else {
	if (verbose) {
	    winPerror(stderr, lrc, "Openning Netscape 4.0 key");
	}
    }
#endif
#ifdef UNIX
    dirPaths[HomeDir] = getenv("HOME");
#endif

    /* OK, now search the directories and complete the Install */
    for (i=0; i < dirListCount; i++) {
	char *dirPath = dirPaths[dirList[i].dirType];
	if (!dirPath) {
	    continue;
	}
	installAllPKCS11(dirPath, dbType, dirList[i].search, dirList[i].tail, 
								type, module);
    }

    return 0;
}
