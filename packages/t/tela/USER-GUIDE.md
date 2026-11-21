# tela User Guide (openSUSE / SUSE Linux Enterprise)

`tela` is a test execution framework designed for reliable test automation,
dynamic hardware/system resource matching, and TAP13-compliant reporting.
It was developed by the IBM Linux on Z team to support automated validation of
system commands, hardware configurations, and kernel device drivers.

---

## 1. Package Overview

When installed from `build.opensuse.org` via `zypper`, the tela framework is
provided across three packages:

| Package | Contents & Purpose |
| :--- | :--- |
| **`tela`** | Core test runner (`/usr/bin/tela`), Makefile include (`/usr/share/tela/tela.mak`), Bash support library (`tela.bash`), resource discovery scripts (`/usr/lib64/tela/src/libexec`), and system resource templates (`telarc`, `telastate`). |
| **`tela-devel`** | C API header (`/usr/include/tela.h`) and precompiled object files (`$(TELA_OBJ)`) required to build and link C test programs. |
| **`tela-test`** | Ready-to-run sample test suites (`api`, `match`) and architecture-specific test suites (`arch`) tailored to the system architecture. |

### Installation

```bash
# Install core runtime framework
sudo zypper in tela

# Optional: Install C development files if compiling C testcases
sudo zypper in tela-devel

# Optional: Install sample test suites and architecture tests
sudo zypper in tela-test
```

---

## 2. Quick Start

### 2.1 Directory Structure

Create a test directory for your project or test suite:

```bash
mkdir -p my-tests
cd my-tests
```

### 2.2 Create a Makefile

Create a `Makefile` that includes the installed `tela.mak`:

```makefile
# Include the system-wide tela framework definitions
include /usr/share/tela/tela.mak

# List of test programs to execute
TESTS := check_ping.sh test_service.sh
```

### 2.3 Write a Bash Test (`check_ping.sh`)

```bash
#!/bin/bash
# Source the tela Bash library
source $TELA_BASH || exit 1

# Perform your test check
ping -c 1 127.0.0.1 >/dev/null 2>&1
ok $? "localhost_ping"

# Exit with the aggregated test status
exit $(exit_status)
```

Make the script executable:

```bash
chmod +x check_ping.sh
```

### 2.4 Execute Tests

Run tests using GNU Make:

```bash
make check
```

Expected output:

```text
Running 1 tests
(1/1) check_ping.sh:localhost_ping ... [pass]
1 tests executed, 1 passed, 0 failed, 0 skipped
Result log stored in /path/to/my-tests/test.log
```

---

## 3. Writing Tests

### 3.1 Bash Test Cases

Include `source $TELA_BASH || exit 1` at the beginning of your script. The
following functions are available:

- `ok <rc> <name>`: Record test result (passes if `<rc>` is 0, fails otherwise).
- `pass <name>`: Record a passing test case.
- `fail <name>`: Record a failing test case.
- `skip <name> <reason>`: Record a skipped test case.
- `todo <name> <reason>`: Record a planned/work-in-progress test case.
- `diag "<message>"`: Write diagnostic comments into the test log.
- `yaml "<yaml_data>"`: Attach structured YAML diagnostics.
- `exit $(exit_status)`: Exit with status code `0` if all tests passed, `1` if any failed.

Example:

```bash
#!/bin/bash
source $TELA_BASH || exit 1

if [ -f /etc/os-release ]; then
    pass "os_release_exists"
else
    fail "os_release_exists"
fi

skip "external_api" "Network access not configured"

exit $(exit_status)
```

### 3.2 C Test Cases

To compile and run C test programs, ensure `tela-devel` is installed:

```bash
sudo zypper in tela-devel
```

Create `test_demo.c`:

```c
#include <stdio.h>
#include <tela.h>

int main(int argc, char *argv[])
{
    /* Announce planned number of tests (optional) */
    plan(2);

    /* Testcase 1 */
    ok(1 == 1, "basic_arithmetic");

    /* Testcase 2 with diagnostic comment */
    diag("Verifying pointer allocation");
    void *ptr = malloc(1024);
    ok(ptr != NULL, "memory_allocation");
    free(ptr);

    /* Return aggregate test exit status */
    return exit_status();
}
```

In your `Makefile`, reference `$(TELA_OBJ)`:

