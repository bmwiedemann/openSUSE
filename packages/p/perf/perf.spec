#
# spec file for package perf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perf
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        Performance Monitoring Tools for Linux
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
Url:            https://perf.wiki.kernel.org/
BuildRequires:  audit-devel
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gtk2-devel
BuildRequires:  kernel-source >= 2.6.31
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  xz-devel
BuildRequires:  rubygem(asciidoctor)
%ifarch aarch64 ia64 x86_64 ppc64 ppc64le ppc %sparc
BuildRequires:  libnuma-devel
%endif
%ifarch s390x s390
%define         _perf_unwind NO_LIBUNWIND=1
%else
%define         _perf_unwind %{nil}
BuildRequires:  libunwind-devel
%endif
BuildRequires:  newt-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
# dl_open requirement so not autodetected
%ifarch ppc64 ppc64le
Requires:       libebl
%endif
%{perl_requires}
%{?libperl_requires}

Requires:       kernel >= 2.6.31
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a userspace tool 'perf', which monitors performance for
either unmodified binaries or the entire system. It requires a Linux kernel
which includes the Performance Counters for Linux (PCL) subsystem (>= 2.6.31).
This subsystem utilizes the Performance Monitoring Unit (PMU) / hardware
counters of the underlying cpu architecture (if supported).

%prep
# copy necessary files from kernel-source since we need to modify them
(cd /usr/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} lib) | tar -xf - 
chmod +x tools/perf/util/generate-cmdlist.sh

%build
cd tools/perf
export WERROR=0
# PASS rpm optflags as EXTRA_FLAGS,  passing as CFLAGS overrides and breaks build
make %{?_smp_mflags} -f Makefile.perf PYTHON=python3 EXTRA_CFLAGS="%{optflags}" ASCIIDOC8=1 prefix=/usr libdir=%{_libdir} perfexecdir=lib/%{name}-core all doc %{_perf_unwind} tipdir=share/doc/packages/perf USE_ASCIIDOCTOR=1

%install
cd tools/perf
export WERROR=0
make -f Makefile.perf V=1 PYTHON=python3 EXTRA_CFLAGS="%{optflags}" prefix=/usr libdir=%{_libdir} perfexecdir=lib/%{name}-core DESTDIR=%{buildroot} install install-doc %{_perf_unwind} tipdir=share/doc/packages/perf USE_ASCIIDOCTOR=1
mkdir -p %{buildroot}/%{_docdir}/perf/examples/bpf
mv %{buildroot}/usr/lib/perf/include/bpf/* %{buildroot}/%{_docdir}/perf/examples/bpf
mv %{buildroot}/usr/lib/perf/examples/bpf/* %{buildroot}/%{_docdir}/perf/examples/bpf

%files
%defattr(-, root, root)
%attr(0644, root, root) %doc COPYING CREDITS README tools/perf/design.txt
%if 0%{?suse_version} > 1315
%attr(0644, root, root) %doc %{_docdir}/perf/tips.txt
%endif
%{_bindir}/perf
%{_bindir}/trace
%{_libdir}/libperf-gtk.so
%ifnarch armv7l
%dir %{_libdir}/traceevent
%dir %{_libdir}/traceevent/plugins
%{_libdir}/traceevent/plugins/plugin_*.so
%endif
%attr(0644, -, -) %{_sysconfdir}/bash_completion.d/perf
%{_libexecdir}/%{name}-core
%{_datarootdir}/%{name}-core
%{_mandir}/man1/perf*
%dir %{_docdir}/perf
%dir %{_docdir}/perf/examples
%dir %{_docdir}/perf/examples/bpf
%{_docdir}/perf/examples/bpf/*

%changelog
