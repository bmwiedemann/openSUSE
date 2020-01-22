#
# spec file for package golang
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Sascha Peilicke <saschpe@gmx.de>
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

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.3.0
Release:        0
Summary:        Go support for Protocol Buffers - Google's data interchange format
License:        BSD-3-Clause
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        WORKSPACE
Patch0:         https://raw.githubusercontent.com/bazelbuild/rules_go/0.18.5/third_party/com_github_golang_protobuf-gazelle.patch
Patch1:         https://raw.githubusercontent.com/bazelbuild/rules_go/0.18.5/third_party/com_github_golang_protobuf-extras.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  golang-packaging
BuildRequires:  xz

BuildRequires:  golang(golang.org/x/sync/errgroup)
Requires:       golang(golang.org/x/sync/errgroup)

%{go_nostrip}
%{go_provides}

%description
This package provides Go support, in the form of a library and protocol compiler
plugin, for Google's protocol buffers. (RPC is not supported.)

%package -n protoc-gen-go
Summary:        Go support for Protocol Buffers - Google's data interchange format
Group:          Development/Languages/Golang
AutoReqProv:    Off

%{go_exclusivearch}

%description -n protoc-gen-go
This package provides Go support, in the form of a library and protocol compiler
plugin, for Google's protocol buffers. (RPC is not supported.)

%prep
%autosetup -n %{repo}-%{version} -p1
tar -zxf %{SOURCE1}
cp %{SOURCE3} .

%build
export GOFLAGS=-mod=vendor
export GO111MODULE=off
%goprep %{import_path}
%gobuild ...

%install
%goinstall
%gosrc
%gofilelist

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md LICENSE AUTHORS CONTRIBUTORS

%files -n protoc-gen-go
%defattr(-,root,root)
%{_bindir}/conformance
%{_bindir}/protoc-gen-go

%changelog
