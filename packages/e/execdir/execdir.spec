#
# spec file for package execdir
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           execdir
Version:        0.4.1.git1770014834
Release:        0
Summary:        Execute a command in a specific directory
License:        MIT
URL:            https://github.com/qr243vbi/execdir
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(lmdb)

%description
A tool that lets you run a command in a specific directory. It supports shell commands and path aliases. execdir will try to get an alias if the path doesn't exist.
Example usage: execdir <dir> <command> [<arguments> ...]

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md
%{_mandir}/man1/%{name}.1*

%changelog
