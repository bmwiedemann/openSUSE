#
# spec file for package perf
#
# Copyright (c) 2020 SUSE LLC
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


# a bug in dwz leaves temporary trace-*.debug.#dwz#.* on 64 bits in place
# remove this once fixed, see:
# https://sourceware.org/bugzilla/show_bug.cgi?id=26645
%define _find_debuginfo_dwz_opts %{nil}
# perf does not link with LTO
%define _lto_cflags %{nil}
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
%ifarch s390x s390
%define         _perf_unwind NO_LIBUNWIND=1
%else
%define         _perf_unwind %{nil}
BuildRequires:  libunwind-devel
%endif
Name:           perf
Version:        %{version}
Release:        0
Summary:        Performance Monitoring Tools for Linux
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            https://perf.wiki.kernel.org/
Patch0:         0001-perf-fix-off-by-ones-in-memset-after-realloc.patch
BuildRequires:  OpenCSD-devel
BuildRequires:  audit-devel
%ifnarch %{arm}
BuildRequires:  babeltrace-devel
%endif
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gtk2-devel
BuildRequires:  kernel-source >= 2.6.31
BuildRequires:  libcap-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  newt-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  rubygem(asciidoctor)
Requires:       kernel >= 2.6.31
%{perl_requires}
%{?libperl_requires}
%ifarch aarch64 ia64 x86_64 ppc64 ppc64le ppc %sparc
BuildRequires:  libnuma-devel
%endif

%description
This package provides a userspace tool 'perf', which monitors performance for
either unmodified binaries or the entire system. It requires a Linux kernel
which includes the Performance Counters for Linux (PCL) subsystem (>= 2.6.31).
This subsystem utilizes the Performance Monitoring Unit (PMU) / hardware
counters of the underlying cpu architecture (if supported).

%prep
# copy necessary files from kernel-source since we need to modify them
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} lib) | tar -xf -
chmod +x tools/perf/util/generate-cmdlist.sh

# don't error out on deprecated definitions in gtk2.h
sed -i 's@ignored "-Wstrict-prototypes"@&\n#pragma GCC diagnostic ignored "-Wdeprecated-declarations"@' tools/build/feature/test-gtk2.c

%autopatch -p1

%build
cd tools/perf
export WERROR=0
# PASS rpm optflags as EXTRA_FLAGS, passing as CFLAGS overrides and breaks build
make %{?_smp_mflags} -f Makefile.perf PYTHON=python3 \
	EXTRA_CFLAGS="%{optflags}" \
	ASCIIDOC8=1 USE_ASCIIDOCTOR=1 CORESIGHT=1 \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	perfexecdir=lib/%{name}-core \
	tipdir=share/doc/packages/perf \
	%{_perf_unwind} \
	all doc

%install
cd tools/perf
export WERROR=0
make -f Makefile.perf V=1 PYTHON=python3 EXTRA_CFLAGS="%{optflags}" \
	ASCIIDOC8=1 USE_ASCIIDOCTOR=1 CORESIGHT=1 \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	perfexecdir=lib/%{name}-core \
	tipdir=share/doc/packages/perf \
	DESTDIR=%{buildroot} \
	%{_perf_unwind} \
	install install-doc

mkdir -p %{buildroot}/%{_docdir}/perf/examples/bpf
mv %{buildroot}%{_prefix}/lib/perf/include/bpf/* %{buildroot}/%{_docdir}/perf/examples/bpf
mv %{buildroot}%{_prefix}/lib/perf/examples/bpf/* %{buildroot}/%{_docdir}/perf/examples/bpf

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/perf %{buildroot}%{_datadir}/bash-completion/completions/

%files
%license COPYING
%doc CREDITS README tools/perf/design.txt
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
%{_prefix}/lib/%{name}-core
%{_datadir}/bash-completion/completions/perf
%{_datadir}/%{name}-core
%{_mandir}/man1/perf*
%dir %{_docdir}/perf/examples
%dir %{_docdir}/perf/examples/bpf
%{_docdir}/perf/examples/bpf/*

%changelog
