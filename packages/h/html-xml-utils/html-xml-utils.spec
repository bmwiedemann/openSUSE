#
# spec file for package html-xml-utils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           html-xml-utils
Version:        7.7
Release:        0
Summary:        A number of utilities for manipulating HTML and XML files
License:        W3C
Group:          Development/Languages/Other
Url:            https://www.w3.org/Tools/HTML-XML-utils/
Source:         https://www.w3.org/Tools/HTML-XML-utils/html-xml-utils-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libcurl-devel
BuildRequires:  libidn2-devel

%description
HTML-XML-utils provides a number of utilities for manipulating and
converting HTML and XML files in various ways.

%prep
%setup -q
chmod -x ChangeLog README

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
