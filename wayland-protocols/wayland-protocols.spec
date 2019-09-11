#
# spec file for package wayland-protocols
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


Name:           wayland-protocols
Version:        1.18
Release:        0
Summary:        Wayland protocols that adds functionality not available in the core protocol
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://wayland.freedesktop.org/
Source:         https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
Source2:        https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz.sig
Source3:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-scanner)
BuildArch:      noarch

%description
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that adds functionality not available in the core protocol
Group:          Development/Libraries/C and C++

%description devel
This package contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%prep
%autosetup

%build
%configure

%install
%make_install

%files devel
%doc README
%license COPYING
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/

%changelog
