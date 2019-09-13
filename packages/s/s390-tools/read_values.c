/********************************************************************************/
/*										*/
/*	Copyright (C) 2014-2015, SUSE LLC					*/
/*										*/
/*	All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

#define _GNU_SOURCE
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

static char *versionstring	= "Version 1.0 2015-10-12 13:31";

static char *version	   	= "1.0.0";

void	*configuration_handle	= NULL;
int	layers			= -1;

/*
 *	List of machine types
 */
struct machinetype {
	char	*typenumber;
	char	*fullname;
	} machinetypes[] =  {
	{ "2064", "2064 = z900    IBM eServer zSeries 900" },
	{ "2066", "2066 = z800    IBM eServer zSeries 800" },
	{ "2084", "2084 = z990    IBM eServer zSeries 990" },
	{ "2086", "2086 = z890    IBM eServer zSeries 890" },
	{ "2094", "2094 = z9-EC   IBM System z9 Enterprise Class" },
	{ "2096", "2096 = z9-BC   IBM System z9 Business Class" },
	{ "2097", "2097 = z10-EC  IBM System z10 Enterprise Class" },
	{ "2098", "2098 = z10-BC  IBM System z10 Business Class" },
	{ "2817", "2817 = z196    IBM zEnterprise 196" },
	{ "2818", "2818 = z114    IBM zEnterprise 114" },
	{ "2827", "2827 = z12-EC  IBM zEnterprise EC12" },
	{ "2828", "2828 = z12-BC  IBM zEnterprise BC12" },
	{ "2964", "2964 = z13     IBM z13" },
	};

int	debug = 0;

/******************************************************************************/
/*									      */
/*									      */
/*									      */
/******************************************************************************/
void	print_version()
{
printf("Version: %s\n", version);
}
/******************************************************************************/
/*									      */
/*	Look for one attribute and print it				      */
/*									      */
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
			printf("%s: ",(user_string == NULL? "NULL": user_string));
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
	printf("Fehler: erg = %d, result_string = %s \n", erg, (result_string == NULL? "NULL": result_string));
	/* TODO qc_get_attribute_string returned error */
	}
} /* print_attribute  */

/********************************************************************************/
/*										*/
/*	Open the lib and get the handle						*/
/*										*/
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
/*										*/
/*	Look at the type of machine we're running on and print out a user	*/
/*	friendly string								*/
/*										*/
/********************************************************************************/
void print_cputype()
{
int	i, search;
int	erg;
const char	*cpu_type = NULL;

	erg = qc_get_attribute_string(configuration_handle, qc_type, 0, &cpu_type);
	if (erg == 1 && cpu_type != NULL) {
		for (i = 0, search = 1; (i < sizeof(machinetypes) / sizeof(struct machinetype)) && search ; i++)
		   {
		   if (strcmp(cpu_type, machinetypes[i].typenumber) == 0) {
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
/*										*/
/*	Print out the values for SCC						*/
/*										*/
/*	To uniquely identify a machine the following information is used:	*/
/*										*/
/*	Type									*/
/*	Sequence code								*/
/*	CPUs total								*/
/*	CPUs IFL								*/
/*	LPAR Number								*/
/*	LPAR Characteristics:							*/
/*	LPAR CPUs								*/
/*	LPAR IFLs								*/
/*										*/
/*	Optional:								*/
/*										*/
/*	VM00 Name								*/
/*	VM00 Control Programm							*/
/*	VM00 CPUs								*/
/*										*/
/********************************************************************************/
void print_scc()
{
print_version();
print_attribute("Type", 0, qc_type, string, WITH_KEY);
print_attribute("Sequence Code", 0, qc_sequence_code, string, WITH_KEY);
print_attribute("CPUs Total", 0, qc_num_cpu_total, integer, WITH_KEY);
print_attribute("CPUs IFL", 0, qc_num_cpu_total, integer, WITH_KEY);
print_attribute("LPAR Number", 1, qc_partition_number, integer, WITH_KEY);
print_attribute("LPAR Name", 1, qc_layer_name, string, WITH_KEY);
print_attribute("LPAR Characteristics", 1, qc_partition_char, string, WITH_KEY);
print_attribute("LPAR CPUs Total", 1, qc_num_cpu_total, integer, WITH_KEY);
print_attribute("LPAR CPUs IFL", 1, qc_num_cpu_total, integer, WITH_KEY);
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
/*									      */
/*	print out the uuid for this machine				      */
/*									      */
/*	TODO!								      */
/*									      */
/******************************************************************************/
void print_uuid()
{
return;
} /* print_uuid */

/******************************************************************************/
/*									      */
/*	print out the list of valid / found symbols			      */
/*									      */
/******************************************************************************/
void list(char * list_attribute_param)
{
return;
} /* list */

/******************************************************************************/
/*									      */
/*	print out the requested attribute				      */
/*									      */
/******************************************************************************/
void print_user_attribute(char *key, char *attribute_param, int layer)
{
return;
} /* print_uuid */


/******************************************************************************/
/*									      */
/*	Help Function							      */
/*									      */
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
/*									      */
/*	Main								      */
/*									      */
/******************************************************************************/
int main(int argc, char **argv, char **envp)
{
int	opt;
int	read_sysinfo_opt;
int	print_attr;
int	print_cpu;
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
		while ((opt = getopt(argc, argv, "a:cd:hL:suV")) != -1) {
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
	   if ((print_attr + print_cpu + list_attr + create_scc + create_uuid) > 1) {
	   	fputs("Only one of the options a, c, L, s or u can be specified.",stderr);
		return 1;
	   } /* endif */
	   /* still not im[plemented thatfore set to zero */
	   create_uuid = list_attr = print_attr = 0;
	   if (print_attr != 0) {
	   	print_user_attribute(NULL, print_attribute_param, layers);
		goto main_exit;
	   } /* endif */
	   if (print_cpu != 0) {
		print_cputype();
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
	   	print_uuid();
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
} /* end main */
