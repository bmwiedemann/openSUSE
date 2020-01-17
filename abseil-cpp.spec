#
# spec file for package abseil-cpp
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define src_install_dir /usr/src/%{name}

Name:           abseil-cpp
Version:        20190808
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
URL:            https://abseil.io/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
ExcludeArch:    %ix86

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package source
Summary:        Source code of Abseil

%description source
Source code of Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
