#
# spec file for package squilt-python
#
# Copyright (c) 2025 SUSE LLC
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


Name:           squilt-python
Version:        20230719.dde2b0b
Release:        0
Summary:        A quilt wrapper using nsjail
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/mgerstner/squilt
Source0:        squilt-%{version}.tar.gz
Requires:       nsjail
Requires:       python3
Requires:       quilt
# x86_64 only due to dependency nsjail having ExclusiveArch x86_64
ExclusiveArch:  x86_64
# This package provides an alternative implementation of squilt
Provides:       squilt = %{version}-%{release}
Conflicts:      squilt

%description
Wrapper to confine quilt with nsjail, written in Python

%prep
%setup -q -n squilt-%{version}

%build
# nothing to build

%install
install -Dm 0755 squilt %{buildroot}%{_bindir}/squilt

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/squilt

%changelog
