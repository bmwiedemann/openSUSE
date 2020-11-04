#
# spec file for package cel-cpp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define src_install_dir /usr/src/%{name}

Name:           cel-cpp
Version:        20191127
Release:        0
Summary:        C++ Implementation of the Common Expression Language
License:        Apache-2.0
Group:          Development/Libraries/C and C++          
Url:            https://github.com/google/cel-cpp
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes

%description
This is a C++ implementation of a Common Expression Language runtime.

%package source
Summary:        Source code of %{name}
Group:          Development/Sources
BuildArch:      noarch

%description source
This is a C++ implementation of a Common Expression Language runtime.

This package contains source code for %{name}.

%prep
%setup -q

%build
# TODO: If anyone will be interested in compiled cel-cppfor C++
# they need to be built and installed.

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

