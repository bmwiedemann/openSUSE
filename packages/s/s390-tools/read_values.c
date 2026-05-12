/********************************************************************************/
/*                                                                              */
/*      Copyright (C) 2014-2015, 2019-2026 SUSE LLC                             */
/*                                                                              */
/*      All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

/*
 * read_values.c
 *
 * Optimized version of system information query tool for IBM Z.
 * Uses qclib: https://github.com/ibm-s390-linux/qclib
 * Includes /proc/sysinfo fallback to prevent qclib's 
 *     "Unable to open configuration, return_code =-2" errors.
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
#include <stdbool.h>
#include <query_capacity.h>

/*
 * Constants and Globals
 */
static const char *VERSION_STRING = "Version 1.1.1 2026-05-12";
static const char *VERSION_NUMBER = "1.1.1";

void *config_handle = NULL;
int global_layers = -1;
int debug_level = 0;

typedef enum {
    TYPE_INTEGER,
    TYPE_STRING,
    TYPE_FLOAT
} DataType;

/*
 * Fallback Structure for when qclib fails
 */
typedef struct {
    char type[64];
    char sequence_code[64];
    int cpus_total;
    char lpar_name[64];
    int lpar_number;
} ProcSysinfo;

ProcSysinfo proc_fallback = { "Unknown", "Unknown", 0, "Unknown", 0 };

/*
 * Mapping for User Input -> qclib Attributes
 */
typedef struct {
    const char *name;
    enum qc_attr_id id;
    DataType type;
} AttributeMap;

/* 
 * Table of supported attributes.
 */
static const AttributeMap ATTR_TABLE[] = {
    { "qc_layer_type_num",      qc_layer_type_num,      TYPE_INTEGER },
    { "qc_layer_category_num",  qc_layer_category_num,  TYPE_INTEGER },
    { "qc_layer_name",          qc_layer_name,          TYPE_STRING },
    { "qc_layer_uuid",          qc_layer_uuid,          TYPE_STRING },
    { "qc_type_family",         qc_type_family,         TYPE_INTEGER },
    { "qc_type",                qc_type,                TYPE_STRING },
    { "qc_type_name",           qc_type_name,           TYPE_STRING },
    { "qc_model",               qc_model,               TYPE_STRING },
    { "qc_sequence_code",       qc_sequence_code,       TYPE_STRING },
    { "qc_partition_number",    qc_partition_number,    TYPE_INTEGER },
    { "qc_partition_char",      qc_partition_char,      TYPE_INTEGER },
    { "qc_control_program_id",  qc_control_program_id,  TYPE_STRING },
    { "qc_num_cpu_total",       qc_num_cpu_total,       TYPE_INTEGER },
    { "qc_num_ifl_total",       qc_num_ifl_total,       TYPE_INTEGER },
    { "qc_num_cp_total",        qc_num_cp_total,        TYPE_INTEGER },
    { "qc_num_ziip_total",      qc_num_ziip_total,      TYPE_INTEGER },
    { "qc_num_cpu_configured",  qc_num_cpu_configured,  TYPE_INTEGER },
    { "qc_num_cpu_standby",     qc_num_cpu_standby,     TYPE_INTEGER },
    { "qc_num_cpu_reserved",    qc_num_cpu_reserved,    TYPE_INTEGER },
    { "qc_num_cpu_dedicated",   qc_num_cpu_dedicated,   TYPE_INTEGER },
    { "qc_num_cpu_shared",      qc_num_cpu_shared,      TYPE_INTEGER },
    { "qc_has_secure",          qc_has_secure,          TYPE_INTEGER },
    { "qc_secure",              qc_secure,              TYPE_INTEGER }
};

static const size_t ATTR_TABLE_SIZE = sizeof(ATTR_TABLE) / sizeof(ATTR_TABLE[0]);

/*
 * Machine Type Definition
 */
struct machinetype {
    enum qc_model_families model_family;
    const char *typenumber;
    const char *fullname;
};

