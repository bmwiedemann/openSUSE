#
# spec file for package matcha
#
# Copyright (c) 2026 mantarimay
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


Name:           matcha
Version:        0.14.2
Release:        0
Summary:        A terminal email client
License:        MIT
URL:            https://github.com/floatpane/matcha
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
Matcha is a terminal email client for users who prefer keyboards
over mice and terminals over browsers.

It is built with Go and the Bubble Tea TUI framework. It supports
email providers such as Gmail and iCloud. Mail can be read, composed
and managed entirely from the command line.

%prep
%autosetup -p1 -a1

%build
go build \
   -o build/%{name} \
   -mod=vendor \
   -ldflags="-s -w" \
   -buildmode=pie \
   ./

%install
install -Dm0755 build/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
