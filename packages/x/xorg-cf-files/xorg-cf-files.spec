#
# spec file for package xorg-cf-files
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


Name:           xorg-cf-files
Version:        1.0.8
Release:        0
Summary:        Data files for the imake utility
License:        MIT
Group:          Development/Tools/Building
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz
Patch1:         u_xorg-cf-files-D_DEFAULT_SOURCE.patch
BuildRequires:  font-util >= 1.1
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
Requires:       gccmakedep
Requires:       imake
Requires:       makedepend
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The xorg-cf-files package contains the data files for the imake utility,
defining the known settings for a wide variety of platforms (many of
which have not been verified or tested in over a decade), and for many
of the libraries formerly delivered in the X.Org monolithic releases.

The X Window System used imake extensively up through the X11R6.9
release, for both full builds within the source tree and external
software. X has since moved to GNU autoconf and automake for its build
system in X11R7.0 and later releases, but still maintains imake for
building existing external software programs that have not yet
converted.

%define _configdir %{_datadir}/X11/config

%prep
%setup -q
%patch1 -p1

cat > host.def << EOF
#define ConfigDir %_configdir
#define XAppLoadDir /usr/share/X11/app-defaults
#define UseSeparateConfDir NO
#define ManPath /usr/share/man
%ifarch ppc64 s390x x86_64 sparc64 riscv64
#define ModuleDir /usr/lib64/xorg/modules
%else
#define ModuleDir /usr/lib/xorg/modules
%endif
#ifdef  i386Architecture
#undef  DefaultGcc2i386Opt
#define DefaultGcc2i386Opt      -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  MipsArchitecture
#undef  DefaultGcc2MipsOpt
#define DefaultGcc2MipsOpt      -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  PpcArchitecture
#undef  DefaultGcc2PpcOpt
#define DefaultGcc2PpcOpt       -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  Ppc64Architecture
#undef  DefaultGcc2Ppc64Opt
#define DefaultGcc2Ppc64Opt     -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  AMD64Architecture
#undef  DefaultGcc2AMD64Opt
#define DefaultGcc2AMD64Opt     -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  AArch64Architecture
#undef  DefaultGcc2AArch64Opt
#define DefaultGcc2AArch64Opt   -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  s390xArchitecture
#undef  OptimizedCDebugFlags
#define OptimizedCDebugFlags    -O2 -Wall -fno-strict-aliasing
#endif
#ifdef  ia64Architecture
#undef  OptimizedCDebugFlags
#define OptimizedCDebugFlags    -O2 -Wall -fno-strict-aliasing
#endif
#if defined(SparcArchitecture) || defined(Sparc64Architecture)
#undef  OptimizedCDebugFlags
#define OptimizedCDebugFlags    -O2 -Wall -fno-strict-aliasing
# undef HaveLib64
#if defined(Sparc64Architecture)
# define HaveLib64    YES
#else
# define HaveLib64    NO
#endif
#endif
#ifdef  RiscV64Architecture
#undef  DefaultGcc2RiscV64Opt
#define DefaultGcc2RiscV64Opt   -O2 -Wall -fno-strict-aliasing
#endif
EOF

%build
%configure --with-config-dir=%_configdir
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
%dir %{_datadir}/X11
%{_datadir}/X11/config/

%changelog