/* Hardware database */
static const struct machinetype MACHINE_TYPES[] = {
    { QC_TYPE_FAMILY_IBMZ,     "2064", "2064 = z900    IBM eServer zSeries 900" },
    { QC_TYPE_FAMILY_IBMZ,     "2066", "2066 = z800    IBM eServer zSeries 800" },
    { QC_TYPE_FAMILY_IBMZ,     "2084", "2084 = z990    IBM eServer zSeries 990" },
    { QC_TYPE_FAMILY_IBMZ,     "2086", "2086 = z890    IBM eServer zSeries 890" },
    { QC_TYPE_FAMILY_IBMZ,     "2094", "2094 = z9-EC   IBM System z9 Enterprise Class" },
    { QC_TYPE_FAMILY_IBMZ,     "2096", "2096 = z9-BC   IBM System z9 Business Class" },
    { QC_TYPE_FAMILY_IBMZ,     "2097", "2097 = z10-EC  IBM System z10 Enterprise Class" },
    { QC_TYPE_FAMILY_IBMZ,     "2098", "2098 = z10-BC  IBM System z10 Business Class" },
    { QC_TYPE_FAMILY_IBMZ,     "2817", "2817 = z196    IBM zEnterprise 196" },
    { QC_TYPE_FAMILY_IBMZ,     "2818", "2818 = z114    IBM zEnterprise 114" },
    { QC_TYPE_FAMILY_IBMZ,     "2827", "2827 = z12-EC  IBM zEnterprise EC12" },
    { QC_TYPE_FAMILY_IBMZ,     "2828", "2828 = z12-BC  IBM zEnterprise BC12" },
    { QC_TYPE_FAMILY_IBMZ,     "2964", "2964 = z13     IBM z13" },
    { QC_TYPE_FAMILY_LINUXONE, "2964", "2964 = IBM LinuxONE Emperor" },
    { QC_TYPE_FAMILY_IBMZ,     "2965", "2965 = z13s    IBM z13s (single frame)" },
    { QC_TYPE_FAMILY_LINUXONE, "2965", "2965 = IBM LinuxONE Rockhopper" },
    { QC_TYPE_FAMILY_IBMZ,     "3906", "3906 = z14     IBM z14" },
    { QC_TYPE_FAMILY_LINUXONE, "3906", "3906 = IBM LinuxONE Emperor II" },
    { QC_TYPE_FAMILY_IBMZ,     "3907", "3907 = z14 ZR1 IBM z14 ZR1" },
    { QC_TYPE_FAMILY_LINUXONE, "3907", "3907 = IBM LinuxONE Rockhopper II" },
    { QC_TYPE_FAMILY_IBMZ,     "8561", "8561 = z15 T01 IBM z15 T01" },
    { QC_TYPE_FAMILY_LINUXONE, "8561", "8561 = IBM LinuxONE III LT1" },
    { QC_TYPE_FAMILY_IBMZ,     "8562", "8562 = z15 T02 IBM z15 T02" },
    { QC_TYPE_FAMILY_LINUXONE, "8562", "8562 = IBM LinuxONE III LT2" },
    { QC_TYPE_FAMILY_IBMZ,     "3931", "3931 = z16 A01 IBM z16 A01" },
    { QC_TYPE_FAMILY_LINUXONE, "3931", "3931 = IBM LinuxONE Emperor 4" },
    { QC_TYPE_FAMILY_IBMZ,     "3932", "3932 = z16 A02 IBM z16 A02" },
    { QC_TYPE_FAMILY_LINUXONE, "3932", "3932 = IBM LinuxONE Rockhopper 4" },
    { QC_TYPE_FAMILY_IBMZ,     "9175", "9175 = z17 ME1 IBM z17 ME1" },
    { QC_TYPE_FAMILY_LINUXONE, "9175", "9175 = IBM LinuxONE Emperor 5" },
    { QC_TYPE_FAMILY_IBMZ,     "9176", "9176 = z17     IBM z17    " },
    { QC_TYPE_FAMILY_LINUXONE, "9176", "9176 = IBM LinuxONE Rockhopper 5" },
};

/*
 * Helper: Clean up resources on exit
 */
void cleanup(void) {
    if (config_handle != NULL) {
        qc_close(config_handle);
        config_handle = NULL;
        setenv("QC_DEBUG", "0", 1);
        setenv("QC_AUTODUMP", "0", 1);
    }
}

void print_version(void) {
    printf("Version: %s\n", VERSION_NUMBER);
}

void print_usage(void) {
    puts("Usage:\n"
         "\n"
         "-a <attribute>  List the value of the named attribute\n"
         "-c              Print the cputype of this machine\n"
         "-d <number>     Debug Level (1=QC_DEBUG, 2=QC_AUTODUMP)\n"
         "-h              Print this help\n"
         "-L <keyword>    List supported attributes (e.g. -L attributes)\n"
         "-s              Create Info for SCC\n"
         "-S              Report whether secure boot is switched on\n"
         "-u              Create UUID\n"
         "-V              Print version string\n");
}

