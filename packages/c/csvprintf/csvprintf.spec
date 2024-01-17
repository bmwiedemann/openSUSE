#
# spec file for package csvprintf
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


Name:           csvprintf
Version:        1.3.2
Release:        0
Summary:        Simple CSV file parser for the UNIX command line
License:        Apache-2.0
Group:          Productivity/File utilities
URL:            https://github.com/archiecobbs/csvprintf
Source:         %{name}/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xsltproc
Requires:       xsltproc

%description
%{name} is a simple UNIX command line utility for parsing CSV files.

%{name} works like the printf(1) command line utility: you supply a
printf(1) format string on the command line, and each row of the CSV file
is split into arguments and formatted accordingly. The format specifiers
in the format string contain numeric or symbolic column accessors to
specify which CSV column to format.

%{name} can also convert CSV files into XML and JSON documents
and Bash variable assignments suitable for eval(1).

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%check
%make_build tests

%install
%make_install

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/xml2csv
%attr(0644,root,root) %{_mandir}/man1/*
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}
%{_datadir}/%{name}

%changelog
