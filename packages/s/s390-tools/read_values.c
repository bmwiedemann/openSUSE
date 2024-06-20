/********************************************************************************/
/*                                                                              */
/*	Copyright (C) 2014-2015, 2019-2023 SUSE LLC                             */
/*                                                                              */
/*	All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

#define _GNU_SOURCE
#include <sys/utsname.h>
#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include <query_capacity.h>

/*
 *	Data types
 */
enum datatypes {
	integer,
	string,
	floatingpoint
};

#define	WITHOUT_KEY	0
#define	WITH_KEY	1

static char *versionstring	= "Version 1.0.5 2024-06-20 14:30";

static char *version	   	= "1.0.5";

void	*configuration_handle	= NULL;
int	layers			= -1;

/*
 *	List of machine types
 */
struct machinetype {
	enum qc_model_families model_families;
	char	*typenumber;
	char	*fullname;
	} machinetypes[] =  {
	{ QC_TYPE_FAMILY_IBMZ,	   "2064", "2064 = z900    IBM eServer zSeries 900" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2066", "2066 = z800    IBM eServer zSeries 800" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2084", "2084 = z990    IBM eServer zSeries 990" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2086", "2086 = z890    IBM eServer zSeries 890" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2094", "2094 = z9-EC   IBM System z9 Enterprise Class" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2096", "2096 = z9-BC   IBM System z9 Business Class" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2097", "2097 = z10-EC  IBM System z10 Enterprise Class" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2098", "2098 = z10-BC  IBM System z10 Business Class" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2817", "2817 = z196    IBM zEnterprise 196" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2818", "2818 = z114    IBM zEnterprise 114" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2827", "2827 = z12-EC  IBM zEnterprise EC12" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2828", "2828 = z12-BC  IBM zEnterprise BC12" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2964", "2964 = z13     IBM z13" },
	{ QC_TYPE_FAMILY_LINUXONE, "2964", "2964 = IBM LinuxONE Emperor" },
	{ QC_TYPE_FAMILY_IBMZ,	   "2965", "2965 = z13s    IBM z13s (single frame)" },
	{ QC_TYPE_FAMILY_LINUXONE, "2965", "2965 = IBM LinuxONE Rockhopper" },
	{ QC_TYPE_FAMILY_IBMZ,	   "3906", "3906 = z14     IBM z14" },
	{ QC_TYPE_FAMILY_LINUXONE, "3906", "3906 = IBM LinuxONE Emperor II" },
	{ QC_TYPE_FAMILY_IBMZ,	   "3907", "3907 = z14 ZR1 IBM z14 ZR1" },
	{ QC_TYPE_FAMILY_LINUXONE, "3907", "3907 = IBM LinuxONE Rockhopper II" },
	{ QC_TYPE_FAMILY_IBMZ,	   "8561", "8561 = z15 T01 IBM z15 T01" },
	{ QC_TYPE_FAMILY_LINUXONE, "8561", "8561 = IBM LinuxONE III LT1" },
	{ QC_TYPE_FAMILY_IBMZ,	   "8562", "8562 = z15 T02 IBM z15 T02" },
	{ QC_TYPE_FAMILY_LINUXONE, "8562", "8562 = IBM LinuxONE III LT2" },
	{ QC_TYPE_FAMILY_IBMZ,     "3931", "3931 = z16 A01 IBM z16 A01" },
	{ QC_TYPE_FAMILY_LINUXONE, "3931", "3931 = IBM LinuxONE Emperor 4" },
	{ QC_TYPE_FAMILY_IBMZ,     "3932", "3932 = z16 A02 IBM z16 A02" },
	{ QC_TYPE_FAMILY_LINUXONE, "3932", "3932 = IBM LinuxONE Rockhopper 4" },
	};

int	debug = 0;

