#
# spec file for package cpupower
#
# Copyright (c) 2020 SUSE LLC
# Author: Thomas Renninger <trenn@suse.de>
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


# Use this as version when things are in mainline kernel
%define version %(rpm -q --qf '%{VERSION}' kernel-source)

%define tsversion      20.03.20
%define pbversion      17.05.11
%define ssversion      1.3

Name:           cpupower
# Use this as version when things are in mainline kernel
%define version %(rpm -q --qf '%VERSION' kernel-source)
Version:        5.5
Release:        0
Summary:        Tools to determine and set CPU Power related Settings
License:        GPL-2.0-only
Group:          System/Base
URL:            https://git.kernel.org/cgit/linux/kernel/git/rafael/linux-pm.git
Source:         %{name}-%{version}.tar.bz2
Source1:        turbostat-%{tsversion}.tar.bz2
Source2:        cpupower_export_tarball_from_git.sh
Source3:        x86_energy_perf_policy-%{pbversion}.tar.bz2
Source4:        intel-speed-select-%{ssversion}.tar.bz2
Source5:        Makefile.intel-speed-select
Patch1:         cpupower_rapl.patch
Patch2:         rapl_monitor.patch
Patch3:         cpupower_exclude_kernel_Makefile.patch
Patch4:         cpupower-Revert-library-ABI-changes-from-commit-ae2917093fb60bdc1ed3e.patch
Patch5:         Correction-to-manpage-of-cpupower.patch
Patch6:         amd_do_not_show_amount_of_boost_states_if_zero.patch

#turbostat patches
Patch22:        turbostat_makefile_fix_asm_header.patch
Patch23:        remove_bits_h.patch

# x86_energy_perf patches
# Fixes bsc#1048546:
Patch30:        x86_perf_makefile_fix_asm_header.patch

# intel-speed-select patches
Patch50:        intel-speed-select_remove_DATE_TIME.patch

BuildRequires:  gettext-tools
BuildRequires:  libcap-devel
BuildRequires:  pciutils
BuildRequires:  pciutils-devel

%description
This tool accesses the Linux kernel's processor power subsystems
like CPU frequency switching (cpufreq) or CPU sleep states (cpuidle).

%package -n libcpupower0
Summary:        Processor power related C-library
Group:          System/Libraries

%description -n libcpupower0
Contains libcpupower which offers easy functions to access
processor frequency, processor idle, processor power hierarchy
and other CPU power consumption related information.

%package devel
Summary:        Include files for libcpupower
Group:          Development/Languages/C and C++
Requires:       libcpupower0 = %{version}

%description devel
Include files for C/C++ development with libcpupower.

%package bench
Summary:        CPU frequency micro benchmark
Group:          System/Benchmark

%description bench
This benchmark helps to test the condition of a given kernel cpufreq
governor (e.g. ondemand, userspace, conservative) and the cpufreq HW driver
(e.g. powernow-k8, acpi-cpufreq, ...).
For that purpose, it compares the performance governor to a configured
powersave module.

%prep
%setup -q -D -b 1 -b 3 -b 4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

cd ../turbostat-%{tsversion}
%patch22 -p1
%patch23 -p1

cd ../x86_energy_perf_policy-%{pbversion}
%patch30 -p1

cd ../intel-speed-select-%{ssversion}
cp %{SOURCE5} Makefile
%patch50 -p1

%build
CONF="PACKAGE_BUGREPORT=https://bugs.opensuse.org mandir=%{_mandir} libdir=%{_libdir} CPUFRQ_BENCH=true VERSION=%{version}"
export CFLAGS="%{optflags} -fcommon -I ."
make $CONF %{?_smp_mflags}

%ifarch ix86 x86_64
cd ../turbostat-%{tsversion}
export CFLAGS="%{optflags} -fcommon -I ."
make %{?_smp_mflags}
cd ../x86_energy_perf_policy-%{pbversion}
make %{?_smp_mflags}
cd ../intel-speed-select-%{ssversion}
make %{?_smp_mflags}
%endif

%install
CONF="PACKAGE_BUGREPORT=https://bugs.opensuse.org mandir=%{_mandir} libdir=%{_libdir} CPUFRQ_BENCH=true DESTDIR=%{buildroot} sbindir=%{_sbindir} docdir=%{_docdir}/%{name} confdir=%{_sysconfdir} VERSION=%{version}"
%make_install $CONF

# copy to examples doc dir to avoid complains from the build
# system about an executable in the doc dir.
mkdir -p %{buildroot}/%{_docdir}/%{name}/examples
mv %{buildroot}//%{_docdir}/%{name}/cpufreq-bench_script.sh %{buildroot}/%{_docdir}/%{name}/examples

%find_lang %{name}

%ifarch ix86 x86_64
cd ../turbostat-%{tsversion}
%make_install -e
cd ../x86_energy_perf_policy-%{pbversion}
%make_install
cd ../intel-speed-select-%{ssversion}
%make_install
%endif

%post -n libcpupower0 -p /sbin/ldconfig
%postun -n libcpupower0 -p /sbin/ldconfig

%files -f %{name}.lang
%{_datadir}/bash-completion/completions/cpupower
%{_mandir}/man1/cpupower*
%{_bindir}/cpupower
%ifarch ix86 x86_64
%{_mandir}/man8/turbostat*
%{_bindir}/turbostat
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/x86_energy_perf_policy
%{_bindir}/intel-speed-select
%endif

%files bench
%config %{_sysconfdir}/cpufreq-bench.conf
%{_sbindir}/cpufreq-bench
%{_bindir}/cpufreq-bench_plot.sh
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/cpufreq-bench_script.sh
%{_docdir}/%{name}/README-BENCH

%files -n libcpupower0
%{_libdir}/libcpupower*.so.*

%files devel
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h
%{_libdir}/libcpu*.so

%changelog
