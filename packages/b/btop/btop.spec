#
# spec file for package btop
#
# Copyright (c) 2022 SUSE LLC
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


Name:           btop
Version:        1.2.0
Release:        0
Summary:        Usage and stats for processor, memory, disks, network and processes
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/aristocratos/btop
Source:         %{url}/archive/v%{version}.tar.gz#/v%{version}.tar.gz
BuildRequires:  coreutils
%if 0%{?suse_version} < 1550
%define cxxopt CXX=g++-10
BuildRequires:  gcc10-c++
%else
%define cxxopt %{nil}
BuildRequires:  gcc-c++ >= 11
%endif
BuildRequires:  sed

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes. C++ version and continuation of bashtop and bpytop.

%prep
%setup -q

%build
%make_build %{cxxopt}

%install
%make_install PREFIX=/usr

%files
/usr/bin/btop
%dir /usr/share/btop
%dir /usr/share/btop/themes
/usr/share/btop/README.md
/usr/share/btop/themes/*.theme
%license LICENSE
%doc CHANGELOG.md

%changelog