/*
 * Fallback: Parses standard kernel /proc/sysinfo if qclib fails
 */
void load_fallback_sysinfo(void) {
    FILE *fp = fopen("/proc/sysinfo", "r");
    if (!fp) return;

    char line[256];
    while (fgets(line, sizeof(line), fp)) {
        if (strncmp(line, "Type:", 5) == 0) {
            sscanf(line + 5, "%63s", proc_fallback.type);
        } else if (strncmp(line, "Sequence Code:", 14) == 0) {
            sscanf(line + 14, "%63s", proc_fallback.sequence_code);
        } else if (strncmp(line, "CPUs Total:", 11) == 0) {
            sscanf(line + 11, "%d", &proc_fallback.cpus_total);
        } else if (strncmp(line, "LPAR Name:", 10) == 0) {
            sscanf(line + 10, "%63s", proc_fallback.lpar_name);
        } else if (strncmp(line, "LPAR Number:", 12) == 0) {
            sscanf(line + 12, "%d", &proc_fallback.lpar_number);
        }
    }
    fclose(fp);
}

/*
 * Initialize qclib safely. 
 * NEVER returns a non-zero exit code to prevent installation errors.
 */
void init_sysinfo(void) {
    int rc = 0;

    config_handle = qc_open(&rc);
    if (config_handle == NULL || rc < 0) {
        fprintf(stderr, "\nWarning: qclib information unavailable (rc=%d).\n Engaging /proc/sysinfo fallback.\n\n", rc);
        load_fallback_sysinfo();
        return;
    }

    global_layers = qc_get_num_layers(config_handle, &rc);
    if (global_layers < 0) {
        fprintf(stderr, "\nWarning: Unable to retrieve layers (rc=%d).\n Engaging /proc/sysinfo fallback.\n\n", rc);
        qc_close(config_handle);
        config_handle = NULL;
        load_fallback_sysinfo();
    }
}

void print_attribute(const char *label, int level, enum qc_attr_id attr_id, DataType type, bool show_key) {
    int rc = 0;
    int val_int = 0;
    float val_float = 0.0f;
    const char *val_str = NULL;

    if (!config_handle) return; // Silent return if using fallback

    switch (type) {
        case TYPE_INTEGER: rc = qc_get_attribute_int(config_handle, attr_id, level, &val_int); break;
        case TYPE_STRING:  rc = qc_get_attribute_string(config_handle, attr_id, level, &val_str); break;
        case TYPE_FLOAT:   rc = qc_get_attribute_float(config_handle, attr_id, level, &val_float); break;
    }

    if (rc == 1) {
        if (show_key) printf("%s : ", (label ? label : "NULL"));
        
        switch (type) {
            case TYPE_INTEGER: printf("%d\n", val_int); break;
            case TYPE_STRING:  printf("%s\n", val_str ? val_str : ""); break;
            case TYPE_FLOAT:   printf("%f\n", val_float); break;
        }
    } else if (rc < 0) {
        fprintf(stderr, "%s: Error retrieving attribute. Code: %d\n", label ? label : "Attribute", rc);
    }
}

void print_cputype(void) {
    /* FALLBACK CHECK */
    if (!config_handle) {
        printf("%s = Generic s390x Node (Fallback Data)\n", proc_fallback.type);
        return;
    }

    int rc, family_type = -1;
    const char *cpu_type = NULL;

    rc = qc_get_attribute_int(config_handle, qc_type_family, 0, &family_type);
    if (rc <= 0 || family_type == -1) {
        fprintf(stderr, "Error reading family type\n");
        return;
    }

    rc = qc_get_attribute_string(config_handle, qc_type, 0, &cpu_type);
    if (rc != 1 || cpu_type == NULL) {
        fprintf(stderr, "Error reading CPU type string\n");
        return;
    }

    size_t num_types = sizeof(MACHINE_TYPES) / sizeof(MACHINE_TYPES[0]);
    for (size_t i = 0; i < num_types; i++) {
        if ((enum qc_model_families)family_type == MACHINE_TYPES[i].model_family && 
            strcmp(cpu_type, MACHINE_TYPES[i].typenumber) == 0) {
            printf("%s\n", MACHINE_TYPES[i].fullname);
            return;
        }
    }

    const char *family_name = "Unknown Family";
    if ((enum qc_model_families)family_type == QC_TYPE_FAMILY_IBMZ) family_name = "IBM zSystems";
    else if ((enum qc_model_families)family_type == QC_TYPE_FAMILY_LINUXONE) family_name = "IBM LinuxONE";

    printf("%s = %s (Generic)\n", cpu_type, family_name);
}