/******************************************************************************/
/*                                                                            */
/*	Print the program version                                             */
/*                                                                            */
/******************************************************************************/
void	print_version()
{
printf("Version: %s\n", version);
}
/******************************************************************************/
/*                                                                            */
/*	Look for one attribute and print it                                   */
/*                                                                            */
/******************************************************************************/
void print_attribute(char *user_string, int level, enum qc_attr_id attribute, enum datatypes type, int print_key)
{ 
int		erg = 0;
const char	*result_string = NULL;
int		result_int = 0;
float		result_float = 0.0;
	
	switch (type)
	   {
	   case integer:
		erg = qc_get_attribute_int(configuration_handle, attribute, level, &result_int);
	   	break;
	   case string:
		erg = qc_get_attribute_string(configuration_handle, attribute, level, &result_string);
	   	break;
	   case floatingpoint:
		erg = qc_get_attribute_float(configuration_handle, attribute, level, &result_float);
	   	break;
	   default:
	   	break;
	   }
	if (erg == 1) {
		if (print_key == WITH_KEY) {
			printf("%s : ",(user_string == NULL? "NULL": user_string));
		} /* endif */
		switch (type)
		   {
		   case integer:
			printf("%d\n",result_int);
			break;
		   case string:
			printf("%s\n", result_string);
			break;
		   case floatingpoint:
		   	printf("%f\n",result_float);
			break;
		   default:
			break;
		   }
	} /* endif */
	else {
		if ( erg == 0 ) {
                /*   printf("%s : Attribute exists, but is not set. \n", (user_string == NULL? "NULL": user_string)); */
		} /* endif */
		else if ( erg < 0) {
	           printf("%s: An error occurred retrieving the attribute. Error: erg = %d, result_string = %s \n", user_string, erg, (result_string == NULL? "NULL": result_string));
		} /* end else if */
	/*                                             */	
	/* TODO qc_get_attribute_string returned error */
	/*                                             */	
	}
} /* print_attribute  */

/********************************************************************************/
/*                                                                              */
/*	Open the lib and get the handle                                         */
/*                                                                              */
/********************************************************************************/
int read_sysinfo()
{
int	return_code;

	configuration_handle = qc_open(&return_code);
	if (return_code < 0) {
		printf("Error: Unable to open configuration, return_code =%d\n", return_code);
		return -1;
	} /* endif */
	if (return_code > 0) {
		printf("Warning: Unable to read configuration completely, return_code =%d\n", return_code);
		return -2;
	} /* endif */
	if (configuration_handle == NULL) {
		printf("Error: Unable to open configuration, return_code =%d\n", return_code);
		return -3;
	} /* endif */
	layers = qc_get_num_layers(configuration_handle, &return_code);
	if (layers < 0) {
		printf("Error: Unable to retrieve number of layers, return_code =%d\n", return_code);
		return -4;
	} /* endif */
	return 0;
} /* read_sysinfo */

/********************************************************************************/
/*                                                                              */
/*	Look at the type of machine we're running on and print out a user       */
/*	friendly string                                                         */
/*                                                                              */
/********************************************************************************/
void print_cputype()
{
int	i, search;
int	erg;
const char	*cpu_type = NULL;
int	family_type = -1;

/*
 *	First find out whether we run on an IBM Z, or a LinuxONE system
 */
	erg = qc_get_attribute_int(configuration_handle, qc_type_family, 0, &family_type);
	if (erg <= 0 || family_type == -1) {
		printf("Error reading family type\n");
		return;
	} /* endif */
/*
 *	Now get the machine ID
 */
	erg = qc_get_attribute_string(configuration_handle, qc_type, 0, &cpu_type);
	if (erg == 1 && cpu_type != NULL) {
		for (i = 0, search = 1; (i < sizeof(machinetypes) / sizeof(struct machinetype)) && search ; i++)
		   {
		   if ((family_type ==  machinetypes[i].model_families) && (strcmp(cpu_type, machinetypes[i].typenumber) == 0)) {
		   	printf("%s\n", machinetypes[i].fullname);
			search = 0;
		   } /* endif */
		   } /* endfor */
		if (search != 0) {
			printf("An unknown machine type was reported: %s\n\
Please file a bug report with this output:\n" , cpu_type);
/*	TODO output of /proc/sysinfo					      */
		} /* endif */
	} /* endif */
	return;
} /* print_cputype  */

