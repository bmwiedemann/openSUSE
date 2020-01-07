#
# spec file for package bazel-rules-swift
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

Name:           bazel-rules-swift
Version:        0.13.0
Release:        0
Summary:        Swift rules for Bazel
License:        Apache-2.0
Url:            https://github.com/bazelbuild/rules_swift
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
Bazel rules which support building software written in Swift.

%package source
Summary:        Source code of bazel-rules-swift

%description source
Bazel rules which support building software written in Swift.

This package contains source code of bazel-rules-swift.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -R * %{buildroot}%{src_install_dir}
fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

