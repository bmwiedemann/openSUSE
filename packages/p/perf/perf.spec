#
# spec file for package perf
#
# Copyright (c) 2025 SUSE LLC
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


# perf does not link with LTO
%define _lto_cflags %{nil}
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
%define version_pure %(echo %{version}|sed 's@\\([0-9]*\\)\\.\\([0-9]*\\).*@\\1\\2@')
%ifarch s390x s390
%define         _perf_unwind NO_LIBUNWIND=1
%else
%define         _perf_unwind %{nil}
BuildRequires:  libunwind-devel
%endif
%{?sle15_python_module_pythons}
Name:           perf
Version:        %{version}
Release:        0
Summary:        Performance Monitoring Tools for Linux
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            https://perf.wiki.kernel.org/
BuildRequires:  OpenCSD-devel
BuildRequires:  audit-devel
%ifnarch %{arm}
BuildRequires:  babeltrace-devel
%endif
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  clang
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  kernel-source >= 2.6.31
BuildRequires:  libcap-devel
# Debuginfod integration has major issues: boo#1213785
#BuildRequires:  libdebuginfod-devel
BuildRequires:  libdw-devel
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  libelf-devel
BuildRequires:  libtraceevent-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm
BuildRequires:  newt-devel
BuildRequires:  openssl-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  rubygem(asciidoctor)
%ifarch aarch64 ia64 x86_64 ppc64 ppc64le ppc %sparc
BuildRequires:  libnuma-devel
%endif
Recommends:     kernel >= 2.6.31
Recommends:     perf-gtk
%{perl_requires}
%{?libperl_requires}

%define python_subpackage_only 1
%python_subpackages

%description
This package provides a userspace tool 'perf', which monitors performance for
either unmodified binaries or the entire system. It requires a Linux kernel
which includes the Performance Counters for Linux (PCL) subsystem (>= 2.6.31).
This subsystem utilizes the Performance Monitoring Unit (PMU) / hardware
counters of the underlying cpu architecture (if supported).

%package gtk
Summary:        Gtk browser for perf-report
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description gtk
A GTK2 frontend for perf-report. (Use `perf report --gtk`.)

%package devel
Summary:        Development headers for perf
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
Development headers for perf. This is currently only dlfilter header.

%package bash-completion
Summary:        Bash completion for perf
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
bash command line completion support for perf.

%package rebuild
Summary:        Empty package to ensure rebuilding perf in OBS
%requires_eq kernel-source

%description rebuild
This is an empty package that ensures perf is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%package -n python-perf
Summary:        Python Bindings for Manipulating Perf Events
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python-perf
This package contains a module that permits applications written in
the Python programming language to manipulate perf events.

%prep
# copy necessary files from kernel-source since we need to modify them
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,tools,Makefile} lib kernel/bpf/disasm.[ch]) | tar -xf -
chmod +x tools/perf/util/generate-cmdlist.sh
%autopatch -p1 -m%{version_pure}0

# don't error out on deprecated definitions in gtk2.h
sed -i 's@ignored "-Wstrict-prototypes"@&\n#pragma GCC diagnostic ignored "-Wdeprecated-declarations"@' tools/build/feature/test-gtk2.c

# skip info-from-txt generation (it's the same as man anyway)
sed -i.old 's@\(all: .*\)info@\1@' tools/perf/Documentation/Makefile

# PASS rpm optflags as EXTRA_FLAGS, passing as CFLAGS overrides and breaks build
%define perf_options LIBTRACEEVENT_DYNAMIC=1 BUILD_BPF_SKEL=1 EXTRA_CFLAGS="%{optflags}" ASCIIDOC8=1 USE_ASCIIDOCTOR=1 CORESIGHT=1 GTK2=1 prefix=%{_prefix} libdir=%{_libdir} perfexecdir=lib/%{name}-core tipdir=share/doc/packages/perf %{_perf_unwind}

%build
cd tools/perf
export WERROR=0

# Specifying "all doc" as one invocation when using -f Makefile.perf doesn't
# work and all compiling is deferred to later %install; so seperate into two
make %{?_smp_mflags} -f Makefile.perf \
	V=0 VF=0 \
	%{perf_options} \
	all

make %{?_smp_mflags} -f Makefile.perf \
	V=0 VF=0 \
	%{perf_options} \
	doc

%install
cd tools/perf
export WERROR=0
make -f Makefile.perf \
	%{perf_options} \
	DESTDIR=%{buildroot} \
	install install-doc

# Install all python-perf flavors
%{python_expand #
rm -rf python_ext_build/*
make -f Makefile.perf \
	PYTHON=$python \
	%{perf_options} \
	DESTDIR=%{buildroot} \
	install-python_ext
}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/perf %{buildroot}%{_datadir}/bash-completion/completions/

# temp workaround as perf Makefile is still installing plugins even with LIBTRACEEVENT_DYNAMIC=1
rm -rf %{buildroot}/%{_libdir}/traceevent

%fdupes %{buildroot}/%{_prefix}/lib/%{name}-core

%files
%license COPYING
%doc CREDITS README tools/perf/design.txt
%if 0%{?suse_version} > 1315
%attr(0644, root, root) %doc %{_docdir}/perf/tips.txt
%endif
%{_bindir}/perf
%{_bindir}/trace
%{_prefix}/lib/%{name}-core
%if %{version_pure} < 614
%{_datadir}/%{name}-core
%endif
%{_mandir}/man1/perf*

%files gtk
%{_libdir}/libperf-gtk.so

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/perf

%files devel
%dir %{_includedir}/perf/
%{_includedir}/perf/*.h

%files rebuild
%license COPYING

%files %{python_files perf}
%defattr(-,root,root)
%{python_sitearch}/perf*

%changelog
