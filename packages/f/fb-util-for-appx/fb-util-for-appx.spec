#
# spec file for package fb-util-for-appx
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           fb-util-for-appx
Version:        0.1
Release:        0
License:        BSD-3-Clause
Summary:        Tool creating APPX packages
Url:            https://github.com/facebook/%{name}
Group:          Development/Libraries/Other
Source:         https://github.com/facebook/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tool to create and optionally sign Microsoft Windows APPX packages.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root)
%doc README.md PATENTS
%license LICENSE
%{_bindir}/appx

%changelog
