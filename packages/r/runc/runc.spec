#
# spec file for package runc
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
# nodebuginfo


# MANUAL: Make sure you update this each time you update runc.
%define git_version d7735e388ef5eecbd60d93bfbe5afe0f3fbc8a6b
%define git_short   d7735e388ef5

%define project github.com/opencontainers/runc

Name:           runc
Version:        1.2.1
%define upstream_version %{version}
Release:        0
Summary:        Tool for spawning and running OCI containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/opencontainers/runc
Source0:        https://github.com/opencontainers/runc/releases/download/v%{upstream_version}/runc.tar.xz#/runc-%{upstream_version}.tar.xz
Source1:        https://github.com/opencontainers/runc/releases/download/v%{upstream_version}/runc.tar.xz.asc#/runc-%{upstream_version}.tar.xz.asc
Source2:        runc.keyring
BuildRequires:  diffutils
BuildRequires:  fdupes
BuildRequires:  go >= 1.22.4
BuildRequires:  go-go-md2man
BuildRequires:  libseccomp-devel
BuildRequires:  libselinux-devel
Recommends:     criu
# There used to be a docker-runc package which was specifically for Docker.
# Since Docker now tracks upstream more consistently, we use the same package
# but we need to obsolete the old one. bsc#1181677
Obsoletes:      docker-runc < %{version}
Provides:       docker-runc = %{version}
# KUBIC-SPECIFIC: There used to be a kubic-specific docker-runc package, but
#                 now it's been merged into the one package. bsc#1181677
Obsoletes:      docker-runc-kubic < %{version}
Provides:       docker-runc-kubic = %{version}
Obsoletes:      docker-runc = 0.1.1+gitr2819_50a19c6
Obsoletes:      docker-runc_50a19c6
ExcludeArch:    s390

# Construct "git describe --dirty --long --always".
%define git_describe v%{upstream_version}-0-g%{git_short}

%description
runc is a CLI tool for spawning and running containers according to the OCI
specification. It is designed to be as minimal as possible, and is the workhorse
of Docker. It was originally designed to be a replacement for LXC within Docker,
and has grown to become a separate project entirely.

%prep
%setup -q -n %{name}-%{upstream_version}
%autopatch -p1

%build
# build runc
make BUILDTAGS="seccomp" COMMIT="%{git_describe}" runc
# build man pages
man/md2man-all.sh

# make sure that our keyring copy is identical to upstream.
our_keyring=$(sha256sum <"%{SOURCE2}")
src_keyring=$(sha256sum <runc.keyring)
if [ "$our_keyring" != "$src_keyring" ]; then
	echo "keyring file doesn't match upstream"
	diff -u "%{SOURCE2}" runc.keyring
	exit 1
fi

%install
# We install to /usr/sbin/runc as per upstream and create a symlink in /usr/bin
# for rootless tools.
install -D -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -m0755 -d %{buildroot}%{_bindir}
ln -s  %{_sbindir}/%{name} %{buildroot}%{_bindir}/%{name}

# Man pages.
install -d -m0755 %{buildroot}%{_mandir}/man8
install -m0644 man/man8/runc*.8 %{buildroot}%{_mandir}/man8

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man8/runc*.8.gz

%changelog
