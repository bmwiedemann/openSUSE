#
# spec file for package bazel-rules-foreign-cc
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

Name:           bazel-rules-foreign-cc
Version:        20190214
Release:        0
Summary:        Build rules for interfacing with non-Bazel build systems
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/bazelbuild/rules_foreign_cc
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Rules for building C/C++ projects using foreign build systems inside Bazel
projects.

%package source
Summary:        Source code of bazel-rules-foreign-cc
Group:          Development/Sources
BuildArch:      noarch

%description source
Rules for building C/C++ projects using foreign build systems inside Bazel
projects.

This package contains source code of bazel-rules-foreign-cc.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix non-executable-script warning.
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec chmod +x "{}" +
# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!/usr/bin/env bash|#!/bin/bash|' "{}" +
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

