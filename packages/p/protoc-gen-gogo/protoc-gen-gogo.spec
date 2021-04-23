#
# spec file for package protoc-gen-gogo
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


%global provider        github
%global provider_tld    com
%global project         gogo
%global repo            protobuf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           protoc-gen-gogo
Version:        1.2.0
Release:        0
Summary:        Fork of protoc-gen-go - Go support for Google's protocol buffers
License:        Apache-2.0
Group:          Development/Languages/Golang
Url:            https://github.com/gogo/protobuf
Source0:        %{name}-%{version}.tar.xz
Source100:      BUILD
Source101:      WORKSPACE
BuildRequires:  fdupes
BuildRequires:  golang-packaging
%{go_provides}

%description
protoc-gen-gogo is a fork of protoc-gen-go. It implements Go bindings for
protocol buffers and provides more generation features than protoc-gen-go.

%package source
Summary:        Source code of protoc-gen-gogo
Group:          Development/Sources
BuildArch:      noarch

%description source
protoc-gen-gogo is a fork of protoc-gen-go. It implements Go bindings for
protocol buffers and provides more generation features than protoc-gen-go.

This package contains source code for protoc-gen-go.

%prep
%setup -q
cp %{SOURCE100} .
cp %{SOURCE101} .

%build
%goprep %{provider_prefix}
%gobuild %{name}

%install
%goinstall

# Install sources
mkdir -p %{buildroot}%{src_install_dir}
cp -R * %{buildroot}%{src_install_dir}
# Fix env-script-interpreter rpmlint error
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!.*/usr/bin/env bash|#!/bin/bash|' "{}" +

%fdupes %{src_install_dir}

%files
%license LICENSE
%doc README
%{_bindir}/%{name}

%files source
%{src_install_dir}

%changelog
