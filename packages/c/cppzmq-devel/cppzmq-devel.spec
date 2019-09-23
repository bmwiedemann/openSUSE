#
# spec file for package cppzmq-devel
#
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           cppzmq-devel
Version:        0.0.0+git.20170110.178a910
Release:        0
Summary:        A C++ binding for 0MQ
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/zeromq/cppzmq
Source:         cppzmq-%{version}.tar.xz
#needs a czmq version first
#BuildRequires:  cmake
#BuildRequires:  gcc-c++
#BuildRequires:  zeromq-devel
Requires:       zeromq-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A simple C++ binding for 0MQ

%prep
%setup -q -n cppzmq-%{version}

%build

%install
mkdir -p %{buildroot}%{_includedir}/
install -m 644 *.hpp %{buildroot}%{_includedir}/

%files
%defattr(-,root,root)
%doc LICENSE README
%{_includedir}/*.hpp

%changelog
