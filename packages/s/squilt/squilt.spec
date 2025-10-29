#
# spec file for package squilt
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           squilt
Version:        20251029.56b4c47
Release:        0
Summary:        A quilt wrapper using nsjail
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/jsegitz/squilt
Source0:        %{name}-%{version}.tar.gz
Requires:       bubblewrap
Requires:       quilt

%description
Wrapper to confine quilt with nsjail

%prep
%setup -q -n %{name}-%{version}

%build
# Fix squilt on Tumbleweed
%if 0%{?suse_version} > 1500
sed -i -e 's@/etc/nsswitch@/usr/etc/nsswitch@g' squilt
%endif

%install
install -Dm 0755 squilt %{buildroot}%{_bindir}/squilt

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/squilt

%changelog
