#
# spec file for package greenlit
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pythons %{primary_python}
Name:           greenlit
Version:        3.1.1
Release:        0
Summary:        Test framework for Linux distributions on NVIDIA platforms
# Legal-Review-Notice:
# - 14 files are GPL-2.0-only: 7 C sources, 3 shell tests and 2 bpftrace
#   scripts by their SPDX headers, plus the two modules below. They are
#   kernel modules, programs and scripts built or run on the target, never
#   imported by or linked with the Apache-2.0 Python code.
# - src/modules/mm/bingo/bingo.c has an Apache-2.0 header but declares
#   MODULE_LICENSE("GPL"); a trivial pr_info module, counted as GPL-2.0-only.
# - external_tests/mair_el1_war/test_pgprot_api/test_pgprot_api.c has no
#   header; MODULE_LICENSE("GPL") does not say "or later", so GPL-2.0-only.
# - Seven files use the deprecated SPDX id GPL-2.0, read as GPL-2.0-only.
License:        Apache-2.0 AND GPL-2.0-only
URL:            https://github.com/NVIDIA/GreenLiT
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM greenlit-unitdir.patch gh#NVIDIA/GreenLiT#1 martin@pluskal.org -- find the units in /usr/lib/systemd/system
Patch0:         greenlit-unitdir.patch
# PATCH-FIX-OPENSUSE greenlit-ste-test-endianness.patch martin@pluskal.org -- skip a host-byte-order test on big-endian hosts
Patch1:         greenlit-ste-test-endianness.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-PyYAML
Requires:       %{primary_python}-packaging
Requires:       kmod
Requires:       pciutils
Requires:       procps
Requires:       util-linux
Recommends:     (kernel-64kb-devel if kernel-64kb)
Recommends:     (kernel-default-devel if (kernel-default or kernel-default-base))
Recommends:     (kernel-longterm-devel if kernel-longterm)
Recommends:     bpftrace
Recommends:     freeipmi
Recommends:     gcc
Recommends:     i2c-tools
Recommends:     ipmitool
Recommends:     kexec-tools
Recommends:     libgpiod-utils
Recommends:     libvirt-client
Recommends:     libvirt-daemon-qemu
Recommends:     linux-glibc-devel
Recommends:     make
Recommends:     numactl
Recommends:     perf
Recommends:     qemu-arm
Recommends:     stress-ng
Recommends:     sudo
Recommends:     tar
Recommends:     tpm2.0-tools
Suggests:       mokutil
BuildArch:      noarch
%{?systemd_ordering}

%description
GreenLiT is NVIDIA's test framework for Linux distributions on NVIDIA
platforms (Grace, Vera, Tegra, DGX). glt-test-suite runs system-level,
hardware and OS checks grouped into standard, disruptive and stress
test plans.

The suite runs as root. Disruptive tests reboot the machine, kexec into
another kernel or change the kernel command line in the GRUB
configuration. Tests that need kernel modules or helper programs build
them at run time under %{_datadir}/greenlit. The greenlit.service and
greenlit.timer units, which resume a session after a reboot, ship
disabled; the suite enables them itself when a test needs it.

%prep
%autosetup -p1 -n GreenLiT-%{version}

%build
# Nothing to build: test programs are compiled on the target at run time

%install
# The code imports common, modules and scripts as top-level packages, so
# it lives in a private directory instead of site-packages.
install -d %{buildroot}%{_datadir}/%{name}
cp -a src/greenlit src/common src/modules src/scripts %{buildroot}%{_datadir}/%{name}/
install -Dpm 0644 src/bin/smt_aware_wakee.py %{buildroot}%{_datadir}/%{name}/bin/smt_aware_wakee.py
install -Dpm 0644 confs/hardware-manifest.json %{buildroot}%{_datadir}/%{name}/hardware-manifest.json
install -Dpm 0644 -t %{buildroot}%{_datadir}/%{name}/confs.d confs/glt-confs.d/*
install -d %{buildroot}%{_datadir}/%{name}/executing_dir
cp -a external_tests/. %{buildroot}%{_datadir}/%{name}/executing_dir/
sed -i '1s|^#!/usr/bin/env bash$|#!/bin/bash|' \
    %{buildroot}%{_datadir}/%{name}/executing_dir/mair_el1_war/test_mair_el1_war.sh
# Run as "bpftrace <file>" and "python3 <file>", never executed directly
chmod 0644 %{buildroot}%{_datadir}/%{name}/modules/iommu/nested_ste/observe_ste.bt
sed -i '1{/^#!/d}' \
    %{buildroot}%{_datadir}/%{name}/modules/iommu/cmdqv_hyp_own/observe.bt.in \
    %{buildroot}%{_datadir}/%{name}/scripts/check_kernel_patches.py

# A script, not a shell wrapper: the suite stops itself with pkill glt-test-suite
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/glt-test-suite <<EOF
#!%{__python3} %{py3_shbang_opts}
import sys

sys.path.insert(0, "%{_datadir}/%{name}")
from greenlit.greenlit import main

sys.exit(main())
EOF
chmod 0755 %{buildroot}%{_bindir}/glt-test-suite

install -Dpm 0644 -t %{buildroot}%{_unitdir} confs/greenlit.service confs/greenlit.timer

%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode checked-hash -d %{_datadir}/%{name} %{buildroot}%{_datadir}/%{name}
# smt_aware_wakee.py is run as a script
rm -r %{buildroot}%{_datadir}/%{name}/bin/__pycache__
%fdupes %{buildroot}%{_datadir}/%{name}

%check
export PYTHONPATH=$PWD:$PWD/src
%pytest tests
%python_expand PYTHONPATH=%{buildroot}%{_datadir}/%{name} $python -B -c 'import greenlit.greenlit'

%pre
%service_add_pre greenlit.service greenlit.timer

%post
%service_add_post greenlit.service greenlit.timer

%preun
%service_del_preun greenlit.service greenlit.timer

%postun
# A restart would resume the last test session
%service_del_postun_without_restart greenlit.service greenlit.timer

%files
%license LICENSE
%doc README.md docs/reference docs/user-guides
%{_bindir}/glt-test-suite
%{_datadir}/%{name}
%{_unitdir}/greenlit.service
%{_unitdir}/greenlit.timer

%changelog