```makefile
include /usr/share/tela/tela.mak

TESTS := test_demo

test_demo: test_demo.c $(TELA_OBJ)
```

Run `make check` to build and execute.

---

## 4. Hardware and System Resource Matching

tela supports **dynamic resource matching**, allowing test cases to state
hardware or software requirements in sidecar YAML files (`<test>.yaml`).

### 4.1 Resource Definition (`.telarc`)

The resource configuration file defines what hardware and system resources
are available on the testbed. By default, tela checks `~/.telarc` or `$TELA_RC`.

You can inspect the pre-generated template installed with the package:

```bash
cat /usr/share/tela/telarc
```

Or generate a fresh `.telarc` discovering your current system resources:

```bash
make -f /usr/share/tela/tela.mak telarc > ~/.telarc
```

To view the current resolved state of your system resources:

```bash
make -f /usr/share/tela/tela.mak telastate
```

### 4.2 Specifying Test Requirements

Create a YAML file alongside your test script matching its filename
(e.g., `check_arch.sh` and `check_arch.sh.yaml`).

#### Example: Architecture Requirement

`check_arch.sh.yaml`:
```yaml
system:
  arch: x86_64
```

`check_arch.sh`:
```bash
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Validated CPU architecture: $TELA_SYSTEM_ARCH"
ok 0 "cpu_arch_check"
exit $(exit_status)
```

If run on an `x86_64` system, the test runs and passes.
If run on an `s390x` or `aarch64` system, tela automatically skips the test:
```text
(1/1) check_arch.sh ......... [skip] Missing arch: x86_64
```

#### Example: Specific Hardware Devices (e.g. PCI, Storage, Network)

`test_storage.sh.yaml`:
```yaml
system:
  virtio-scsi-lun disk:
    size: >=10000000000
```

When matched, tela exposes the allocated resource attributes as environment variables:
`$TELA_SYSTEM_VIRTIO_SCSI_LUN_DISK_DEV`
`$TELA_SYSTEM_VIRTIO_SCSI_LUN_DISK_SIZE`

### 4.3 IBM Z / s390x Specific Resources

On IBM Z (`s390x`), tela discovers and matches s390-specific subsystems:
- **`dasd`**: Direct Access Storage Devices (ECKD/FBA)
- **`qeth`**: OSA-Express and HiperSockets network interfaces
- **`apqn`**: Crypto Express adapters (CEX, CCA, EP11)
- **`zfcp-host` / `zfcp-lun`**: Fibre Channel over SCSI host adapters and LUNs
- **`dcss`**: Discontiguous Saved Segments
- **`chpid`**: Channel path identifiers and topology
- **`scm`**: Storage-Class Memory (Flash Express)
- **`tape`**: Channel-attached tape drives

Example `dasd_test.sh.yaml`:
```yaml
system:
  dasd disk:
    use: 1
    allow_write: 1
```

---

## 4.4 Recommendations for "Disruptive" Commands in tela

Several IBM Z hardware commands perform operations that can alter system
state, disrupt I/O, reformat storage, take channel paths offline, or reboot
the system.

### Classification of Disruptive Commands

| Category | Commands | Potential Impact |
| :--- | :--- | :--- |
| **Destructive Storage Formatting** | `dasdfmt`, `fdasd` | Low-level formatting or repartitioning permanently destroys data on target volumes. |
| **I/O Exclusion & Device Detachment** | `chzdev -d`, `chccwdev -d`, `cio_ignore` | Disabling active devices can cause immediate loss of network or storage access. |
| **Channel Path Manipulation** | `chchp -c 0` | Taking channel paths offline can degrade or sever I/O multipath connectivity. |
| **Boot & IPL Configuration** | `zipl`, `chreipl` | Overwriting the boot record or changing the IPL device can make the system unbootable. |
| **Shutdown & Panic Action Control** | `chshut` | Alters system behavior on panics or halt signals. |
| **Dynamic CPU/Memory Unplugging** | `cpuplugd`, `zpcictl` | Removing online CPUs or resetting PCI functions may cause performance drops or driver resets. |

### Architectural Best Practices & Recommendations

