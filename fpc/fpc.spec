#
# spec file for package fpc
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%ifarch %arm
# We use hardfloat on ARM
%define fpcopt -dFPC_ARMHF -k--build-id -k-z -knoexecstack
%else
%define fpcopt -k--build-id -k-z -knoexecstack
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
%ifarch ppc64
%define ppcname ppcppc64
%endif
%ifarch %ix86
%define ppcname ppc386
%endif

# Current stable version does not support aarch64, so use beta version
%ifarch aarch64
# 3.1.1 = 3.1~svn39346
%define fpcversion 3.1.1
%else
%define fpcversion 3.0.4
%endif
%define stableversion 3.0.4

Name:           fpc
Version:        %{fpcversion}
Release:        0
Summary:        Free Pascal Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Languages/Other
Url:            https://www.freepascal.org/
# Stable version
Source:         %{name}build-%{stableversion}.tar.gz
# Current stable version does not support aarch64, so use beta version
# from ftp://ftp.freepascal.org/pub/fpc/snapshot/v31/source/
Source2:        %{name}build.zip
Source90:       %{name}-rpmlintrc
Patch0:         update-fpcdocs.patch
Patch1:         fpc-fix_aarch64.patch
BuildRequires:  binutils
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  fpc
BuildRequires:  glibc-devel
BuildRequires:  texlive
BuildRequires:  texlive-latex
%if 0%{?suse_version} > 1220
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-float
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-mdwtools
BuildRequires:  texlive-metafont
BuildRequires:  texlive-ntgclass
BuildRequires:  texlive-psnfss
BuildRequires:  texlive-times
%endif
%ifarch aarch64
BuildRequires:  unzip
%endif
Requires:       binutils
Requires:       gpm
Requires:       ncurses
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64 %arm aarch64 ppc ppc64

%description
Freepascal is a free 32/64bit Pascal Compiler. It comes with a run-time
library and is fully compatible with Turbo Pascal 7.0 and nearly Delphi
compatible. Some extensions are added to the language, like function
overloading and generics. Shared libraries can be linked. This package
contains commandline compiler and utils. Provided units are the runtime
library (RTL), free component library (FCL) and the base and extra
packages.

%package doc
Summary:        Freepascal Compiler - documentation and examples
Group:          Documentation/Other

%description doc
The fpc-doc package contains the documentation (in pdf format) and
examples of Freepascal.

%package src
Summary:        Freepascal Compiler - sources
Group:          Development/Languages/Other

%description src
The fpc-src package contains the sources of Freepascal, for
documentation or automatical-code generation purposes.

%prep
%ifnarch aarch64
%setup -q -n %{name}build-%{stableversion}
%patch0 -p1
%else
%setup -Tcq -b2 -n %{name}build
%patch1 -p1
%endif

# Remove files with license problems (which are not used on Linux)
rm -f fpcsrc/packages/nvapi/nvapi.pas

# Fix permissions (fix rpmlint warning "script-without-shebang")
chmod 644 fpcsrc/packages/cocoaint/utils/doc/Make\ Cocoa\ Headers.txt
chmod 644 fpcsrc/packages/cocoaint/utils/doc/Make\ Single\ Header.txt
chmod 644 fpcsrc/packages/cocoaint/utils/doc/Make\ iPhone\ Headers.txt
chmod 644 fpcsrc/packages/cocoaint/utils/parser.php
chmod 644 fpcsrc/packages/libvlc/src/vlc.pp
chmod 644 fpcsrc/packages/fcl-stl/tests/gtreetest.pp
chmod 644 fpcsrc/packages/fcl-stl/src/gtree.pp

# Copy needed source files by external packages in a new directory (to be included in the fpc-src subpackage)
install -dm 0755 fpc-src
cp -a fpcsrc/rtl fpc-src
cp -a fpcsrc/packages fpc-src
find fpc-src -name '*.o' | xargs rm -f
rm -rf fpc-src/packages/extra/amunits
rm -rf fpc-src/packages/extra/winunits

%build
STARTPP=%{ppcname}

pushd fpcsrc

FPCDIR=
NEWPP=`pwd`/compiler/%{ppcname}

make %{?_smp_mflags} compiler_cycle FPC=${STARTPP} OPT='%{fpcopt} %{fpcdebugopt}'
make %{?_smp_mflags} rtl_clean rtl_smart FPC=${NEWPP} OPT='%{fpcopt}'
make %{?_smp_mflags} packages_smart \
		FPC=${NEWPP} OPT='%{fpcopt}'
%ifnarch aarch64
make %{?_smp_mflags} ide_all \
		FPC=${NEWPP} OPT='%{fpcopt} %{fpcdebugopt}'
%endif
make %{?_smp_mflags} utils_all \
     FPC=${NEWPP} OPT='%{fpcopt} %{fpcdebugopt}'
mv ../fpcdocs .
make -C fpcdocs pdf FPC=${NEWPP}
popd

%install
# Make available built binaries
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
%ifnarch aarch64
make ide_distinstall      ${INSTALLOPTS}
%endif
make -C fpcdocs pdfinstall ${INSTALLOPTS}
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
cp -a fpcsrc/compiler/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING
cp -a fpcsrc/rtl/COPYING.txt %{buildroot}%{_defaultdocdir}/%{name}/COPYING.rtl
cp -a fpcsrc/rtl/COPYING.FPC %{buildroot}%{_defaultdocdir}/%{name}/COPYING.FPC

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

%files
%defattr(-,root,root,-)
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/NEWS
%doc %{_defaultdocdir}/%{name}/README
%doc %{_defaultdocdir}/%{name}/readme.ide
%doc %{_defaultdocdir}/%{name}/faq*
%doc %{_defaultdocdir}/%{name}/COPYING*
%doc %{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/fppkg.cfg
%dir %{_sysconfdir}/fppkg
%config(noreplace) %{_sysconfdir}/fppkg/default
%{_bindir}/*
%{_libdir}/%{name}/
%ifarch x86_64
/usr/lib/%{name}/
%endif
%exclude %{_defaultdocdir}/%{name}/*.pdf
%exclude %{_defaultdocdir}/%{name}/examples
%exclude %{_datadir}/fpcsrc

%files doc
%defattr(-,root,root,-)
%docdir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*.pdf
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/examples/*
%exclude %{_datadir}/fpcsrc

%files src
%defattr(-,root,root,-)
%dir %{_datadir}/fpcsrc
%{_datadir}/fpcsrc/*

%changelog
