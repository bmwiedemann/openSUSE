#
# spec file for package docbook-utils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           docbook-utils
Version:        0.6.15
Release:        0
Summary:        Small Wrapper Scripts for Processing DocBook Files
License:        LGPL-2.1-or-later
URL:            https://github.com/devexp-db/docbook-utils
Source:         https://github.com/devexp-db/docbook-utils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         docbook-utils-catalog-jw.patch
Patch1:         docbook-utils-0.6.15-fix-bashisms.patch
# PATCH-FIX-TO-UPSTREAM
Patch2:         support_source_date_epoch.patch
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  sgml-skel
# Keep the tool package names: spec-cleaner --perl explodes them into
# the full provided perl() module list, which is noise.
BuildRequires:  automake
BuildRequires:  perl-SGMLS
Requires:       %{name}-minimal
# Keep the texlive package name: the tex() file deps resolve to the
# same package but hide which backend the scripts actually need.
Requires:       texlive-jadetex
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
Requires:       docbook-dsssl-stylesheets
Requires:       docbook_3
Requires:       docbook_4
Requires:       iso_ent
Requires:       openjade
Requires:       opensp
Requires:       sgml-skel
# Keep the tool package name, see the BuildRequires comment above.
Requires:       perl-SGMLS

%description minimal
The docbook-utils package is a set of a few small programs intended to
ease everyday use of technical documentation software based on the
DocBook DTD, either written in SGML or XML.

Tasks they currently accomplish are: * jw: convert SGML files to
   other formats (HTML, RTF, PostScript, PDF)

* sgmldiff: detect the differences in markup between two SGML files

%prep
%setup -q
%patch -P 0 -p1 -b .catalog
%patch -P 1 -p1
%patch -P 2 -p1

%build
autoreconf -i -f
%configure
%make_build

%install
%make_install
mv %{buildroot}%{_prefix}/doc/html/docbook* html

%files minimal
%license COPYING
%doc README TODO html
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/jw
%{_bindir}/sgmldiff
%{_bindir}/docbook2txt
%dir %{_datadir}/sgml/docbook/utils-%{version}
%dir %{_datadir}/sgml/docbook/utils-%{version}/backends
%{_datadir}/sgml/docbook/utils-%{version}/frontends
%{_datadir}/sgml/docbook/utils-%{version}/backends/html
%{_datadir}/sgml/docbook/utils-%{version}/backends/man
%{_datadir}/sgml/docbook/utils-%{version}/backends/rtf
%{_datadir}/sgml/docbook/utils-%{version}/backends/txt
%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
%{_datadir}/sgml/docbook/utils-%{version}/helpers

%files
%{_bindir}/docbook2ps
%{_bindir}/docbook2dvi
%{_bindir}/docbook2pdf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_datadir}/sgml/docbook/utils-%{version}/backends/tex
%{_datadir}/sgml/docbook/utils-%{version}/backends/texi
%{_datadir}/sgml/docbook/utils-%{version}/backends/dvi
%{_datadir}/sgml/docbook/utils-%{version}/backends/ps
%{_datadir}/sgml/docbook/utils-%{version}/backends/pdf
%{_mandir}/man?/*

%changelog
