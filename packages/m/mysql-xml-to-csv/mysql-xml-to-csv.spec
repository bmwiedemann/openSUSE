#
# spec file for package mysql-xml-to-csv
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


Name:           mysql-xml-to-csv
Version:        1.0.2
Release:        0
Summary:        Convert MySQL XML output to CSV
License:        Apache-2.0
Group:          Productivity/Databases/Tools
URL:            https://github.com/archiecobbs/%{name}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libexpat-devel
BuildRequires:  make

%description
%{name} converts MySQL XML query results (i.e., produced using
the mysql(1) command when given the --xml flag) into a CSV file.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install
install -d %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1.gz
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}

%changelog
