#
# spec file for package host-spawn
#
# Copyright (c) 2024 SUSE LLC
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


Name:           host-spawn
Version:        1.6.0
Release:        0
Summary:        A reimplementation of flatpak-spawn --host
License:        MIT-0
URL:            https://github.com/1player/host-spawn
Source0:        %{name}-v%{version}.tar.zst
Source1:        vendor.tar.zst
# Go packaging wiki suggests golang-packaging, but this does not work on 15.5
BuildRequires:  golang(API) >= 1.18
BuildRequires:  zstd

%description
Run commands on your host machine from inside your flatpak sandbox, toolbox or distrobox containers.

%prep
%autosetup -p1 -a1 -n %{name}-v%{version}

%build
# https://github.com/1player/host-spawn/blob/master/build.sh#L22
CGO_ENABLED=0 go build \
   -ldflags  "-X main.Version=%{version}" \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
