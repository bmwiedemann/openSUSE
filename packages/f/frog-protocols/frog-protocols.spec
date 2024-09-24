#
# spec file for package frog-protocols
#
# Copyright (c) Neal Gompa
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

Name:           frog-protocols
Version:        0.01
Release:        0
Summary:        Faster moving Wayland protocols

License:        MIT
URL:            https://github.com/misyltoad/frog-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson >= 0.55

# This is a development package so add it for convention
Provides:       %{name}-devel = %{version}-%{release}


%description
%{name} contains Wayland protocol definitions for protocols
being developed in a more agile fashion to enable shipping
functionality to users more quickly. It is intended to
accelerate development of formal Wayland protocols.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE.md
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/


%changelog
