#
# spec file for package bazel-rules-cc
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

Name:           bazel-rules-cc
Version:        20190722
Release:        0
Summary:        C++ rules for Bazel
Group:          Development/Tools/Building
License:        Apache-2.0
Url:            https://github.com/bazelbuild/rules_cc
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildArch:      noarch

%description
Bazel rules which support building software written in C++.

%package source
Summary:        Source code of bazel-rules-cc
Group:          Development/Sources

%description source
Bazel rules which support building software written in C++.

This package contains source code of bazel-rules-cc.

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

