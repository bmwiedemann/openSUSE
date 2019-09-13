#
# spec file for package xmlto
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xmlto
Version:        0.0.28
Release:        0
Summary:        Tool for Converting XML Files to Various Formats
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/XML
URL:            https://pagure.io/xmlto/
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2
Source10:       README.SUSE
Patch0:         xmlto-nonvoid.patch
Patch1:         xmlto-xsltopts.patch
Patch2:         xmlto-codecleanup.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libxslt-tools
BuildRequires:  sgml-skel
# We rely entirely on the DocBook XSL stylesheets!
Requires:       docbook-xsl-stylesheets >= 1.56.0
Requires:       docbook_4
Requires:       libxslt-tools
# For full functionality, we need passivetex; but since most users are not happy with
# getting texlive installed, we only suggest it.
Suggests:      texlive-xmltex >= 2007

%description
This is a package for converting XML files to various formats using XSL
stylesheets.  As a processor it depends on xsltproc and as a formatter
for print output it makes use of passivetex.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %{SOURCE10} .
rm -f xmlif/xmlif.c

%build
%configure BASH=/bin/bash
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}%{_datadir}/xmlto/xsl
%fdupes %{buildroot}%{_datadir}/xmlto

%files
%doc README.SUSE
%license COPYING
%doc AUTHORS README ChangeLog FAQ THANKS NEWS
%{_bindir}/xmlto
%{_bindir}/xmlif
%{_mandir}/man1/xmlto.1%{?ext_man}
%{_mandir}/man1/xmlif.1%{?ext_man}
%{_datadir}/xmlto

%changelog
