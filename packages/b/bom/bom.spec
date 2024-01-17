#
# spec file for package bom
#
# Copyright (c) 2021 SUSE LLC
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


Name:           bom
Version:        1.0.1
Release:        0
Summary:        Deals with Unicode byte order marks
License:        Apache-2.0
Group:          Productivity/File utilities
URL:            https://github.com/archiecobbs/%{name}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

%description
bom is a simple UNIX command line utility for dealing with Unicode byte
order marks (BOM's).

Unicode byte order marks are "magic number" byte sequences that sometimes
appear at the beginning of a file to indicate the file's character
encoding. They're sometimes helpful but usually they're just annoying.

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
install -d %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1.gz
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}

%changelog
