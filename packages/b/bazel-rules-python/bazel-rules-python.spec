#
# spec file for package bazel-rules-python
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

Name:           bazel-rules-python
Version:        0.0.1
Release:        0
Summary:        Python rules for Bazel
License:        Apache-2.0
Url:            https://github.com/bazelbuild/rules_python
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Bazel rules for packaging and distributing software written in Python.

%package source
Summary:        Source code of bazel-rules-python
Group:          Development/Sources
BuildArch:      noarch

%description source
Bazel rules for packaging and distributing software written in Python.

This package contains source code of bazel-rules-python.

%prep
%setup -q
# Yes, someone really added an executable bit to markdown files...
chmod -x docs/*.md

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -R * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