/********************************************************************************/
/*                                                                              */
/*	Print out the values for SCC                                            */
/*                                                                              */
/*	To uniquely identify a machine the following information is used:       */
/*                                                                              */
/*	Type                                                                    */
/*	Sequence code                                                           */
/*	CPUs total                                                              */
/*	CPUs IFL                                                                */
/*	LPAR Number                                                             */
/*	LPAR Characteristics:                                                   */
/*	LPAR CPUs                                                               */
/*	LPAR IFLs                                                               */
/*                                                                              */
/*	Optional:                                                               */
/*                                                                              */
/*	VM00 Name                                                               */
/*	VM00 Control Programm                                                   */
/*	VM00 CPUs                                                               */
/*                                                                              */
/********************************************************************************/
void print_scc()
{
print_version();
print_attribute("Type", 0, qc_type, string, WITH_KEY);
print_attribute("Type Name", 0, qc_type_name, string, WITH_KEY);
print_attribute("Sequence Code", 0, qc_sequence_code, string, WITH_KEY);
print_attribute("CPUs Total", 0, qc_num_ifl_total, integer, WITH_KEY);
print_attribute("CPUs IFL", 0, qc_num_ifl_total, integer, WITH_KEY);
print_attribute("LPAR Number", 1, qc_partition_number, integer, WITH_KEY);
print_attribute("LPAR Name", 1, qc_layer_name, string, WITH_KEY);
print_attribute("LPAR Characteristics", 1, qc_partition_char, string, WITH_KEY);
print_attribute("LPAR CPUs Total", 1, qc_num_ifl_total, integer, WITH_KEY);
print_attribute("LPAR CPUs IFL", 1, qc_num_ifl_total, integer, WITH_KEY);
if (layers  > 2) {
/*
 *	This means, that eather zKVM or z/Vm is running
 */
	print_attribute("VM00 Name", 3, qc_layer_name, string, WITH_KEY);
	print_attribute("VM00 Control Program", 2, qc_control_program_id, string, WITH_KEY);
	print_attribute("VM00 CPUs Total", 3, qc_num_cpu_total, integer, WITH_KEY);
	print_attribute("VM00 IFLs", 3, qc_num_cpu_total, integer, WITH_KEY);
} /* endif */
return;
} /* print_scc */


/******************************************************************************/
/*                                                                            */
/*      Secure boot support models ( check_model () )                         */
/*      Only the following machines support secure boot:                      */
/*         z14, z14 ZR1, z15, z16                                             */
/*                                                                            */
/******************************************************************************/

int check_model (const char *cpu) {

        #define     IBM_Models    6    /* Number of IBM models listed below   */
        char *types[IBM_Models] = {
               "3906",
               "3907",
               "8561",
               "8562",
               "3931",
               "3932",
       };

       int i;
       int models = sizeof(types) / sizeof(types[0]);

        for ( i = 0; i < models; i++) {

           if ( !strcmp(cpu,types[i]) ) {
              return 1;
              };
        }
        return 0;
} /* check_model */


