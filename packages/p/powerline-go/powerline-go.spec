#
# spec file for package powerline-go
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


Name:           powerline-go
Version:        1.22.1
Release:        0
Summary:        A Powerline like prompt for Bash, ZSH and Fish
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://github.com/justjanne/powerline-go
Source0:        https://github.com/justjanne/powerline-go/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) = 1.17
BuildRequires:  golang-packaging
%{go_nostrip}

%description
A Powerline like prompt for Bash, ZSH and Fish. Based on Powerline-Shell by @banga. Ported to golang by @justjanne.

%prep
%autosetup -a1 -n %{name}-%{version}

%build
go build --mod=vendor -buildmode=pie

%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%check
go test -v

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