1. **Explicit Resource Tagging in `.telarc` (`allow_write: 1`)**:
   Never allow disruptive tests to match against generic or unverified devices.
   In your `.telarc`, tag test devices explicitly:
   ```yaml
   system localhost:
     dasd 0.0.1234:
       use: 1
       allow_write: 1  # Crucial: explicitly indicates safe-to-format disk
     qeth 0.0.0900:
       use: 1          # Spare interface; do NOT tag the management interface (0.0.0800)
   ```
   In the test requirement sidecar (`.yaml`), explicitly require `allow_write: 1`.

2. **State Preservation & Restoration using Bash Traps (`trap ... EXIT`)**:
   Always record initial settings and register a cleanup function:
   ```bash
   ORIG_STATE=$(chshut | grep on_panic)
   cleanup() {
       # Restore initial state on normal exit, error, or signal
       chshut on_panic "$ORIG_STATE" >/dev/null 2>&1
   }
   trap cleanup EXIT
   ```

3. **Execution Gating via Test Scope (`TELA_SCOPE` or Environment Flags)**:
   Gate disruptive tests so that standard `make check` runs quickly and safely:
   ```bash
   if [[ "$TELA_SCOPE" != "full" && "$TELA_DISRUPTIVE" != "1" ]]; then
       skip "dasdfmt_destructive" "Set TELA_DISRUPTIVE=1 or SCOPE=full to run"
   fi
   ```

4. **Prefer Non-Destructive / Dry-Run Alternatives**:
   - `dasdfmt`: Use `dasdfmt -c <device>` (check formatting) instead of destructive formatting.
   - `zipl`: Use `zipl --dry-run` or write to a staging image file rather than `/dev/dasda`.
   - `cio_ignore`: Use `cio_ignore -k` (temporary kernel list) and inspect output rather than blacklisting active channel paths.

5. **Testbed Isolation**:
   Run destructive suites on dedicated test LPARs or z/VM guest virtual machines
   with virtual minidisks, never on production hypervisors.

---

## 5. IBM Z Commands Reference & Examples