/******************************************************************************/
/*                                                                            */
/*	print out whether secure boot is enabled                              */
/*                                                                            */
/******************************************************************************/
void print_secure_mode()
{
int	erg;
int	release_major;
int	release_sub;
int	release_minor;
const char	*cpu_type = NULL;
int     cpu_okay = 0;
int     Layer = 0;
int     i = 0;
/*
 *	First we have to check whether we have the appropriate kernel Level (>= 5.3)
 */

struct utsname uts;

	erg = uname(&uts);
	if (erg != 0) {
		perror ("Error executing uname(): ");
		return;
	} /* endif */
#if	0
	printf("sysname:  %s\n", uts.sysname);
	printf("nodename: %s\n", uts.nodename);
	printf("release:  %s\n", uts.release);
#endif
	/*
	 *	A release number looks like:  m.s.mi
	 *	where m, s, mi are numbers with one ore more digits
	 *	Minimum kernel version is 5.3
	 */
	erg = sscanf(uts.release,"%d.%d.%d-%*s", &release_major, &release_sub, &release_minor);
	if ( release_major < 5 ) {
		goto return_does_not_exist;
	}
	if ( release_sub < 3 ) {
		goto return_does_not_exist;
	}
#if	0
	printf("Translated successfully: %d\n", erg);
	printf("release_major: %d\n", release_major);
	printf("release_sub: %d\n", release_sub);
	printf("release_minor: %d\n", release_minor);
	printf("version:  %s\n", uts.version);
	printf("machine:  %s\n", uts.machine);
	printf("Print_secure called\n");
#endif
	/*
	 *	Only the following machines support secure boot: 
	 *     z14,        z15,        z16
	 *	3906, 3907, 8561, 8562, 3931, 3932
	 */
	erg = qc_get_attribute_string(configuration_handle, qc_type, 0, &cpu_type);
	if (erg == 1 && cpu_type != NULL) {
	        cpu_okay = check_model(cpu_type);	
		if ( cpu_okay == 0 ) {
			goto return_does_not_exist;
		} /* endif */
	} /* endif */

	for ( i = 0; i < layers; i++) {
            erg = qc_get_attribute_int(configuration_handle, qc_layer_type_num, i, &Layer);
	    if (erg == 1) {
	       print_attribute("Secure mode on  ", i, qc_has_secure, integer, WITH_KEY);
	       print_attribute("Secure mode used", i, qc_secure,     integer, WITH_KEY);
	       } /* endif */
	    } /* endfor */
return;

return_does_not_exist:
/*
 *	Software or hardware does not support secure boot.
 */
	puts("Secure mode on : 0\nSecure mode used : 0");
return;
} /* print_secure_mode */


/******************************************************************************/
/*                                                                            */
/*	print out the uuid for this machine                                   */
/*                                                                            */
/******************************************************************************/
int print_uuid()
{
	const char	*result_string = NULL;
	int erg;

	erg = qc_get_attribute_string(configuration_handle, qc_sequence_code, 0, &result_string);
	if (erg != 1)
	{
		puts("Error reading the Serial Number");
		return 1;
	}
	printf("%s", result_string);

	result_string = NULL;

	erg = qc_get_attribute_string(configuration_handle, qc_layer_name, 1, &result_string);
	if (erg != 1)
	{
		puts("Error reading the LPAR Name");
		return 1;
	}
	printf("-%s", result_string);

	result_string = NULL;
	if (layers  > 2) {

		erg = qc_get_attribute_string(configuration_handle, qc_layer_name, 3, &result_string);
		if (erg != 1)
		{
			puts("Error Reading the VM Name");
			return 1;
		}
		printf("-%s", result_string);
	}
	putchar('\n');
	return 0;
} /* print_uuid */

/******************************************************************************/
/*                                                                            */
/*	print out the list of valid / found symbols                           */
/*                                                                            */
/******************************************************************************/
void list(char * list_attribute_param)
{
return;
} /* list */

/******************************************************************************/
/*                                                                            */
/*	print out the requested attribute                                     */
/*                                                                            */
/******************************************************************************/
void print_user_attribute(char *key, char *attribute_param, int layer)
{
return;
} /* print_user_attribute */


/******************************************************************************/
/*                                                                            */
/*	Help Function                                                         */
/*                                                                            */
/******************************************************************************/
void help()
{
puts("help:\n\
\n\
-a <attribute>	List the value of the named attribute\n\
-c		Print the cputype of this machine\n\
-d <number>	Debug Level\n\
-h		this help\n\
-L <keyword>	List the requested list (Attribute, Recognised)\n\
-s 		create Info for SCC\n\
-S		report whether secure boot is switched on\n\
-u		create uuid\n\
-V		print version string\n\
");
#if	0
if (debug != 0) {
	puts("\n\
Valid values for debug:\n\
	4 - read sysinfo.zvm from current directory instead of /proc/sysinfo\n\
	8 - printout lines read in from source (see debug == 4)\n\
	16 - printf found keys in store_value\n\
	32 - Search expression in show attribute\n\
");
} /* endif */
#endif
} /* help  */