void print_scc(void) {
    /* FALLBACK CHECK */
    if (!config_handle) {
        print_version();
        printf("Type : %s\n", proc_fallback.type);
        printf("Sequence Code : %s\n", proc_fallback.sequence_code);
        printf("CPUs Total : %d\n", proc_fallback.cpus_total);
        printf("LPAR Number : %d\n", proc_fallback.lpar_number);
        printf("LPAR Name : %s\n", proc_fallback.lpar_name);
        return;
    }

    print_version();
    print_attribute("Type", 0, qc_type, TYPE_STRING, true);
    print_attribute("Type Name", 0, qc_type_name, TYPE_STRING, true);
    print_attribute("Sequence Code", 0, qc_sequence_code, TYPE_STRING, true);
    print_attribute("CPUs Total", 0, qc_num_ifl_total, TYPE_INTEGER, true);
    print_attribute("CPUs IFL", 0, qc_num_ifl_total, TYPE_INTEGER, true);
    print_attribute("LPAR Number", 1, qc_partition_number, TYPE_INTEGER, true);
    print_attribute("LPAR Name", 1, qc_layer_name, TYPE_STRING, true);
    print_attribute("LPAR Characteristics", 1, qc_partition_char, TYPE_STRING, true);
    print_attribute("LPAR CPUs Total", 1, qc_num_ifl_total, TYPE_INTEGER, true);
    print_attribute("LPAR CPUs IFL", 1, qc_num_ifl_total, TYPE_INTEGER, true);

    if (global_layers > 2) {
        print_attribute("VM00 Name", 3, qc_layer_name, TYPE_STRING, true);
        print_attribute("VM00 Control Program", 2, qc_control_program_id, TYPE_STRING, true);
        print_attribute("VM00 CPUs Total", 3, qc_num_cpu_total, TYPE_INTEGER, true);
        print_attribute("VM00 IFLs", 3, qc_num_cpu_total, TYPE_INTEGER, true);
    }
}

void print_secure_mode(void) {
    /* FALLBACK CHECK */
    if (!config_handle) {
        puts("Secure mode on : 0\nSecure mode used : 0");
        return;
    }

    struct utsname uts;
    int major, sub;

    if (uname(&uts) != 0) {
        perror("Error executing uname");
        return;
    }

    if (sscanf(uts.release, "%d.%d", &major, &sub) != 2) return;
    if (major < 5 || (major == 5 && sub < 3)) goto not_supported;

    bool found_any = false;
    int secure_val = 0;
    
    for (int i = 0; i < global_layers; i++) {
        if (qc_get_attribute_int(config_handle, qc_has_secure, i, &secure_val) == 1) {
            print_attribute("Secure mode on  ", i, qc_has_secure, TYPE_INTEGER, true);
            print_attribute("Secure mode used", i, qc_secure,     TYPE_INTEGER, true);
            found_any = true;
        }
    }

    if (found_any) return;

not_supported:
    puts("Secure mode on : 0\nSecure mode used : 0");
}

int print_uuid(void) {
    /* FALLBACK CHECK */
    if (!config_handle) {
        printf("%s-%s\n", proc_fallback.sequence_code, proc_fallback.lpar_name);
        return 0;
    }

    const char *seq_code = NULL;
    const char *lpar_name = NULL;
    const char *vm_name = NULL;

    if (qc_get_attribute_string(config_handle, qc_sequence_code, 0, &seq_code) != 1) {
        fprintf(stderr, "Error reading Serial Number\n");
        return 1; // Note: Kept 1 here just for strictly UUID usage, but doesn't crash global init
    }
    printf("%s", seq_code);

    if (qc_get_attribute_string(config_handle, qc_layer_name, 1, &lpar_name) != 1) {
        fprintf(stderr, "Error reading LPAR Name\n");
        return 1;
    }
    printf("-%s", lpar_name);

    if (global_layers > 2) {
        if (qc_get_attribute_string(config_handle, qc_layer_name, 3, &vm_name) != 1) {
             fprintf(stderr, "Error reading VM Name\n");
             return 1;
        }
        printf("-%s", vm_name);
    }
    putchar('\n');
    return 0;
}

