#
# spec file for package fpc
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%else
%global psuffix -%{flavor}
%endif

%ifarch ppc64le ppc64 ppc
# Bootstrap the compiler for a new architecture. Set this to 0 after we've bootstrapped.
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif

%ifarch %arm
# We use hardfloat on ARM
%define fpcopt -dFPC_ARMHF -k--build-id -k-z -knoexecstack
%else
%ifarch ppc64le
%define fpcopt -Cb- -Caelfv2 -k--build-id -k-z -knoexecstack
%else
%define fpcopt -k--build-id -k-z -knoexecstack
%endif
%endif
%define fpcdebugopt -gl

%ifarch aarch64
%define ppcname ppca64
%endif
%ifarch %arm
%define ppcname ppcarm
%endif
%ifarch ppc
%define ppcname ppcppc
%endif
%ifarch x86_64
%define ppcname ppcx64
%endif
%ifarch ppc64le
%define ppcname ppcppc64
%endif
%ifarch ppc64
%define ppcname ppcppc64
%endif
%ifarch %ix86
%define ppcname ppc386
%endif

Name:           fpc%{?psuffix}
Version:        3.2.0
Release:        0
%if "%{flavor}" == ""
Summary:        Free Pascal Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other
%else
Summary:        Freepascal Compiler documentation
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Documentation/Other
%endif
URL:            https://www.freepascal.org/
Source:         fpcbuild-%{version}.tar.gz
Source1:        fpc-3.2.0-aarch64.zip
Source2:        fpc-3.2.0-ppc64le.zip
Source3:        fpc-3.2.0-ppc64.zip
Source4:        fpc-3.2.0-ppc.zip
Source90:       fpc-rpmlintrc
Patch0:         fpc-fix-library-paths-on-aarch64.patch
Patch1:         fpc-si_c-x86_64-plt.patch
Patch2:         aarch64-fpc-compilation-fix.patch
# From https://github.com/graemeg/freepascal/commit/aad68409bec902e39f9292930238edd32dbc5ac7
Patch3:         aarch64-fpu-initialization.patch
BuildRequires:  binutils
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if %{without bootstrap}
BuildRequires:  fpc
%else
%if "%{flavor}" == "doc"
BuildRequires:  fpc
%else
BuildRequires:  unzip
%endif
%endif
BuildRequires:  glibc-devel
%if "%{flavor}" == "doc"
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-pdftex
BuildRequires:  texlive-ucs
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(a4.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(phvr8t.tfm)
BuildRequires:  tex(ptmr8t.tfm)
BuildRequires:  tex(syntax.sty)
BuildRequires:  tex(tabularx.sty)
BuildRequires:  tex(times.sty)
%endif
Requires:       binutils
ExclusiveArch:  %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le

%if "%{flavor}" == ""
%description
Freepascal is a free 32/64bit Pascal Compiler. It comes with a run-time
library and is fully compatible with Turbo Pascal 7.0 and nearly Delphi
compatible. Some extensions are added to the language, like function
overloading and generics. Shared libraries can be linked. This package
contains commandline compiler and utils. Provided units are the runtime
library (RTL), free component library (FCL) and the base and extra
packages.

%else
%description
The fpc-doc package contains the documentation PDF files.

%endif

%package examples 
Summary:        Freepascal Compiler examples
Group:          Documentation/Other
BuildArch:      noarch

%description examples
The fpc-examples package contains examples for Freepascal.

%package src
Summary:        Freepascal Compiler - sources
Group:          Development/Languages/Other

%description src
The fpc-src package contains the sources of Freepascal, for
documentation or automatical-code generation purposes.

%prep
%setup -q -n fpcbuild-%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

%if %{with bootstrap}
%if "%{flavor}" == ""
%ifarch aarch64
unzip %{SOURCE1}
%endif
%ifarch ppc64le
unzip %{SOURCE2}
%endif
%ifarch ppc64
unzip %{SOURCE3}
%endif
%ifarch ppc
unzip %{SOURCE4}
%endif
%endif
%endif

# Remove files with license problems (which are not used on Linux)
rm -f fpcsrc/packages/nvapi/src/nvapi.pas

# Copy needed source files by external packages in a new directory (to be included in the fpc-src subpackage)
install -dm 0755 fpc-src
cp -a fpcsrc/rtl fpc-src
cp -a fpcsrc/packages fpc-src
find fpc-src -name '*.o' | xargs rm -f
rm -rf fpc-src/packages/extra/amunits
rm -rf fpc-src/packages/extra/winunits

# Inject reproducible date into PDF documentation
date --date=@${SOURCE_DATE_EPOCH:-0} +'\date{%B %Y}' > fpcdocs/date.inc

%build
%if "%{flavor}" == ""
%if %{with bootstrap}
STARTPP=$(pwd)/fpc-%{version}-%{_arch}/bin/%{ppcname}
%else
STARTPP=%{ppcname}
%endif

pushd fpcsrc

FPCDIR=
NEWPP=`pwd`/compiler/%{ppcname}

make %{?_smp_mflags} compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{fpcdebugopt}'
make %{?_smp_mflags} rtl_clean rtl_smart FPC=${NEWPP} OPT='%{fpcopt}'
make %{?_smp_mflags} packages_smart \
		FPC=${NEWPP} OPT='%{fpcopt}'
make %{?_smp_mflags} utils_all \
     FPC=${NEWPP} OPT='%{fpcopt} %{fpcdebugopt}'
popd

%else
make -C fpcdocs pdf FPC=fpc
%endif

%install
# Make available built binaries
%if "%{flavor}" == ""
export PATH=$PATH:%{buildroot}%{_bindir}
pushd fpcsrc
FPCDIR=
NEWPP=`pwd`/compiler/%{ppcname}
INSTALLOPTS="FPC=${NEWPP} \
	INSTALL_PREFIX=%{buildroot}%{_prefix} \
	INSTALL_LIBDIR=%{buildroot}%{_libdir} \
	INSTALL_BASEDIR=%{buildroot}%{_libdir}/%{name}/%{version} \
	CODPATH=%{buildroot}%{_libdir}/%{name}/lexyacc \
	INSTALL_DOCDIR=%{buildroot}%{_defaultdocdir}/%{name} \
	INSTALL_BINDIR=%{buildroot}%{_bindir}
	INSTALL_EXAMPLEDIR=%{buildroot}%{_defaultdocdir}/%{name}/examples"

make compiler_distinstall ${INSTALLOPTS}
make utils_distinstall    ${INSTALLOPTS}
make rtl_distinstall      ${INSTALLOPTS}
make packages_distinstall ${INSTALLOPTS}
popd

pushd install
	make -C doc ${INSTALLOPTS}
	make -C man ${INSTALLOPTS} INSTALL_MANDIR=%{buildroot}%{_mandir}
popd

# create link
ln -sf ../%{_lib}/%{name}/%{version}/%{ppcname} %{buildroot}%{_bindir}/%{ppcname}

# create a version independent config
FPCMKCFGBIN=%{buildroot}%{_prefix}/bin/fpcmkcfg
FPCPATH=%{_libdir}/fpc/`$NEWPP -iV`
SYSFPDIRBASE=%{buildroot}%{_libdir}/fpc/`$NEWPP -iV`/ide/text
${FPCMKCFGBIN} -p -d "basepath=$FPCPATH" -o %{buildroot}%{_sysconfdir}/fpc.cfg
${FPCMKCFGBIN} -p -1 -d "basepath=$FPCPATH" -o ${SYSFPDIRBASE}/fp.cfg
${FPCMKCFGBIN} -p -2 -o ${SYSFPDIRBASE}/fp.ini
${FPCMKCFGBIN} -p -3 -d CompilerConfigDir=%{_sysconfdir}/fppkg -o %{buildroot}%{_sysconfdir}/fppkg.cfg
${FPCMKCFGBIN} -p -4 -d "GlobalPrefix=$FPCGLOBALPREFIX" -o %{buildroot}%{_sysconfdir}/fppkg/default
# Add support for "build ID" in binaries (for debuginfo support)
echo -e \
"\n# ----------------------\n\
# Use BuildId by default\n\
# ----------------------\n\
-k--build-id" >> %{buildroot}%{_sysconfdir}/fpc.cfg

# include the COPYING-information for the compiler/rtl/fcl in the documentation
install -m 644 -D fpcsrc/compiler/COPYING.txt %{buildroot}%{_licensedir}/%{name}/COPYING
install -m 644 -D fpcsrc/rtl/COPYING.txt %{buildroot}%{_licensedir}/%{name}/COPYING.rtl
install -m 644 -D fpcsrc/rtl/COPYING.FPC %{buildroot}%{_licensedir}/%{name}/COPYING.FPC

mv %{buildroot}%{_defaultdocdir}/%{name}/../../%{name}-%{version}/ide/readme.ide %{buildroot}%{_defaultdocdir}/%{name}/readme.ide
mv %{buildroot}%{_defaultdocdir}/%{name}/../../%{name}-%{version} %{buildroot}%{_defaultdocdir}/%{name}/examples
# Install source files needed by external packages
cp -a fpc-src/ %{buildroot}%{_datadir}/fpcsrc/

# delete lexyacc
rm -rf %{buildroot}%{_libdir}/%{name}/lexyacc

chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/ibase/scripts/mkdb
chmod 644 %{buildroot}%{_datadir}/fpcsrc/packages/iconvenc/src/iconvenc.pas
chmod 644 %{buildroot}%{_datadir}/fpcsrc/packages/iconvenc/examples/iconvtest.pp
chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/libc/scripts/h2p
chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/mysql/scripts/rmdb
chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/postgres/scripts/mkdb
chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/postgres/scripts/rmdb
chmod 755 %{buildroot}%{_datadir}/fpcsrc/packages/xforms/scripts/doc2p
chmod 755 %{buildroot}%{_datadir}/fpcsrc/rtl/freebsd/*/identpatch.sh
chmod 755 %{buildroot}%{_datadir}/fpcsrc/rtl/netware/convertimp

%if 0%{?suse_version}
%fdupes -s %{buildroot}%{_datadir}/fpcsrc
%fdupes -s %{buildroot}%{_libdir}/%{name}
%endif

%else
make -C fpcdocs pdfinstall \
        FPC=fpc \
        INSTALL_DOCDIR=%{buildroot}%{_defaultdocdir}/fpc
%endif

%if "%{flavor}" == ""
%files
%license %{_licensedir}/%{name}
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/NEWS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/readme.ide
%doc %{_defaultdocdir}/%{name}/faq*
%doc %{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/fppkg.cfg
%dir %{_sysconfdir}/fppkg
%config(noreplace) %{_sysconfdir}/fppkg/default
%{_bindir}/*
%{_libdir}/libpas2jslib.so*
%{_libdir}/%{name}/
%ifarch x86_64 aarch64 ppc64 ppc64le
/usr/lib/%{name}/
%endif

%files examples
%docdir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/examples/*

%files src
%dir %{_datadir}/fpcsrc
%{_datadir}/fpcsrc/*

%else
%files
%docdir %{_defaultdocdir}/fpc
%doc %{_defaultdocdir}/fpc/*.pdf
%endif

%changelog
