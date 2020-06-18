#
# spec file for package nvidia-container-toolkit
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


%define project github.com/NVIDIA/container-toolkit
Name:           nvidia-container-toolkit
Version:        0.0+git.1580519869.60f165a
Release:        0
Summary:        NVIDIA Container Toolkit
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/NVIDIA/container-toolkit
Source0:        container-toolkit-%{version}.tar.xz
BuildRequires:  libcontainers-common
BuildRequires:  golang(API) >= 1.12
Requires:       libnvidia-container-tools

%description
Build and run containers leveraging NVIDIA GPUs.

%prep
%setup -q -T -D -b 0 -n container-toolkit-%{version}

%build
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

go build -ldflags "-s -w" \
    -v -buildmode=pie \
    -o bin/nvidia-container-toolkit \
    ./nvidia-container-toolkit

%install
install -D -m 0755 $HOME/go/src/%{project}/bin/nvidia-container-toolkit %{buildroot}/%{_bindir}/nvidia-container-toolkit
install -D -m 0644 oci-nvidia-hook.json %{buildroot}/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json
install -D -m 0644 config/config.toml.opensuse-leap %{buildroot}/etc/nvidia-container-runtime/config.toml

%files
%license LICENSE
%{_bindir}/nvidia-container-toolkit
/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json
/etc/nvidia-container-runtime
%config(noreplace) /etc/nvidia-container-runtime/config.toml

%changelog
