#
# spec file for package json-table
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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

Name:           json-table
Version:        4.3.3
Release:        0
Summary:        Nested JSON data to tabular data transformer
License:        EPL-1.0
Group:          Productivity/File utilities
URL:            https://github.com/micha/json-table
#Git-Clone:     https://github.com/micha/json-table.git
Source:         https://github.com/micha/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         json-table-fix-build.patch

%description
Jt reads UTF-8 encoded JSON forms from stdin and writes tab separated
values (or CSV) to stdout. A simple stack-based programming language
is used to extract values from the JSON input for printing.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
make %{?_smp_mflags} test

%files
%doc README.md
%license LICENSE
%{_bindir}/jt
%{_mandir}/man1/jt.1%{?ext_man}

%changelog
