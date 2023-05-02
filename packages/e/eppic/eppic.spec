#
# spec file for package eppic
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


Name:           eppic
Version:        4.99.git.1682279748.c294e5b
Release:        0
Summary:        Embeddable Pre-Processor and Interpreter for C
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
Patch1:         %{name}-fix-install.patch
BuildRequires:  bison
BuildRequires:  crash-devel
BuildRequires:  flex
BuildRequires:  ncurses-devel
URL:            https://github.com/lucchouina/eppic
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

%package -n libeppic-devel
Summary:        EPPIC include files and libraries
Group:          Development/Languages/C and C++

%package -n crash-eppic
Summary:        The eppic extension for crash
Group:          Development/Tools/Debuggers

%description -n libeppic-devel
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

This package provides the include files and libraries needed for development.

%description -n crash-eppic
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

This package provides the extension for the crash utility.

%prep
%setup
%autopatch -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make -C libeppic CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

case `uname -m` in
  aarch64)
    TARGET=ARM64
    TARGET_CFLAGS=
    ;;
  arm*)
    TARGET=ARM
    TARGET_CFLAGS=-D_FILE_OFFSET_BITS=64
    ;;
  i?86)
    TARGET=X86
    TARGET_CFLAGS=-D_FILE_OFFSET_BITS=64
    ;;
  ia64)
    TARGET=IA64
    TARGET_CFLAGS=
    ;;
  ppc)
    TARGET=PPC
    TARGET_CFLAGS=-D_FILE_OFFSET_BITS=64
    ;;
  ppc64|ppc64le)
    TARGET=PPC64
    TARGET_CFLAGS=-m64
    ;;
  riscv64)
    TARGET=RISCV64
    TARGET_CFLAGS=
    ;;
  s390)
    TARGET=S390
    TARGET_CFLAGS=-D_FILE_OFFSET_BITS=64
    ;;
  s390x)
    TARGET=S390X
    TARGET_CFLAGS=
    ;;
  x86_64)
    TARGET=X86_64
    TARGET_CFLAGS=
    ;;
esac
export TARGET TARGET_CFLAGS
ln -snf ../../libeppic applications/crash/
make -C applications/crash -f eppic.mk INCDIR=/usr/include/crash eppic.so

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
make -C libeppic ROOT="%{buildroot}" LIBDIR=%{_libdir} install

mkdir -p %{buildroot}%{_libdir}/crash/extensions
install -m 0644 applications/crash/eppic.so %{buildroot}%{_libdir}/crash/extensions
install -d -m 0755 %{buildroot}%{_datadir}/eppic
cp -r applications/crash/code %{buildroot}%{_datadir}/eppic/crash

%files -n libeppic-devel
%defattr(-,root,root)
%doc libeppic/README.md
%{_includedir}/eppic.h
%{_includedir}/eppic_api.h
%attr(644,root,root) %{_libdir}/libeppic.a

%files -n crash-eppic
%doc applications/crash/README.code
%{_libdir}/crash/extensions/eppic.so
%{_datadir}/eppic

%changelog
