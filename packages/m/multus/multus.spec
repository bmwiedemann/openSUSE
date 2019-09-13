#
# spec file for package multus
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           multus
Version:        3.1
Release:        0
Summary:        CNI plugin providing multiple interfaces in containers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/intel/multus-cni
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.8

%description
Multus is a CNI plugin which provides multiple network interfaces in
containers. It allows to use many CNI plugins at the same time and supports all
plugins which implement the CNI specification.

%prep
%setup -q

%build
./build

%install
install -D -m0755 bin/multus %{buildroot}%{_bindir}/multus
install -D -m0755 images/entrypoint.sh %{buildroot}%{_bindir}/multus-entrypoint

%files
%license LICENSE
%doc README.md
%{_bindir}/multus
%{_bindir}/multus-entrypoint

%changelog

