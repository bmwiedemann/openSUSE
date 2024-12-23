#
# spec file for package helmtui
#
# Copyright (c) 2024 SUSE LLC
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


Name:           helmtui
Version:        0.5.1
Release:        0
Summary:        A simple terminal UI for Helm
License:        MIT
URL:            https://github.com/pidanou/helmtui
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18

%description
Helmtui is a terminal-based UI application to manage your Helm releases,
charts, repositories, and plugins with ease.

Features

* Manage Helm releases effortlessly.
* Add, update, and remove Helm repositories.

%prep
%autosetup -p 1 -a 1

%build
CGO_ENABLED=1 go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