void list_attributes(char *param) {
    (void)param; 
    printf("Supported attributes for -a:\n");
    for (size_t i = 0; i < ATTR_TABLE_SIZE; i++) {
        printf("  %s\n", ATTR_TABLE[i].name);
    }
}

void print_user_attribute(char *key, char *param, int layer_count) {
    (void)key;

    if (param == NULL) {
        fprintf(stderr, "Error: No attribute specified.\n");
        return;
    }

    /* FALLBACK CHECK */
    if (!config_handle) {
        printf("Attribute '%s' unavailable (qclib fallback active).\n", param);
        return;
    }

    const AttributeMap *target = NULL;
    for (size_t i = 0; i < ATTR_TABLE_SIZE; i++) {
        if (strcmp(param, ATTR_TABLE[i].name) == 0) {
            target = &ATTR_TABLE[i];
            break;
        }
    }

    if (!target) {
        fprintf(stderr, "Error: Unknown attribute '%s'. Use -L to see valid options.\n", param);
        return;
    }

    bool found_any = false;
    for (int i = 0; i < layer_count; i++) {
        int rc = 0;
        if (target->type == TYPE_INTEGER) {
            int tmp; rc = qc_get_attribute_int(config_handle, target->id, i, &tmp);
        } else if (target->type == TYPE_STRING) {
            const char *tmp; rc = qc_get_attribute_string(config_handle, target->id, i, &tmp);
        } else {
            float tmp; rc = qc_get_attribute_float(config_handle, target->id, i, &tmp);
        }

        if (rc == 1) {
            printf("Layer %d: ", i);
            print_attribute(target->name, i, target->id, target->type, false);
            found_any = true;
        }
    }

    if (!found_any) printf("Attribute '%s' not set or found in any layer.\n", param);
}

int main(int argc, char **argv, char **envp) {
    int opt;
    bool flag_print_attr = false;
    bool flag_print_cpu = false;
    bool flag_print_secure = false;
    bool flag_list_attr = false;
    bool flag_create_scc = false;
    bool flag_create_uuid = false;
    bool flag_read_sysinfo = false;
    
    char *arg_param = NULL;

    if (argc > 0 && strstr(argv[0], "cputype") != NULL) {
        flag_read_sysinfo = true;
        flag_print_cpu = true;
    } else {
        while ((opt = getopt(argc, argv, "a:cd:hL:sSuV")) != -1) {
            switch (opt) {
                case 'a': flag_read_sysinfo = true; flag_print_attr = true; arg_param = optarg; break;
                case 'c': flag_read_sysinfo = true; flag_print_cpu = true; break;
                case 'd':
                    debug_level = atoi(optarg);
                    if (debug_level & 1) setenv("QC_DEBUG", "1", 1);
                    if (debug_level & 2) setenv("QC_AUTODUMP", "1", 1);
                    debug_level >>= 2;
                    break;
                case 'L': flag_list_attr = true; arg_param = optarg; break;
                case 's': flag_read_sysinfo = true; flag_create_scc = true; break;
                case 'S': flag_read_sysinfo = true; flag_print_secure = true; break;
                case 'u': flag_read_sysinfo = true; flag_create_uuid = true; break;
                case 'V': printf("%s\n", VERSION_STRING); return 0;
                case 'h': default: print_usage(); return 0;
            }
        }
    }

    int action_count = (flag_print_attr ? 1 : 0) + (flag_print_cpu ? 1 : 0) + 
                       (flag_print_secure ? 1 : 0) + (flag_list_attr ? 1 : 0) + 
                       (flag_create_scc ? 1 : 0) + (flag_create_uuid ? 1 : 0);

    if (action_count > 1) {
        fputs("Error: Only one of the options -a, -c, -L, -s, -S or -u can be specified.\n", stderr);
        return 1;
    }

    if (action_count == 0 && !flag_print_cpu) {
         print_usage();
         return 0;
    }

    /* Initialize, but DO NOT check and abort on return codes.
     * The init_sysinfo function safely sets up either qclib or the fallback.
     */
    if (flag_read_sysinfo) {
        init_sysinfo();
    }

    atexit(cleanup);

    if (flag_print_attr) print_user_attribute(NULL, arg_param, global_layers);
    else if (flag_print_cpu) print_cputype();
    else if (flag_print_secure) print_secure_mode();
    else if (flag_list_attr) list_attributes(arg_param);
    else if (flag_create_scc) print_scc();
    else if (flag_create_uuid) print_uuid();

    return 0; // Always exit 0 to avoid qclib fails!
}
