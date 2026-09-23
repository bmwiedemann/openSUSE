#
# spec file for package kainjow-mustache
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


%define devel_package lib%{name}-devel
Name:           kainjow-mustache
Version:        4.1
Release:        0
Summary:        Mustache text templates for modern C++
License:        BSL-1.0
URL:            https://github.com/kainjow/Mustache
Source:         https://github.com/kainjow/Mustache/archive/refs/tags/v%{version}.tar.gz

%description

A header only implementation of Mustache for C++

%package -n %{devel_package}
Summary:        Development files for %{name}
BuildArch:      noarch

%description -n %{devel_package}
This package containtes the development files for %{name}

%prep
%autosetup -p1 -n Mustache-%{version}

%build

%install
install -D -m 644 -t %{buildroot}%{_includedir} mustache.hpp 

%files -n %{devel_package}
%license LICENSE
%doc README.md
%{_includedir}/mustache.hpp

%changelog

