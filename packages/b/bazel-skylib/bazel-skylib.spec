#
# spec file for package bazel-skylib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define src_install_dir /usr/src/%{name}

Name:           bazel-skylib
Version:        0.9.0
Release:        0
Summary:        Set of functions for writing Bazel build rules with Skylark
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/bazelbuild/bazel-skylib
Source:         %{name}-%{version}.tar.xz

%description
Skylib is a standard library that provides functions for manipulating
collections, file paths, and common features for writing custom build rules in
Bazel.

%package source
Summary:        Source code of bazel-skylib
Group:          Development/Sources
BuildArch:      noarch

%description source
Skylib is a standard library that provides functions for manipulating
collections, file paths, and common features for writing custom build rules in
Bazel.

This package contains source code of Skylib.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
