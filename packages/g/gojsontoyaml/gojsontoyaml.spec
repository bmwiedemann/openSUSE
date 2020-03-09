#
# spec file for package gojsontoyaml
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gojsontoyaml
Version:        0.0+git20191212.bf2969b
Release:        0
Summary:        Tool to convert json to yaml
License:        MIT
URL:            https://github.com/brancz/gojsontoyaml
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.13

%description
This is a small tool to convert json to yaml reading from STDIN and writing to STDOUT.

%prep
%setup -qa1

%build
go build -o gojsontoyaml -mod vendor -buildmode=pie main.go

%install
# Install the binary.
mkdir -p %{buildroot}%{_bindir}/
install -m 0755 gojsontoyaml %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/gojsontoyaml

%changelog
