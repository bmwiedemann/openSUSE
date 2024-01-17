#
# spec file for package ibdev2netdev
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


%define         git_ver .18.7258568beb9c

Name:           ibdev2netdev
Version:        0.1
Release:        0
Summary:        List netdevs with their associated RDMA interface (IPoIB, RoCE, iWarp)
License:        GPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/nmorey/ibdev2netdev
Source:         %{name}-%{version}%{git_ver}.tar.gz
BuildRequires:  cmake
BuildRequires:  libibverbs-devel

%description
ibdev2netdev lists netdevs with their associated RDMA interface (IPoIB, RoCE, iWarp)

%prep
%setup -q -n  %{name}-%{version}%{git_ver}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_sbindir}/ibdev2netdev

%changelog
