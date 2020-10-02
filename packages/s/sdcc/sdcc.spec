#
# spec file for package sdcc
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


Name:           sdcc
Version:        4.0.0
Release:        0
Summary:        Small Device C Compiler
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://sdcc.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
Patch0:         0001-Doc-Disable-fallback-to-dvipdfm-remove-non-pdftex-ta.patch
Patch2:         sdcc_enable_additional_target_libs.patch
Patch3:         sdcc-fixupInlineLabel.patch
Patch4:         sdcc-pcode.patch
BuildRequires:  bison
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gputils
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  python3-base
# documentation
BuildRequires:  inkscape
BuildRequires:  lyx
BuildRequires:  makeinfo
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-makeindex-bin
%if 0%{?suse_version} >= 1500
BuildRequires:  texlive-footnotehyper
%endif
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-ulem
BuildRequires:  zlib-devel
BuildRequires:  tex(footnote.sty)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

%package        doc
Summary:        Documentation for the SDCC C compiler
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

This package contains documentation for SDCC C compiler.

%package        libc-sources
Summary:        Small Device C Compiler
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description    libc-sources
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

This package contains sources for the C library and other files for
development.

%prep
%setup -q
rm support/regression/tests/bug3304184.c
# remove non-free libraries, see doc/README.txt: Licenses
find device/non-free/ \( -iname \*.h -o -iname \*.c -o -iname \*.S \) -delete
# remove spurious x bits from source files to make rpmlint happy.
find -name '*.[ch]' -perm -u=x | xargs chmod a-x
%patch0 -p1
%patch2 -p1
%patch3
%patch4
sed -i '1 s@.*@#!/usr/bin/python3@' support/scripts/as2gbmap.py

%build
# Force configure to ignore missing, but unused TeX binaries
export LATEX2HTML=/usr/bin/true
export DVIPDFM=/usr/bin/true
export PYTHON=/usr/bin/python3
%configure \
    --docdir=%{_docdir}/sdcc \
    --disable-non-free \
    --disable-doc

inkscape --export-area-drawing --export-pdf=doc/MCS51_named.pdf doc/MCS51_named.svg

make %{?_smp_mflags}
make %{?_smp_mflags} -C doc sdccman.pdf

%install
%make_install

# install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/sdas
cp sdas/doc/* %{buildroot}%{_docdir}/%{name}/sdas

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
mv %{buildroot}%{_bindir}/*.el %{buildroot}%{_datadir}/emacs/site-lisp

# remove useless file
rm %{buildroot}%{_docdir}/%{name}/INSTALL.txt

# remove strange stuff (installed by mistake?)
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic1{4,6}/.checkdevices
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic1{4,6}/aclocal.m4
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic1{4,6}/stamp-h1
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic1{4,6}/libsdcc/.dirstamp

# remove built libraries from source folder
find %{buildroot}%{_datadir}/%{name}/lib/src/pic16/ -iname \*lib*.a -delete
find %{buildroot}%{_datadir}/%{name}/lib/src/pic14/ -iname \*lib*.a -delete

# remove PPC embedspu (unneeded unless you have an AVR etc with a cell engine), conflicts with binutils
rm -f %{buildroot}%{_bindir}/embedspu

# duplicates
%fdupes -s %{buildroot}%{_datadir}/%{name}/lib/src
%fdupes -s %{buildroot}%{_bindir}
%fdupes -s %{buildroot}%{_datadir}/%{name}/include

# move src away temporarily, as we do not want symlinks across packages
mv %{buildroot}%{_datadir}/%{name}/lib/src %{buildroot}%{_datadir}/%{name}/src
%fdupes -s %{buildroot}%{_datadir}/%{name}/lib
mv %{buildroot}%{_datadir}/%{name}/src %{buildroot}%{_datadir}/%{name}/lib/src

%files
%doc ChangeLog doc/README.txt
%license COPYING
%exclude %{_docdir}/%{name}/ucsim/
%exclude %{_docdir}/%{name}/sdas/
%exclude %{_docdir}/%{name}/*.pdf
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/include
%{_datadir}/%{name}/lib
%exclude %{_datadir}/%{name}/lib/src
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*.el

%files libc-sources
%{_datadir}/%{name}/lib/src

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ucsim
%{_docdir}/%{name}/sdas
%{_docdir}/%{name}/sdccman.pdf

%changelog
