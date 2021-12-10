# spec file for package runsc
#
# Copyright (c) 2021 Orville Q. Song <orville@anislet.dev>
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
%global project         google
%global repo            gvisor
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           runsc
Version:        20211129.0
Release:        0
Summary:        The gVisor OCI Container Runtime
License:        Apache-2.0
Group:          System/Management
URL:            https://gvisor.dev
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
Source2:        %{name}-containerd.toml
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16
ExclusiveArch:	x86_64 aarch64

%description
gVisor is an application kernel for containers that provides efficient defense-in-depth anywhere.

%package containerd
Summary:        Containerd config file for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    (%{name} and containerd)
BuildArch:      noarch

%description containerd
The default Containerd config file for %{name}.

%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
sed -i 's/VERSION_MISSING/release-${version}/g' ./runsc/version.go
%gobuild -mod=vendor -ldflags "-s -w" ./runsc/
ln -s shim containerd-shim-runsc-v1
%gobuild -mod=vendor -ldflags "-s -w" ./containerd-shim-runsc-v1/

%install
install -D -m0755 %{_builddir}/go/bin/runsc %{buildroot}%{_sbindir}/runsc
install -D -m0755 %{_builddir}/go/bin/containerd-shim-runsc-v1 %{buildroot}%{_sbindir}/containerd-shim-runsc-v1

# Install toml file
install -D -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/containerd/runtime-%{name}.toml

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_sbindir}/containerd-shim-runsc-v1
%{_sbindir}/runsc

%files containerd
%defattr(-,root,root)
%dir %{_sysconfdir}/containerd
%config %{_sysconfdir}/containerd/runtime-%{name}.toml

%changelog
