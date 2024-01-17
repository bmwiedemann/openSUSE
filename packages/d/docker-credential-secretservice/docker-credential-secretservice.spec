#
# spec file for package docker-distribution
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           docker-credential-secretservice
Version:        0.7.0
Release:        0
Summary:        Leverage Docker credentials with libsecret
License:        MIT
Group:          System/Management
Url:            http://www.docker.io
Source0:        docker-credential-helpers-%{version}.tar.xz
Source1:        config.secure.json
BuildRequires:  go >= 1.8.0
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  libsecret-devel
Requires(pre):  %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
Docker by default uses base64 to store the credentials for the different
registries. This behavior can be changed by leveraging the credentials storage
to this program, which uses libsecret in Linux.

%prep
%setup -q -n docker-credential-helpers-%{version}

%build
export GOPATH=$PWD/go
export GOFLAGS="-buildmode=pie"
mkdir -p $GOPATH/src/github.com/docker

cp -r $PWD/vendor/* $GOPATH/src
ln -s $PWD $GOPATH/src/github.com/docker/docker-credential-helpers

export VERSION=v%{version}
export REVISION=
make %{?_smp_mflags} secretservice

%pre
cat >&2 <<EOF

In order to have a more secure installation of Docker, copy the
/etc/docker/config.secure.json file into ~/.docker/config.json. This way Docker
will use libsecret in order to store your credentials when accessing a Docker
Registry.
EOF
exit 0

%install
install -D -m755 bin/build/docker-credential-secretservice %{buildroot}/%{_bindir}/docker-credential-secretservice
install -D -m644 %{SOURCE1} %{buildroot}/etc/docker/config.secure.json

%files
%defattr(-,root,root)
%doc LICENSE README.md MAINTAINERS
%{_bindir}/docker-credential-secretservice
%dir %{_sysconfdir}/docker
%config %{_sysconfdir}/docker/config.secure.json

%changelog