/******************************************************************************/
/*                                                                            */
/*	Main                                                                  */
/*                                                                            */
/******************************************************************************/
int main(int argc, char **argv, char **envp)
{
int	opt;
int	read_sysinfo_opt;
int	print_attr;
int	print_cpu;
int	print_secure;
int	print_help;
int	list_attr;
int	create_scc;
int	create_uuid;
int	erg;
int	return_code;
char 	*print_attribute_param = NULL;
char	*list_attribute_param = NULL;
void	*configuration_handle_tmp = NULL;

	read_sysinfo_opt =
	print_attr	=
	print_cpu	=
	print_secure	=
	print_help	=
	list_attr	=
	create_scc	=
	create_uuid	=
	return_code	=
	erg		= 0;
	if (strcmp(argv[0],"cputype") == 0) {
		read_sysinfo_opt++;
		print_cpu++;
	} /* endif */
	else {
		while ((opt = getopt(argc, argv, "a:cd:hL:sSuV")) != -1) {
		   switch (opt)
		      {
		      case 'a':
				read_sysinfo_opt++;
				print_attr++;
				print_attribute_param = strdup(optarg);
			break;
		      case 'c':
				read_sysinfo_opt++;
				print_cpu++;
			break;
		      case 'd':
				debug = atoi(optarg);
				if ((debug & 1) == 1) {
					setenv("QC_DEBUG", "1", 1);
				} /* endif */
				if ((debug & 2) == 2) {
					setenv("QC_AUTODUMP", "1", 1);
				} /* endif */
				debug = debug >> 2;
			break;
		      case 'L':
				read_sysinfo_opt++;
				list_attr++;
				list_attribute_param = strdup(optarg);
			break;
		      case 's': /* create unique string for scc  */
				read_sysinfo_opt++;
				create_scc++;
			break;
		      case 'S': /* print out whether secure boot is enabled  */
				read_sysinfo_opt++;
				print_secure++;
			break;
		      case 'u': /* create UUID  */
				read_sysinfo_opt++;
				create_uuid++;
			break;
		      case 'V':
				printf("%s\n",versionstring);
				return 0;
			break;
		      case 'h':
		      default:
				print_help++;
			 break;
		      } /* endswitch */
		   } /* while */
	     } /* endlse */
	   if (print_help != 0) {
		help();
		return 0;
	   } /* endif */
	   if (read_sysinfo_opt != 0) {
	   	if ((erg = read_sysinfo()) != 0) {
			return -erg;
		} /* endif */
	   } /* endif */
	   if ((print_attr + print_cpu + print_secure + list_attr + create_scc + create_uuid) > 1) {
	   	fputs("Only one of the options a, c, L, s, S or u can be specified.\n",stderr);
		return 1;
	   } /* endif */
	   /* still not implemented thatfore set to zero */
	   list_attr = print_attr = 0;
	   if (print_attr != 0) {
	   	print_user_attribute(NULL, print_attribute_param, layers);
		goto main_exit;
	   } /* endif */
	   if (print_cpu != 0) {
		print_cputype();
		goto main_exit;
	   } /* endif */
	   if (print_secure != 0) {
		print_secure_mode();
		goto main_exit;
	   } /* endif */
	   if (list_attr != 0) {
		list(list_attribute_param);
		goto main_exit;
	   } /* endif */
	   if (create_scc != 0) {
	   	print_scc();
		goto main_exit;
	   } /* endif */
	   if (create_uuid != 0) {
	   	if(print_uuid() == 1){
	   		goto main_exit_error;
	   	}
		goto main_exit;
	   } /* endif */
	   help();
main_exit:
	if (configuration_handle != NULL) {
		configuration_handle_tmp = qc_open(&return_code);
		qc_close(configuration_handle);
		setenv("QC_DEBUG", "0", 1);
		setenv("QC_AUTODUMP", "0", 1);
		qc_close(configuration_handle_tmp);
	} /* endif */

return 0;

main_exit_error:
return 1;
} /* end main */
