#
# spec file for package envoy-protoc-gen-validate
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


%global provider        github
%global provider_tld    com
%global project         envoyproxy
%global repo            protoc-gen-validate
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           envoy-protoc-gen-validate
Version:        20190522
Release:        0
Summary:        Envoy's fork of protoc plugin to generate message validators
License:        Apache-2.0
Group:          Development/Languages/Golang
Url:            https://github.com/envoyproxy/protoc-gen-validate
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.10

%description
protoc-gen-validate is a protoc plugin to generate polyglot message validators.
While protocol buffers effectively guarantee the types of structured data, they
cannot enforce semantic rules for values. This plugin adds support to
protoc-generated code to validate such constraints.

This package ships a fork of protoc-gen-validate developed by envoy-proxy
developers.

%package source
Summary:        Source code of envoy-protoc-gen-validate
Group:          Development/Sources
BuildArch:      noarch

%description source
protoc-gen-validate is a protoc plugin to generate polyglot message validators.
While protocol buffers effectively guarantee the types of structured data, they
cannot enforce semantic rules for values. This plugin adds support to
protoc-generated code to validate such constraints.

This package contains source code of envoy-protoc-gen-validate - a fork of
protoc-gen-validate developed by envoy-proxy developers.

%prep
%setup -q

%build
%goprep %{provider_prefix}
%gobuild .

%install
%goinstall
# Avoid conflict with protoc-gen-validate binary.
mv %{buildroot}%{_bindir}/protoc-gen-validate %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{src_install_dir}
cp -R * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files source
%{src_install_dir}

%changelog