This section provides sample implementations for commands documented in the
[IBM Z Command Reference](https://www.ibm.com/docs/en/linux-on-systems?topic=reference-commands-linuxonibm-z).

### 5.1 DASD Management (`lsdasd`, `dasdfmt`, `fdasd`, `dasdview`, `tunedasd`, `dasdstat`, `zdsfs`)

#### Requirement: `test_dasd.sh.yaml`
```yaml
system:
  arch: s390x
  dasd disk:
    use: 1
    allow_write: 1
    type: "ECKD"
    size: ">=1000000000"
```

#### Test: `test_dasd.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

DASD_ID="$TELA_SYSTEM_DASD_DISK_ID"
DASD_DEV="$TELA_SYSTEM_DASD_DISK_DEV"

# 1. Query status with lsdasd
lsdasd -l "$DASD_ID" > "$TELA_TMP/lsdasd.out"
ok $? "lsdasd_query"

# 2. Inspect structure with dasdview
dasdview -i "$DASD_DEV" >/dev/null 2>&1
ok $? "dasdview_info"

# 3. Enable performance statistics with dasdstat
dasdstat -e "$DASD_DEV" >/dev/null 2>&1
ok $? "dasdstat_enable"
dasdstat -d "$DASD_DEV" >/dev/null 2>&1

# 4. Check formatting (non-destructive) or format if authorized
if [[ "$TELA_DISRUPTIVE" == "1" ]]; then
    dasdfmt -y -b 4096 -d cdl "$DASD_DEV" >/dev/null 2>&1
    ok $? "dasdfmt_format"
    printf "n\np\n1\n\n\nw\nq\n" | fdasd "$DASD_DEV" >/dev/null 2>&1
    ok $? "fdasd_partition"
else
    dasdfmt -c "$DASD_DEV" >/dev/null 2>&1
    ok $? "dasdfmt_check"
fi

# 5. Tune low-level settings with tunedasd
tunedasd -cache on "$DASD_DEV" >/dev/null 2>&1
ok $? "tunedasd_cache"

exit $(exit_status)
```

---

### 5.2 Network & QETH (`lsqeth`, `qethconf`, `qetharp`, `qethqoat`, `znetconf`, `hsci`, `osasnmpd`)

#### Requirement: `test_qeth.sh.yaml`
```yaml
system:
  arch: s390x
  qeth net:
    use: 1
    card_type: "OSD_10GIG|OSD_25GIG|OSD_1000|HiperSockets"
```

#### Test: `test_qeth.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

QETH_ID="$TELA_SYSTEM_QETH_NET_ID"

# 1. Query QETH adapter configuration
lsqeth "$QETH_ID" > "$TELA_TMP/lsqeth.out"
ok $? "lsqeth_query"

# 2. Inspect network device configuration with znetconf
znetconf -c > "$TELA_TMP/znetconf.out"
ok $? "znetconf_check"

# 3. Query OSA address table (qethqoat)
IFACE=$(cat "/sys/bus/ccwgroup/drivers/qeth/$QETH_ID/if_name" 2>/dev/null)
if [[ -n "$IFACE" ]]; then
    qethqoat "$IFACE" >/dev/null 2>&1
    ok $? "qethqoat_query"
    qetharp -q "$IFACE" >/dev/null 2>&1
    ok $? "qetharp_query"
fi

# 4. Manage HSCI (HiperSockets Converged Interface)
hsci show >/dev/null 2>&1
ok $? "hsci_show"

exit $(exit_status)
```

---

### 5.3 Device Configuration & Channel Paths (`lschp`, `chchp`, `chpstat`, `lscss`, `chccwdev`, `chzdev`, `lszdev`, `cio_ignore`)

#### Requirement: `test_cio.sh.yaml`
```yaml
system:
  arch: s390x
  chpid chp:
    status: "online"
```

#### Test: `test_cio.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

CHP_ID="$TELA_SYSTEM_CHPID_CHP_ID"

# 1. List channel paths and statistics
lschp -m "$CHP_ID" >/dev/null 2>&1
ok $? "lschp_query"
chpstat "$CHP_ID" >/dev/null 2>&1
ok $? "chpstat_query"

# 2. List subchannels
lscss >/dev/null 2>&1
ok $? "lscss_query"

# 3. Query IBM Z device configurations
lszdev >/dev/null 2>&1
ok $? "lszdev_query"

# 4. Test I/O exclusion list (non-destructive inspection)
cio_ignore -u >/dev/null 2>&1
ok $? "cio_ignore_unignored"

exit $(exit_status)
```

---

### 5.4 Cryptography & CPACF (`lszcrypt`, `zcryptctl`, `zcryptstats`, `chzcrypt`, `cpacfinfo`, `cpacfstats`)

#### Requirement: `test_crypto.sh.yaml`
```yaml
system:
  arch: s390x
  apqn crypto:
    type: "CEX7A|CEX7C|CEX8A|CEX8C"
```

#### Test: `test_crypto.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

APQN_ID="$TELA_SYSTEM_APQN_CRYPTO_ID"

# 1. CPACF facility verification
cpacfinfo > "$TELA_TMP/cpacf.out"
ok $? "cpacfinfo_query"

# 2. CPACF activity statistics
cpacfstats >/dev/null 2>&1
ok $? "cpacfstats_query"

# 3. Crypto Express device query
lszcrypt -V "$APQN_ID" >/dev/null 2>&1
ok $? "lszcrypt_device"

# 4. AP queue control and statistics
zcryptctl status >/dev/null 2>&1
ok $? "zcryptctl_status"
zcryptstats >/dev/null 2>&1
ok $? "zcryptstats_query"

exit $(exit_status)
```

---

### 5.5 Shared Memory Communications (`smcd`, `smcr`, `smcss`, `smc_chk`, `smc_pnet`, `smc_rnics`, `smc_run`)

#### Requirement: `test_smc.sh.yaml`
```yaml
system:
  arch: s390x
```

#### Test: `test_smc.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Inspect SMC-D and SMC-R link groups
smcd device >/dev/null 2>&1
ok $? "smcd_devices"
smcr linkgroup >/dev/null 2>&1
ok $? "smcr_linkgroups"
smcss >/dev/null 2>&1
ok $? "smcss_sockets"

# 2. Validate SMC environment
smc_chk >/dev/null 2>&1
ok $? "smc_chk_validate"
smc_rnics >/dev/null 2>&1
ok $? "smc_rnics_list"

exit $(exit_status)
```

---

### 5.6 Telemetry, CPU Performance & Topology (`chcpumf`, `lscpumf`, `lshwc`, `lspai`, `pai`, `lsstp`, `zmemtopo`, `zpwr`, `hyptop`, `opticsmon`)

#### Requirement: `test_telemetry.sh.yaml`
```yaml
system:
  arch: s390x
```

#### Test: `test_telemetry.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. CPU-Measurement Facilities
lscpumf > "$TELA_TMP/cpumf.out" 2>&1
ok $? "lscpumf_info"
lshwc >/dev/null 2>&1
ok $? "lshwc_counters"

# 2. Processor Activity Instrumentation (PAI)
lspai >/dev/null 2>&1
ok $? "lspai_info"

# 3. Server Time Protocol (STP) and Memory Topology
lsstp >/dev/null 2>&1
ok $? "lsstp_query"
zmemtopo >/dev/null 2>&1
ok $? "zmemtopo_query"

# 4. Energy & power metrics
zpwr >/dev/null 2>&1
ok $? "zpwr_power_readings"

exit $(exit_status)
```

---

### 5.7 Virtualization & z/VM Management (`vmcp`, `vmur`, `cmsfs-fuse`, `hmcdrvfs`, `lshmc`, `mon_fsstatd`, `mon_procd`)

#### Requirement: `test_zvm.sh.yaml`
```yaml
system:
  arch: s390x
  hypervisor:
    type: zvm
```

#### Test: `test_zvm.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Issue non-disruptive query via CP interface
vmcp "QUERY CPLEVEL" > "$TELA_TMP/cplevel.out"
ok $? "vmcp_query_cplevel"

# 2. Query z/VM virtual unit record spool queue
vmur li >/dev/null 2>&1
ok $? "vmur_list_spool"

# 3. HMC media drive inspection
lshmc >/dev/null 2>&1
ok $? "lshmc_query"

exit $(exit_status)
```

---

### 5.8 FCP, SCSI, LUNs & Tape (`lstape`, `lsluns`, `lszfcp`, `lsscm`, `scsi_logging_level`)

#### Requirement: `test_storage_subsystems.sh.yaml`
```yaml
system:
  arch: s390x
```

#### Test: `test_storage_subsystems.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. List attached LUNs and FCP adapters
lsluns >/dev/null 2>&1
ok $? "lsluns_query"
lszfcp >/dev/null 2>&1
ok $? "lszfcp_query"

# 2. Query Storage-Class Memory (Flash Express)
lsscm >/dev/null 2>&1
ok $? "lsscm_query"

# 3. Query channel-attached tape drives
lstape >/dev/null 2>&1
ok $? "lstape_query"

# 4. Read SCSI logging level
scsi_logging_level -g >/dev/null 2>&1
ok $? "scsi_logging_level_get"

exit $(exit_status)
```

---

### 5.9 Dynamic Reconfiguration & Hardware Control (`zpcictl`, `cpuplugd`)

#### Requirement: `test_hardware_ctl.sh.yaml`
```yaml
system:
  arch: s390x
```

#### Test: `test_hardware_ctl.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Query cpuplugd daemon configuration syntax
if [ -f /etc/cpuplugd.conf ]; then
    cpuplugd -c -f /etc/cpuplugd.conf >/dev/null 2>&1
    ok $? "cpuplugd_conf_check"
else
    skip "cpuplugd_conf_check" "No /etc/cpuplugd.conf file"
fi

# 2. Inspect PCI functions status with zpcictl
if [[ -n "$TELA_SYSTEM_PCI_DEV_ID" ]]; then
    zpcictl --status "$TELA_SYSTEM_PCI_DEV_ID" >/dev/null 2>&1
    ok $? "zpcictl_status"
else
    skip "zpcictl_status" "No PCI function allocated"
fi

exit $(exit_status)
```

---

### 5.10 System Boot & Shutdown (`lsreipl`, `chreipl`, `lsshut`, `chshut`)

#### Requirement: `test_reipl_shut.sh.yaml`
```yaml
system:
  arch: s390x
```

#### Test: `test_reipl_shut.sh`
```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Inspect re-IPL and shutdown actions
lsreipl > "$TELA_TMP/reipl.out"
ok $? "lsreipl_query"
lsshut > "$TELA_TMP/shut.out"
ok $? "lsshut_query"

# 2. Safe non-destructive modification of shutdown action
ORIG_PANIC=$(grep "on_panic" "$TELA_TMP/shut.out" | awk '{print $2}')
cleanup() {
    chshut on_panic "$ORIG_PANIC" >/dev/null 2>&1
}
trap cleanup EXIT

chshut on_panic stop >/dev/null 2>&1
ok $? "chshut_set_stop"
grep -q "on_panic.*stop" <(lsshut)
ok $? "chshut_verified"

exit $(exit_status)
```

---

## 5.11 Commands Described Elsewhere

Commands documented in specialized companion guides:

### A. Bootloader: `zipl` & `zipl-editenv`

- **Purpose**: Installs the Initial Program Loader boot records onto DASD or SCSI disks.
- **Disruptive Risk**: High. Modifying boot records on active system disks can prevent booting.
- **Safeguard**: Always use `--dry-run` or target a designated non-boot test volume.

```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Query zipl configuration syntax without touching boot sectors
zipl --dry-run > "$TELA_TMP/zipl_dryrun.out" 2>&1
ok $? "zipl_dry_run"

# 2. Inspect zipl environment block
zipl-editenv list >/dev/null 2>&1
ok $? "zipl_editenv_list"

exit $(exit_status)
```

### B. Cryptographic Acceleration: `libica` (`icainfo`, `icastats`)

- **Purpose**: Displays supported symmetric/asymmetric algorithms accelerated by CPACF and Crypto Express cards.
- **Disruptive Risk**: None (read-only diagnostic).

```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Query hardware cipher support
icainfo > "$TELA_TMP/icainfo.out" 2>&1
ok $? "icainfo_query"
grep -q "Hardware support:" "$TELA_TMP/icainfo.out"
ok $? "icainfo_hw_accelerated"

# 2. Query cryptographic operation counters
icastats >/dev/null 2>&1
ok $? "icastats_query"

exit $(exit_status)
```

### C. Secure Key Volume Encryption: `zkey` & `zkey-cryptsetup`

- **Purpose**: Generates and manages XTS and CBC secure keys protected by the Master Key of a Crypto Express coprocessor.
- **Disruptive Risk**: Medium (creating volumes alters disk partitions).
- **Safeguard**: Test key repository management in isolated temporary directories.

```bash
#!/bin/bash
source $TELA_BASH || exit 1

KEY_DIR="$TELA_TMP/keyrepo"
mkdir -p "$KEY_DIR"

# 1. Validate zkey repository operations
zkey validate --key-dir "$KEY_DIR" >/dev/null 2>&1
ok $? "zkey_validate_repo"

# 2. Generate a secure AES-XTS key in temporary directory (requires CCA APQN)
if [[ -n "$TELA_SYSTEM_APQN_CRYPTO_ID" ]]; then
    zkey generate "$KEY_DIR/test.key" --key-type XTS --key-bits 256 >/dev/null 2>&1
    ok $? "zkey_generate"
fi

exit $(exit_status)
```

### D. IBM Secure Execution for Linux: `pvimg` & `pvattest`

- **Purpose**: Builds and verifies encrypted, ultravisor-protected KVM guest images.
- **Disruptive Risk**: None for creation and verification.
- **Safeguard**: Query host key availability and validate certificate chains without executing untrusted guests.

```bash
#!/bin/bash
source $TELA_BASH || exit 1

# 1. Check if Ultravisor and Secure Execution are supported
if [ -d /sys/firmware/uv ]; then
    pass "ultravisor_sysfs_present"
    
    # 2. Test attestation tool availability
    pvattest --help >/dev/null 2>&1
    ok $? "pvattest_tool"
else
    skip "secure_execution" "IBM Secure Execution (Ultravisor) not supported by host firmware"
fi

exit $(exit_status)
```

---

## 6. Running the Pre-Packaged Sample Tests (`tela-test`)

If `tela-test` is installed, full sample test suites and architecture-specific
tests are located in `/usr/share/tela/tests/`:

```bash
cd /usr/share/tela/tests

# Run the architecture-specific tests for this machine
cd arch
make check

# Run the dynamic resource matching sample suite
cd ../match
make check

# Run the complete framework test suite
cd ../suite
make check
```

### 6.1 IBM Z / s390x Sample Test Suite (`tela-s390x-tests.tar.gz`)

For IBM Z / s390x systems, a pre-packaged, non-destructive sample test suite archive
is provided with the `tela-test` package at:
`/usr/share/tela/tests/tela-s390x-tests.tar.gz`

This archive contains verified, production-grade test cases demonstrating non-destructive
resource matching and TAP13 reporting on IBM Z:
- `test_crypto_ha.sh`: Dual-card Crypto Express high availability and redundancy validation
  on shared domains.
- `test_dasd_status.sh`: Non-destructive DASD status and swap volume inspection, confirming
  Re-IPL target protection and Linux swap partition state.
- `test_qeth_secondary.sh`: Secondary network adapter configuration and operational link
  inspection, leaving the primary management network untouched.
- `test_crypto_apqn.sh`: Crypto Express coprocessor (CEX >= 5) and CPACF hardware cipher
  acceleration validation via `libica`.
- `test_zvm_guest.sh`: IBM z/VM hypervisor virtualization, CP interface (`vmcp`), ECKD minidisk,
  Virt.NIC QDIO network interface, and channel path inspection.
- `test_kvm_guest.sh`: Linux on Z KVM guest environment, virtual CPU topology, VirtIO SCSI CCW
  bus attachment, and firmware IPL facilities.

#### How to Extract and Use the Sample Suite:

1. **Extract the archive to your desired test directory:**
   ```bash
   tar -zxvf /usr/share/tela/tests/tela-s390x-tests.tar.gz
   cd s390x-tests
   ```

2. **Simulation Mode (runs on any host, including x86_64, using simulated or captured s390x resources):**
   ```bash
   # Run against default mock profile:
   ./run_tests.sh mock

   # Run against specific hypervisor profiles:
   ./run_tests.sh mock lpar    # IBM Z bare-metal LPAR partition state
   ./run_tests.sh mock zvm     # IBM z/VM hypervisor guest state
   ./run_tests.sh mock kvm     # Linux on Z KVM guest state

   # Run multi-hypervisor matrix comparison across all profiles:
   ./run_tests.sh mock all
   ```

3. **Dry-Run Resource Matching (shows resolved TELA_SYSTEM_* environment variables):**
   ```bash
   # Dry-run for a specific hypervisor:
   ./run_tests.sh match lpar
   ./run_tests.sh match zvm
   ./run_tests.sh match kvm

   # Dry-run for all hypervisor profiles:
   ./run_tests.sh match all
   ```

4. **Live Execution on Target IBM Z Hardware:**
   ```bash
   # Deploy the hardware inventory definition matching your hypervisor:
   cp telarc.lpar ~/.telarc   # on bare-metal LPAR
   # or: cp telarc.zvm ~/.telarc    # on z/VM guest
   # or: cp telarc.kvm ~/.telarc    # on KVM guest

   # Execute the entire suite via GNU Make:
   make check

   # Or run an individual test:
   make check TESTS=test_dasd_status.sh

   # Or run via the runner helper:
   ./run_tests.sh live [lpar|zvm|kvm]
   ```

---

## 7. CLI Command Reference (`tela`)

The `tela` executable (`/usr/bin/tela`) provides direct CLI utilities:

- **`tela run <test_program>`**: Run a single test program and monitor output.
- **`tela match <req_file> <res_file>`**: Match requirements against a resource file.
- **`tela monitor <cmd>`**: Monitor and format test execution in real time.
- **`tela format`**: Format TAP13 input stream into human-readable console output.
- **`tela count <test_programs...>`**: Count total number of sub-tests in test files.
- **`tela eval <expr>`**: Evaluate boolean/arithmetic expressions used in YAML.
- **`tela yamlget <file> <key>`**: Query and extract values from YAML test files.

---

## 8. Additional Documentation

Comprehensive upstream documentation is installed under:
`/usr/share/doc/packages/tela/doc/`

Key documents:
- `doc/writing_tests.md`: Guide to writing advanced tests and TAP13 logging.
- `doc/resources.md`: Complete reference on tela resources and matching syntax.
- `doc/functions.md`: Full reference for tela C and Bash functions.
- `doc/environment.md`: Environment variables exported by the framework.
- `doc/yaml.md`: Specification of YAML requirement syntax and operators.
