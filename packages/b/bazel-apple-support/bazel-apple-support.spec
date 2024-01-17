#
# spec file for package bazel-apple-support
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

Name:           bazel-apple-support
Version:        0.7.1
Release:        0
Summary:        Bazel rules to support Apple platforms
License:        Apache-2.0
Url:            https://github.com/bazelbuild/apple_support
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Set of helper methods for Bazel that support building rules for Apple platforms.

%package source
Summary:        Source code of bazel-apple-support
BuildArch:      noarch

%description source
Set of helper methods for Bazel that support building rules for Apple platforms.

This package contains source code for bazel-apple-support.

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

