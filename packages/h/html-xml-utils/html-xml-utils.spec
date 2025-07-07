#
# spec file for package html-xml-utils
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


Name:           html-xml-utils
Version:        8.7
Release:        0
Summary:        A number of utilities for manipulating HTML and XML files
License:        W3C
Group:          Development/Languages/Other
URL:            https://www.w3.org/Tools/HTML-XML-utils/
Source:         https://www.w3.org/Tools/HTML-XML-utils/html-xml-utils-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-dtd-declaration.patch -- fix compilation error on conflicting declarations
Patch0:         fix-dtd-declaration.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libcurl-devel
BuildRequires:  libidn2-devel

%description
HTML-XML-utils provides a number of utilities for manipulating and
converting HTML and XML files in various ways.

%prep
%autosetup -p1
chmod -x ChangeLog README

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING

%check
%{buildroot}%{_bindir}/hxextract h1

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/asc2xml
%{_bindir}/hxaddid
%{_bindir}/hxcite
%{_bindir}/hxcite-mkbib
%{_bindir}/hxclean
%{_bindir}/hxcopy
%{_bindir}/hxcount
%{_bindir}/hxextract
%{_bindir}/hxincl
%{_bindir}/hxindex
%{_bindir}/hxmkbib
%{_bindir}/hxmultitoc
%{_bindir}/hxname2id
%{_bindir}/hxnormalize
%{_bindir}/hxnsxml
%{_bindir}/hxnum
%{_bindir}/hxpipe
%{_bindir}/hxprintlinks
%{_bindir}/hxprune
%{_bindir}/hxref
%{_bindir}/hxremove
%{_bindir}/hxselect
%{_bindir}/hxtabletrans
%{_bindir}/hxtoc
%{_bindir}/hxuncdata
%{_bindir}/hxunent
%{_bindir}/hxunpipe
%{_bindir}/hxunxmlns
%{_bindir}/hxwls
%{_bindir}/hxxmlns
%{_bindir}/xml2asc
%{_mandir}/man1/asc2xml.1.gz
%{_mandir}/man1/hxaddid.1.gz
%{_mandir}/man1/hxcite-mkbib.1.gz
%{_mandir}/man1/hxcite.1.gz
%{_mandir}/man1/hxclean.1.gz
%{_mandir}/man1/hxcopy.1.gz
%{_mandir}/man1/hxcount.1.gz
%{_mandir}/man1/hxextract.1.gz
%{_mandir}/man1/hxincl.1.gz
%{_mandir}/man1/hxindex.1.gz
%{_mandir}/man1/hxmkbib.1.gz
%{_mandir}/man1/hxmultitoc.1.gz
%{_mandir}/man1/hxname2id.1.gz
%{_mandir}/man1/hxnormalize.1.gz
%{_mandir}/man1/hxnsxml.1.gz
%{_mandir}/man1/hxnum.1.gz
%{_mandir}/man1/hxpipe.1.gz
%{_mandir}/man1/hxprintlinks.1.gz
%{_mandir}/man1/hxprune.1.gz
%{_mandir}/man1/hxref.1.gz
%{_mandir}/man1/hxremove.1.gz
%{_mandir}/man1/hxselect.1.gz
%{_mandir}/man1/hxtabletrans.1.gz
%{_mandir}/man1/hxtoc.1.gz
%{_mandir}/man1/hxuncdata.1.gz
%{_mandir}/man1/hxunent.1.gz
%{_mandir}/man1/hxunpipe.1.gz
%{_mandir}/man1/hxunxmlns.1.gz
%{_mandir}/man1/hxwls.1.gz
%{_mandir}/man1/hxxmlns.1.gz
%{_mandir}/man1/xml2asc.1.gz

%changelog
