#
# spec file for package docker-compose-switch
#
# Copyright (c) 2022 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
Name:           docker-compose-switch
Version:        1.0.5
Release:        0
Summary:        Replacement for the docker-compose (python) executable
License:        Apache-2.0
URL:            https://github.com/docker/compose-switch
Source:         compose-switch-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       docker-compose-switch-rpmlintrc
BuildRequires:  golang(API) = 1.18
Requires:       docker
Requires:       docker-compose >= 2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Docker Compose V2 is a major version bump release of Docker Compose.
# It has been completely rewritten from scratch in Golang (V1 was in Python).
Obsoletes:      python2-docker-compose < 2.0.0
Obsoletes:      python3-docker-compose < 2.0.0
Obsoletes:      python36-docker-compose < 2.0.0
Obsoletes:      python37-docker-compose < 2.0.0
Obsoletes:      python38-docker-compose < 2.0.0
Obsoletes:      python39-docker-compose < 2.0.0
Obsoletes:      python310-docker-compose < 2.0.0

%description
Compose Switch is a replacement to the Compose V1 docker-compose (python) executable. It translates the command line into Compose V2 docker compose then run the latter.

%prep
%setup -q -a1 -n compose-switch-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags="-s -w -X github.com/docker/compose-switch/v2/internal.Version=%{version}" \
   -o bin/docker-compose-switch .

%install
install -D -m 0755 bin/%{name} "%{buildroot}%{_bindir}/%{name}"
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/docker-compose %{buildroot}%{_bindir}/docker-compose

%post
update-alternatives --install \
   %{_bindir}/docker-compose docker-compose %{_bindir}/%{name} 2000

%postun
if [ ! -f %{_bindir}/%{name} ] ; then
   update-alternatives --remove docker-compose %{_bindir}/%{name}
fi

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/docker-compose
%ghost %{_sysconfdir}/alternatives/docker-compose

%changelog
