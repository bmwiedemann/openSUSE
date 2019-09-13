#
# spec file for package sgmltools-lite
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define syscfgsgml %{_sysconfdir}/sgml
%define regcat %{_bindir}/sgml-register-catalog
%define INSTALL install -m755 -s -p
%define INSTALL_SCRIPT install -m755 -p
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644 -p
Name:           sgmltools-lite
Version:        3.0.2
Release:        0
Summary:        SGML Converter Suite
License:        GPL-2.0+
Group:          Productivity/Publishing/SGML
Url:            http://sourceforge.net/projects/sgmltools-lite/
Source:         http://download.sourceforge.net/sgmltools-lite/sgmltools-lite-%{version}.tar.gz
Patch0:         sgmltools-lite-html.diff
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  python
BuildRequires:  sgml-skel
BuildRequires:  w3m
Requires:       docbook-dsssl-stylesheets
Requires:       docbook_3
Requires:       docbook_4
Requires:       iso_ent
Requires:       openjade
Requires:       opensp
Requires:       python
Requires:       w3m
Requires(pre):  %{regcat}
BuildArch:      noarch

%description
SGML Converter Suite written in Python.

%prep
%setup -q
%patch0 -p 1

%build
# `make clean' is needed for 3.0.2 (spurious config.* files)
# 2000-11-02 07:02:08 CET -ke-
make %{?_smp_mflags} clean
%configure \
  --with-etcsgml=%{syscfgsgml}
make %{?_smp_mflags}

%install
#make install prefix=$RPM_BUILD_ROOT/usr
# make install.man
mkdir -p %{buildroot}%{_bindir}
%{INSTALL_SCRIPT} bin/sgmltools %{buildroot}%{_bindir}
%{INSTALL_SCRIPT} bin/sgmlwhich %{buildroot}%{_bindir}
%define sgmldir %{_datadir}/sgml
%define sgmltoolsdir %{sgmldir}/stylesheets/sgmltools
%define sgmltoolsdtddir %{sgmldir}/dtd/sgmltools
%define sgmltoolspythondir %{sgmldir}/misc/sgmltools/python
%define sgmltoolspythonbackendsdir %{sgmltoolspythondir}/backends
mkdir -p %{buildroot}%{sgmltoolsdir}
for i in dsssl/*.dsl dsssl/*.cat; do \
  %{INSTALL_DATA} $i %{buildroot}%{sgmltoolsdir}; \
done
mkdir -p %{buildroot}%{sgmltoolsdtddir}
for i in dtd/[a-z]*; do \
  %{INSTALL_DATA} $i %{buildroot}%{sgmltoolsdtddir}; \
done
mkdir -p %{buildroot}%{_mandir}/man1
%{INSTALL_DATA} man/sgmltools.1 %{buildroot}%{_mandir}/man1/sgmltools-lite.1
mkdir -p %{buildroot}%{sgmltoolspythonbackendsdir}
for i in python/*.py; do \
  %{INSTALL_DATA} $i %{buildroot}%{sgmltoolspythondir}; \
done
for i in python/backends/*.py; do \
  %{INSTALL_DATA} $i %{buildroot}%{sgmltoolspythonbackendsdir}; \
done
%{INSTALL_DATA} VERSION %{buildroot}%{sgmldir}/misc/sgmltools
mkdir -p %{buildroot}%{syscfgsgml}
%{INSTALL_DATA} aliases %{buildroot}%{syscfgsgml}/aliases
# catalog is maintained by sgml-skel 2003-05-26 16:13:37 CEST -ke-
# # install -m 644 catalog.suse $RPM_BUILD_ROOT%{syscfgsgml}/catalog
# :> $RPM_BUILD_ROOT%{syscfgsgml}/catalog
# for c in `echo %{sgmldir}/CATALOG.iso_ent \
#                %{sgmldir}/CATALOG.docbook-dsssl-stylesheets \
#                %{sgmldir}/CATALOG.docbook_[0-9] \
#                %{sgmldir}/openjade/catalog \
#                %{buildroot}%{sgmltoolsdir}/*cat \
#                %{buildroot}%{sgmltoolsdtddir}/catalog*` ; do
#   if [ -f $c ] ; then
#     # remove %{buildroot} from filenames installed with this package
#     echo CATALOG \"$c\" | sed 's:%{buildroot}::' \
#       >> $RPM_BUILD_ROOT%{syscfgsgml}/catalog
#   else
#     echo CATALOG $c is missing. && exit 1
#   fi
# done
# # sed 's:/local::' catalog.suse >> $RPM_BUILD_ROOT%{syscfgsgml}/catalog

%post
if [ -x %{regcat} ]; then
  %{regcat} -a %{sgmltoolsdir}/sgmltools.cat >/dev/null 2>&1
fi
exit 0

%preun
if [ -x %{regcat} ]; then
  %{regcat} -r %{sgmltoolsdir}/sgmltools.cat  >/dev/null 2>&1
fi
exit 0

%files
%doc README POSTINSTALL index.html COPYING
%config %{syscfgsgml}/aliases
%{_bindir}/*
%{_mandir}/*/*
%{sgmldir}/*

%changelog
