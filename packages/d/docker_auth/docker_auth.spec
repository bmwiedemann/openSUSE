#
# spec file for package docker_auth
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


Name:           docker_auth
Version:        1.4.0+git20190925.6f38360
Release:        0
Summary:        Authenticaton for container registry with tokens
License:        Apache-2.0
URL:            https://github.com/cesanta/docker_auth
Source:         docker_auth-%{version}.tar.xz
BuildRequires:  golang(API) = 1.12
BuildRequires:  go1.12 >= 1.12.9

%description
This package contains a tool to authenticate the access to
a container registry. Access is granted defined by an access
control list for every user.

%prep
%setup -q
rm chart/docker-auth/.helmignore

%build
cd auth_server
# Make the go command working in OBS and on all architectures:
sed -i -e 's|CGO_ENABLED=0 go build -v --ldflags=--s|go build -mod vendor -buildmode=pie -v|g' Makefile
make

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 auth_server/auth_server %{buildroot}%{_sbindir}/

%files
%license LICENSE
%doc README.md chart docs examples
%{_sbindir}/auth_server

%changelog
