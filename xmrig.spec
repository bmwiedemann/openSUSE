#
# spec file for package xmrig
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xmrig
Version:        6.6.2
Release:        0
Summary:        XMR mining application
License:        GPL-3.0-only
URL:            https://xmrig.com/
Source0:        %{name}-%{version}.tar.gz
#PATCH-FEATURE disable-forced-donation.patch nopeinomicon@posteo.net -- Removes forced donation to developers
Patch0:         disable-forced-donation.patch
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libuv-devel
BuildRequires:  make

%description
Open source CPU/GPU XMR cryptocurrency miner.

%prep
%setup -q
%patch0 -p1

%build
%cmake -DWITH_EMBEDDED_CONFIG=YES
%cmake_build

%install
install -D -m 0755 build/xmrig %{buildroot}%{_bindir}/xmrig

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/xmrig

%changelog
