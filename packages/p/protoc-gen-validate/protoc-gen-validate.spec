#
# spec file for package protoc-gen-validate
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global provider        github
%global provider_tld    com
%global project         lyft
%global repo            protoc-gen-validate
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           protoc-gen-validate
Version:        0.0.12
Release:        0
Summary:        Protoc plugin to generate polyglot message validators
License:        Apache-2.0
Group:          Development/Languages/Golang
Url:            https://github.com/lyft/protoc-gen-validate
Source0:        %{name}-%{version}.tar.xz
Source1:        protoc-gen-validate-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.10

%description
protoc-gen-validate is a protoc plugin to generate polyglot message validators.
While protocol buffers effectively guarantee the types of structured data, they
cannot enforce semantic rules for values. This plugin adds support to
protoc-generated code to validate such constraints.

%package source
Summary:        Source code of protoc-gen-validate
Group:          Development/Sources
BuildArch:      noarch

%description source
protoc-gen-validate is a protoc plugin to generate polyglot message validators.
While protocol buffers effectively guarantee the types of structured data, they
cannot enforce semantic rules for values. This plugin adds support to
protoc-generated code to validate such constraints.

This package contains source code for protoc-gen-validate.

%prep
%setup -q

%build
%goprep %{provider_prefix}
%gobuild .

%install
%goinstall

mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix env-script-interpreter rpmlint error
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!.*/usr/bin/env bash|#!/bin/bash|' "{}" +
# Remove executable bits from json files
find %{buildroot}%{src_install_dir} -type f -name "*.json" -exec chmod -x "{}" +

%fdupes %{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files source
%{src_install_dir}

%changelog
