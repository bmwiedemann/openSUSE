#
# spec file for package cpupower
#
# Copyright (c) 2023 SUSE LLC
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


%define maindir tools/power/cpupower
%define tsdir tools/power/x86/turbostat
%define pbdir tools/power/x86/x86_energy_perf_policy
%define ssdir tools/power/x86/intel-speed-select
# Use this as version when things are in mainline kernel
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Name:           cpupower
Version:        %{version}
Release:        0
Summary:        Tools to determine and set CPU Power related Settings
License:        GPL-2.0-only
Group:          System/Base
URL:            https://git.kernel.org/cgit/linux/kernel/git/rafael/linux-pm.git
Patch3:         cpupower_exclude_kernel_Makefile.patch
Patch6:         amd_do_not_show_amount_of_boost_states_if_zero.patch
BuildRequires:  gettext-tools
BuildRequires:  kernel-source
BuildRequires:  libcap-devel
BuildRequires:  libnl-devel
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

%package bash-completion
Summary:        Bash completion for cpupower
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
bash command line completion support for cpupower.

%package rebuild
Summary:        Empty package to ensure rebuilding cpupower in OBS
Group:          System/Monitoring
%requires_eq    kernel-source

%description rebuild
This is empty package that ensures cpupower is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%lang_package

%prep
# copy necessary files from kernel-source since we need to modify them
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} lib) | tar -xf -
chmod +x tools/power/cpupower/utils/version-gen.sh
cd %{maindir}
%patch3 -p1
%patch6 -p1

%build
CONF="PACKAGE_BUGREPORT=https://bugs.opensuse.org mandir=%{_mandir} libdir=%{_libdir} CPUFRQ_BENCH=true"
export CFLAGS="%{optflags} -fcommon"
%make_build -C %{maindir} $CONF

%ifarch %{ix86} x86_64
%make_build -C %{tsdir}
%make_build -C %{pbdir}
%make_build -C %{ssdir}
%endif

%install
CONF="PACKAGE_BUGREPORT=https://bugs.opensuse.org mandir=%{_mandir} libdir=%{_libdir} CPUFRQ_BENCH=true DESTDIR=%{buildroot} sbindir=%{_sbindir} docdir=%{_docdir}/%{name} confdir=%{_sysconfdir}"
%make_install -C %{maindir} $CONF

%ifarch %{ix86} x86_64
%make_install -C %{tsdir}
%make_install -C %{pbdir}
%make_install -C %{ssdir}
%endif

# copy to examples doc dir to avoid complains from the build
# system about an executable in the doc dir.
mkdir -p %{buildroot}/%{_docdir}/%{name}/examples
mv %{buildroot}//%{_docdir}/%{name}/cpufreq-bench_script.sh %{buildroot}/%{_docdir}/%{name}/examples

%find_lang %{name}

%post -n libcpupower0 -p /sbin/ldconfig
%postun -n libcpupower0 -p /sbin/ldconfig

%files
%{_mandir}/man1/cpupower*%{?ext_man}
%{_bindir}/cpupower
%ifarch %{ix86} x86_64
%{_mandir}/man8/turbostat*%{?ext_man}
%{_bindir}/turbostat
%{_mandir}/man8/x86_energy_perf_policy*%{?ext_man}
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
%{_includedir}/*.h
%{_libdir}/libcpu*.so

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/cpupower

%files lang -f %{name}.lang

%files rebuild
%license COPYING

%changelog
