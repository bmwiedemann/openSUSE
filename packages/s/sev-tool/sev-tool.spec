#
# spec file for package sev-tool
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


Name:           sev-tool
Version:        0.17
Release:        0
Summary:        A tool for interacting with AMD SEV
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/AMDESE/sev-tool
Source:         %{name}_%{version}.orig.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel

%if 0%{?fedora_version} >= 29 || 0%{?rhel_version} >= 600 || 0%{?centos_version} >= 600
BuildRequires:  openssl-devel
%else
BuildRequires:  libopenssl-1_1-devel
%endif

BuildRequires:  libvirt-devel
BuildRequires:  make
BuildRequires:  openssl >= 1.1.0

%description
A tool for provisioning SEV encrypted virtual guests, executing hardware tests, and running host machine introspection.

%prep
%setup -q

%build
autoreconf -if
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root)
/usr/bin/sevtool

%changelog
