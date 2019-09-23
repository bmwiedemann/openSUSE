#
# spec file for package docbook-utils
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


Name:           docbook-utils
BuildRequires:  automake
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  perl-SGMLS
BuildRequires:  sgml-skel
Summary:        Small Wrapper Scripts for Processing DocBook Files
License:        LGPL-2.1+
Group:          Productivity/Publishing/DocBook
Version:        0.6.14
Release:        0
Requires:       %{name}-minimal
Requires:       texlive-jadetex
Source:         ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/%{name}-%{version}.tar.gz
Patch0:         docbook-utils-catalog-jw.patch
Patch1:         docbook-utils-0.6.14-fix-bashisms.patch
# PATCH-FIX-TO-UPSTREAM
Patch2:         support_source_date_epoch.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The docbook-utils package is a set of a few small programs intended to
ease everyday use of technical documentation software based on the
DocBook DTD, either written in SGML or XML.

Tasks they currently accomplish are: * jw: convert SGML files to
   other formats (HTML, RTF, PostScript, PDF)

* sgmldiff: detect the differences in markup between two SGML files

%package minimal
Summary:        Small Wrapper Scripts for Processing DocBook Files
Group:          Productivity/Publishing/DocBook
Requires:       docbook-dsssl-stylesheets
Requires:       docbook_3
Requires:       docbook_4
Requires:       iso_ent
Requires:       openjade
Requires:       opensp
Requires:       perl-SGMLS
Requires:       sgml-skel

%description minimal
The docbook-utils package is a set of a few small programs intended to
ease everyday use of technical documentation software based on the
DocBook DTD, either written in SGML or XML.

Tasks they currently accomplish are: * jw: convert SGML files to
   other formats (HTML, RTF, PostScript, PDF)

* sgmldiff: detect the differences in markup between two SGML files

%prep
%setup -q
%patch0 -p1 -b .catalog
%patch1 -p1
%patch2 -p1

%build
autoreconf -i -f
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/usr/doc/html/docbook* html

%files minimal
%defattr (-,root,root)
%doc README COPYING TODO html
%_bindir/docbook2html
%_bindir/docbook2man
%_bindir/docbook2rtf
%_bindir/jw
%_bindir/sgmldiff
%_bindir/docbook2txt
%dir %{_prefix}/share/sgml/docbook/utils-%{version}
%dir %{_prefix}/share/sgml/docbook/utils-%{version}/backends
%{_prefix}/share/sgml/docbook/utils-%{version}/frontends
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/html
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/man
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/rtf
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/txt
%{_prefix}/share/sgml/docbook/utils-%{version}/docbook-utils.dsl
%{_prefix}/share/sgml/docbook/utils-%{version}/helpers

%files
%defattr (-,root,root)
%_bindir/docbook2ps
%_bindir/docbook2dvi
%_bindir/docbook2pdf
%_bindir/docbook2tex
%_bindir/docbook2texi
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/tex
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/texi
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/dvi
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/ps
%{_prefix}/share/sgml/docbook/utils-%{version}/backends/pdf
%{_mandir}/man?/*

%changelog
