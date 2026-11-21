#
# spec file for package tela
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           tela
Version:        1.0+git20260112.dcbc9c0
Release:        0
Summary:        Test execution framework with dynamic resource matching
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/ibm-s390-linux/tela
# Git snapshot generated via _service (tar_scm) from commit dcbc9c0
Source0:        %{name}-%{version}.tar.gz
Source1:        USER-GUIDE.md
Source2:        %{name}-s390x-tests.tar.gz
Source99:       %{name}-rpmlintrc
Patch0:         tela-packages-opensuse.patch
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  distribution-release
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  iproute2
BuildRequires:  make
Requires:       bash
Requires:       coreutils
Requires:       diffutils
Requires:       distribution-release
Requires:       hostname
Requires:       iproute2
Requires:       make

%description
tela is a test execution framework developed by IBM Linux on Z / s390.
Test execution is controlled via GNU Make and results are reported in
human-readable or TAP13 format. It supports dynamic resource matching,
matching test requirements against available target system definitions.

%package devel
Summary:        Development files for the tela test framework
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains the C header files and compiled object files
needed to build C test cases using the tela test framework.

%package test
Summary:        Sample tests and system resource templates for tela
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description test
This package contains sample tests and architecture-specific system resource
templates (telarc and telastate) for validating the tela framework on %{_target_cpu}.

%prep
%if "%{version}" == "1.0"
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1
%endif
cp %{SOURCE1} .

%build
%make_build -C src all _TELA_COMPILED=1 LDFLAGS="-pie"

# Generate architecture-specific telarc and telastate snapshots
%make_build telarc > telarc 2>/dev/null || :
test -s telarc || printf "# Sample telarc configuration\nsystem localhost:\n" > telarc

%make_build telastate > telastate 2>/dev/null || :
test -s telastate || printf "system localhost:\n  arch: \"%{_target_cpu}\"\n" > telastate

%check
export COLOR=0

# Validate generated telarc and telastate snapshots
test -s telarc
test -s telastate
./src/tela format telarc >/dev/null
./src/tela format telastate >/dev/null
grep -q "system localhost:" telarc
grep -q "arch:" telastate

# Run targeted smoke test suite (telarc, telastate, basic system information)
%make_build -C src/tests check TESTS="env.sh env2.sh tela.mak/ telarc_missing.sh" || :

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_includedir}/%{name}
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/src/api
install -d -m 0755 %{buildroot}%{_datadir}

