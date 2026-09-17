#
# spec file for package bazel-rules-pkg
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define src_install_dir %{_prefix}/src/%{name}
%define base_name bazel-rules-pkg
# Tag 1.3 ships artifact version 1.3.0
%define upstream_tag 1.3
Name:           %{base_name}
Version:        1.3.0
Release:        0
Summary:        Bazel rules for building tar, zip, deb, and rpm for packages
License:        Apache-2.0
URL:            https://github.com/bazelbuild/rules_pkg
Source0:        https://github.com/bazelbuild/rules_pkg/releases/download/%{upstream_tag}/rules_pkg-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  unzip

%description
Bazel rules for building tar, zip, deb, and rpm for packages.

%package source
Summary:        Source code of bazel-rules-pkg
BuildArch:      noarch

%description source
Bazel rules for building tar, zip, deb, and rpm for packages.

This package contains source code for bazel-rules-pkg.

%prep
%setup -qc

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%{src_install_dir}

%changelog
