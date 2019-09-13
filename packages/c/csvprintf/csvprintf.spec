#
# spec file for package csvprintf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2010 Archie L. Cobbs <archie@dellroad.org>
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


Name:           csvprintf
Version:        1.0.4
Release:        0
Summary:        Simple CSV file parser for the UNIX command line
License:        Apache-2.0
Group:          Productivity/Text/Utilities
Source:         %{name}-%{version}.tar.gz
Url:            http://csvprintf.googlecode.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xsltproc
Requires:       xsltproc

%description
%{name} is a simple UNIX command line utility for parsing CSV files.

%{name} works just like the printf(1) command line utility. You
supply a printf(1) format string on the command line and each record
in the CSV file is formatted accordingly. Each format specifier in
the format string contains a column accessor to specify which CSV
column to use, so for example '%%3$d' would format the third column
as a decimal value.

%{name} can also convert CSV files into XML documents and back.

%prep
%setup -q

%build
%{configure}
make

%install
%{makeinstall}

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/xml2csv
%attr(0644,root,root) %{_mandir}/man1/*
%defattr(0644,root,root,0755)
%doc %{_datadir}/doc/packages/%{name}
%{_datadir}/%{name}

%changelog
