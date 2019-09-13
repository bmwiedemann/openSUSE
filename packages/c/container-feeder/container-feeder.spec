#
# spec file for package container-feeder
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
%global project         kubic-project
%global repo            container-feeder
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           container-feeder
Version:        4.0.0+20181105.git_r92_066ce53
Release:        0
Summary:        Load container images from RPMs into different container engines
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubic-project/container-feeder
Source:         master.tar.gz
Source1:        sysconfig.%{name}
Source2:        %{name}.service
Source3:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  device-mapper-devel
BuildRequires:  fdupes
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  libassuan-devel
BuildRequires:  libbtrfs-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  golang(API) >= 1.11
# go1.11.3 contains sec. fixes bsc#1118897(CVE-2018-16873) bsc#1118897(CVE-2018-16873) bsc#1118899(CVE-2018-16875)
BuildRequires:  go1.11 >= 1.11.3
Requires:       docker-kubic
Requires:       libcontainers-common
Requires:       libcontainers-image
Requires:       libcontainers-storage
Requires:       libgpgme11
Requires:       xz
Requires(post): %fillup_prereq
%{?systemd_requires}
%{go_nostrip}
%{go_provides}

%description
Load container images in the Docker archive format, installed by RPMs, into
different container engines, such as docker or crio (containers/storage).

%prep
%setup -q -n container-feeder-master

%build
export GOPATH=$HOME/go
mkdir -p $HOME/go/src/%{import_path}
rm -rf $HOME/go/src/%{import_path}/*
cp -ar * $HOME/go/src/%{import_path}
cd $HOME/go/src/%{import_path}

go build -tags "containers_image_ostree_stub seccomp apparmor"          -o bin/container-feeder          main.go

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only -n %{name}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%install
cd $HOME/go/src/%{import_path}
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 container-feeder.json %{buildroot}/%{_sysconfdir}/container-feeder.json

mkdir -p %{buildroot}/%{_fillupdir}
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_fillupdir}

mkdir -p %{buildroot}/%{_unitdir}
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/
mkdir -p %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}

%fdupes %{buildroot}/%{_prefix}

%files
%doc README.md
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%config(noreplace) %{_sysconfdir}/container-feeder.json

%changelog
