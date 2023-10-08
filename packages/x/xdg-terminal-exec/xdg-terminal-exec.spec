#
# spec file for package xdg-terminal-exec
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


Name:           xdg-terminal-exec
Version:        20231003+git.e5c20d0
Release:        0
Summary:        XDG terminal execution utility and default terminal specification
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0-or-later
URL:            https://github.com/Vladimir-csp/xdg-terminal-exec/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bats

%description
Utility for XDG terminal execution and defining a systems default graphical terminal emulator.

%prep
%autosetup -p1

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 xdg-terminal-exec %{buildroot}%{_bindir}

%check
bats test

%files
%license LICENSE
%{_bindir}/xdg-terminal-exec

%changelog
