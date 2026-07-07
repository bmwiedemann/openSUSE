#
# spec file for package mcp-server-managesw
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


%define gitname managesw-mcp
%define vers 0.2.1

Name:           mcp-server-managesw
Version:        0.2.1
Release:        0
Summary:        MCP server for package management
License:        MIT
URL:            https://github.com/openSUSE/managesw-mcp
Source0:        https://github.com/openSUSE/managesw-mcp/archive/refs/tags/v%{vers}%{?verssuf}.tar.gz#/%{name}-%{vers}%{?verssuf}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.24

%description
a server that exposes OS software management functions through the Model
Context Protocol (MCP). It allows you to manage packages, repositories, and
patches on a Linux system. Most of the functions are only available on zypper
and dnf based systems

%prep
%autosetup -p1 -a1 -n %{gitname}-%{version}

%build
# The macro make_build does not work on older CentOS releases
make

%install
# The macro make_install does not work on older CentOS releases
make install DESTDIR=%{buildroot}
# RPM automatically stores hardlinked files only once
ln %{buildroot}/%{_bindir}/%{gitname} %{buildroot}/%{_bindir}/%{name}

%check

%files
%{_bindir}/%{gitname}
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
