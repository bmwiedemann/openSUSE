#
# spec file for package bluetuith
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


Name:           bluetuith
Version:        0.1.3
Release:        0
Summary:        A TUI bluetooth manager for Linux
License:        MIT
Group:          Hardware/Mobile
URL:            https://github.com/darkhz/bluetuith
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
Requires:       bluez
Requires:       dbus-1

%description
bluetuith is a TUI-based bluetooth connection manager, which can interact with bluetooth adapters and devices. It aims to be a replacement to most bluetooth managers, like blueman.
This project is currently in the alpha stage.

%prep
%setup -q -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
