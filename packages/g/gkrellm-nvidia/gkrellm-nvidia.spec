#
# spec file for package gkrellm-nvidia
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gkrellm-nvidia
Version:        1.2
Release:        0
Summary:        A plugin for GKrellM and Nvidia GPUs
License:        GPL-2.0-or-later
URL:            https://github.com/carcass82/gkrellm-nvidia
Source:         https://github.com/carcass82/gkrellm-nvidia/archive/refs/tags/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gkrellm)
Requires:       gkrellm

%description
A simple GKrellM plugin for reading nvidia GPUs data. Clock, Temperature and
Fan Speed for multiple GPU are supported.

%prep
%autosetup -p1 -n %{name}-release-%{version}
sed -i "s:/lib/:/%{_lib}/:" Makefile

%build
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_libdir}/gkrellm2/plugins/nvidia.so

%changelog
