#
# spec file for package protoc-gen-go
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
%global project         golang
%global repo            protobuf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           protoc-gen-go
Version:        1.2.0
Release:        0
Summary:        Go support for Google's protocol buffers
License:        BSD-3-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bazel-rules-go-source
BuildRequires:  golang-packaging
%{go_provides}

%description
protoc-gen-go implements Go bindings for protocol buffers. For information
about protocol buffers themselves, see
https://developers.google.com/protocol-buffers/

%package source
Summary:        Source code of protoc-gen-go
Group:          Development/Sources
BuildArch:      noarch

%description source
protoc-gen-go implements Go bindings for protocol buffers. For information
about protocol buffers themselves, see
https://developers.google.com/protocol-buffers/

This package contains source code for protoc-gen-go.

%prep
%setup -q

%build
%goprep %{provider_prefix}
%gobuild %{name}

%install
%goinstall

# Install sources
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Apply patches for Bazel support
patch -p1 -d %{buildroot}%{src_install_dir} < /usr/src/bazel-rules-go/third_party/com_github_golang_protobuf-gazelle.patch
patch -p1 -d %{buildroot}%{src_install_dir} < /usr/src/bazel-rules-go/third_party/com_github_golang_protobuf-extras.patch
echo 'workspace(name = "com_github_golang_protobuf")' > %{buildroot}%{src_install_dir}/WORKSPACE

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files source
%{src_install_dir}

%changelog

