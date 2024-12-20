#
# spec file for package go-md2man
#
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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

Name:           go-md2man
Version:        2.0.6
Release:        0
Summary:        Utility to create manpages from markdown
License:        MIT
Group:          Development/Tools/Doc Generators
URL:            https://github.com/cpuguy83/
Source:         https://github.com/cpuguy83/go-md2man/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

%description
Utility to create manpages from markdown.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/cpuguy83/go-md2man/v2
%{gobuild} -mod=vendor .

%install
%{goinstall}
install -d %{buildroot}%{_mandir}/man1/
%{buildroot}/%{_bindir}/go-md2man -in go-md2man.1.md -out %{buildroot}%{_mandir}/man1/go-md2man.1

%files
%license LICENSE.md
%doc README.md
%{_bindir}/go-md2man
%{_mandir}/man1/go-md2man.1%{?ext_man}

%changelog