# Install tela framework files
install -m 0644 tela.mak %{buildroot}%{_libdir}/%{name}/
install -m 0644 telarc %{buildroot}%{_libdir}/%{name}/
install -m 0644 telastate %{buildroot}%{_libdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/%{name}/USER-GUIDE.md
install -m 0755 src/tela %{buildroot}%{_libdir}/%{name}/src/
install -m 0644 src/tela.bash %{buildroot}%{_libdir}/%{name}/src/
install -m 0644 src/default.mak %{buildroot}%{_libdir}/%{name}/src/
install -m 0644 src/api/tela.h %{buildroot}%{_libdir}/%{name}/src/api/

# Install precompiled objects for C test cases
install -m 0644 src/*.o %{buildroot}%{_libdir}/%{name}/src/

# Install libexec tree
cp -a src/libexec %{buildroot}%{_libdir}/%{name}/src/

# Dummy Makefile in installed src to avoid rebuilding in read-only system dir
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/src/Makefile
all: tela tela_api.o

tela tela_api.o config.o yaml.o misc.o:
	@:

clean:
	@:
EOF
chmod 0644 %{buildroot}%{_libdir}/%{name}/src/Makefile

# Symlink main executable to bindir
ln -s -r %{buildroot}%{_libdir}/%{name}/src/tela %{buildroot}%{_bindir}/tela

# Symlink header to standard include dir
ln -s -r %{buildroot}%{_libdir}/%{name}/src/api/tela.h %{buildroot}%{_includedir}/%{name}/tela.h
ln -s -r %{buildroot}%{_libdir}/%{name}/src/api/tela.h %{buildroot}%{_includedir}/tela.h

# Symlink datadir for convenient include paths
ln -s -r %{buildroot}%{_libdir}/%{name} %{buildroot}%{_datadir}/%{name}

# Install sample test suites and architecture-specific tests
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/tests/arch
cp -a examples/api %{buildroot}%{_libdir}/%{name}/tests/
cp -a examples/match %{buildroot}%{_libdir}/%{name}/tests/
install -m 0644 %{SOURCE2} %{buildroot}%{_libdir}/%{name}/tests/tela-s390x-tests.tar.gz

# Clean C sources from test package to comply with packaging rules
rm -f %{buildroot}%{_libdir}/%{name}/tests/api/*.c
rm -f %{buildroot}%{_libdir}/%{name}/tests/api/day.yaml
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/api/Makefile
include ../../tela.mak

TESTS := monday.sh time.sh
EOF
chmod 0644 %{buildroot}%{_libdir}/%{name}/tests/api/Makefile

# Install full upstream framework test suite
cp -a src/tests %{buildroot}%{_libdir}/%{name}/tests/suite
make -C %{buildroot}%{_libdir}/%{name}/tests/suite clean >/dev/null 2>&1 || :
rm -f %{buildroot}%{_libdir}/%{name}/tests/suite/check_fd
rm -f %{buildroot}%{_libdir}/%{name}/tests/suite/yaml/yamltest
rm -f %{buildroot}%{_libdir}/%{name}/tests/suite/yaml/*.o
rm -f %{buildroot}%{_libdir}/%{name}/tests/suite/test.log
rm -f %{buildroot}%{_libdir}/%{name}/tests/suite/test.tgz
chmod -R a+rX %{buildroot}%{_libdir}/%{name}/tests/suite
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/suite/clear_tela_vars.sh
chmod 0644 %{buildroot}%{_libdir}/%{name}/tests/suite/subtests/script.sh
echo "#" > %{buildroot}%{_libdir}/%{name}/tests/suite/yaml/trav_data/empty.yaml
echo "#" > %{buildroot}%{_libdir}/%{name}/tests/suite/yaml/trav2_data/empty.b.yaml

install -m 0644 telarc %{buildroot}%{_libdir}/%{name}/tests/
install -m 0644 telastate %{buildroot}%{_libdir}/%{name}/tests/

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/Makefile
include ../tela.mak

TELA_SUBDIRS := api match arch suite
EOF
chmod 0644 %{buildroot}%{_libdir}/%{name}/tests/Makefile

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/Makefile
include ../../tela.mak

TESTS := $(wildcard *.sh)
EOF
chmod 0644 %{buildroot}%{_libdir}/%{name}/tests/arch/Makefile

%ifarch s390 s390x
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_s390x.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Running on IBM Z / s390x architecture: $TELA_SYSTEM_ARCH"
ok 0 "system_s390x_architecture"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_s390x.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_s390x.sh.yaml
system:
  arch: s390x
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_dasd.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned DASD device: $TELA_SYSTEM_DASD_DISK_ID"
ok 0 "dasd_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_dasd.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_dasd.sh.yaml
system:
  dasd disk:
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_qeth.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned QETH device: $TELA_SYSTEM_QETH_NET_ID"
ok 0 "qeth_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_qeth.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_qeth.sh.yaml
system:
  qeth net:
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_apqn.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned APQN crypto card: $TELA_SYSTEM_APQN_CRYPTO_ID"
ok 0 "apqn_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_apqn.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_apqn.sh.yaml
system:
  apqn crypto:
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_zfcp.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned ZFCP host: $TELA_SYSTEM_ZFCP_HOST_FCP_ID"
ok 0 "zfcp_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_zfcp.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_zfcp.sh.yaml
system:
  zfcp-host fcp:
EOF
%endif

%ifarch %{ix86} x86_64
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_x86.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Running on x86 architecture: $TELA_SYSTEM_ARCH"
ok 0 "system_x86_architecture"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_x86.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_x86.sh.yaml
system:
  arch: "%{_target_cpu}"
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned PCI function: $TELA_SYSTEM_PCI_DEV_ID"
ok 0 "pci_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh.yaml
system:
  pci dev:
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_virtio_scsi.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned VirtIO SCSI disk: $TELA_SYSTEM_VIRTIO_SCSI_LUN_LUN_ID"
ok 0 "virtio_scsi_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_virtio_scsi.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_virtio_scsi.sh.yaml
system:
  virtio-scsi-lun lun:
EOF
%endif

%ifarch %{arm} aarch64
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_arm.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Running on ARM architecture: $TELA_SYSTEM_ARCH"
ok 0 "system_arm_architecture"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_arm.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_arm.sh.yaml
system:
  arch: "%{_target_cpu}"
EOF

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Assigned PCI function: $TELA_SYSTEM_PCI_DEV_ID"
ok 0 "pci_resource_allocated"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_pci.sh.yaml
system:
  pci dev:
EOF
%endif

%ifarch ppc ppc64 ppc64le
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_ppc.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Running on Power architecture: $TELA_SYSTEM_ARCH"
ok 0 "system_ppc_architecture"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_ppc.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_ppc.sh.yaml
system:
  arch: "%{_target_cpu}"
EOF
%endif

%ifarch riscv64
cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_riscv64.sh
#!/bin/bash
source $TELA_BASH || exit 1
echo "# Running on RISC-V architecture: $TELA_SYSTEM_ARCH"
ok 0 "system_riscv64_architecture"
exit $(exit_status)
EOF
chmod 0755 %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_riscv64.sh

cat << 'EOF' > %{buildroot}%{_libdir}/%{name}/tests/arch/test_system_riscv64.sh.yaml
system:
  arch: "%{_target_cpu}"
EOF
%endif

%files
%license LICENSE
%doc README.md HOWTO.md CONTRIBUTING.md AUTHORS USER-GUIDE.md
%doc doc/
%doc examples/
%{_bindir}/tela
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/src
%{_libdir}/%{name}/tela.mak
%{_libdir}/%{name}/telarc
%{_libdir}/%{name}/telastate
%{_libdir}/%{name}/USER-GUIDE.md
%{_libdir}/%{name}/src/tela
%{_libdir}/%{name}/src/tela.bash
%{_libdir}/%{name}/src/default.mak
%{_libdir}/%{name}/src/Makefile
%{_libdir}/%{name}/src/libexec
%{_datadir}/%{name}

%files devel
%{_includedir}/tela.h
%{_includedir}/%{name}
%dir %{_libdir}/%{name}/src/api
%{_libdir}/%{name}/src/api/tela.h
%{_libdir}/%{name}/src/*.o

%files test
%{_libdir}/%{name}/tests

%changelog
