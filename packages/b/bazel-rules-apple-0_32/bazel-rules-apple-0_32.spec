#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define base_name bazel-rules-apple
# Since bazel-rules-apple follows semantic versioning,
# it should be enough if we make a package for each major version.
%define version_postfix 0_32

Name:           bazel-rules-apple-%{version_postfix}
Version:        0.32.0
Release:        0
Summary:        Bazel rules to build software for Apple platforms
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/bazelbuild/rules_apple
Source0:        https://github.com/bazelbuild/rules_apple/releases/download/0.32.0/rules_apple.0.32.0.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Bazel rules to build software for Apple platforms.

%package source
Summary:        Source code of bazel-rules-apple
BuildArch:      noarch

%description source
Bazel rules to build software for Apple platforms.

This package contains source code for bazel-rules-apple.

%prep
%setup -qc

sed -i "s|!/usr/bin/env python3|!/usr/bin/python3|" test/testdata/fmwk/generate_framework.py

%build
chmod -x **/*.md

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
