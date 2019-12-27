#
# spec file for package bazel-compilation-database
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           bazel-compilation-database
Version:        0.4.1
Release:        0
Summary:        Clang JSON Compilation Database generator for Bazel
License:        Apache-2.0 
Group:          Development/Tools/Building
Url:            https://github.com/grailbio/bazel-compilation-database
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes

%description
A JSON Compilation Database generator following the Clang specification
for Bazel.

%package source
Summary:        Source code of bazel-compilation-database
Group:          Development/Sources
BuildArch:      noarch

%description source
A JSON Compilation Database generator following the Clang specification
for Bazel.

This package contains source code of bazel-compilation-database.

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

