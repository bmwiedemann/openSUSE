#
# spec file for package ccgfs
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


Name:           ccgfs
Version:        0.81.g3
Release:        0
Summary:        Transport-agnostic network filesystem
License:        GPL-3.0-only
Group:          System/Filesystems
URL:            https://inai.de/projects/ccgfs/
#Git-Clone:	https://codeberg.org/jengelh/ccgfs
#Source:        https://inai.de/files/ccgfs/ccgfs-0.81.tar.xz
Source:         %name-%version.tar.xz
Source3:        %name.keyring
BuildRequires:  automake
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig >= 0.19
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(fuse) >= 2.6.5
BuildRequires:  pkgconfig(libHX) >= 3.12
BuildRequires:  pkgconfig(libcrypto) >= 0.9.7
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6

%description
ccgfs is a transport-agnostic filesystem. Common transport modes are
"pull" and "push", the latter of which makes it possible to export a
filesystem located in a LAN to a DMZ host without needing to allow
connections from the DMZ as would be the case with the pull model.
Any transport can be used, e.g. ssh for encryption.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install unitdir="%{?_unitdir}"
# Remove unwanted sysvinit script if system provides systemd support
rm -Rfv "%buildroot/%_initddir"

%pre
%service_add_pre ccgfs-super.service

%post
%service_add_post ccgfs-super.service

%preun
%service_del_preun ccgfs-super.service

%postun
%service_del_postun ccgfs-super.service

%files
%_unitdir/*.service
%_sbindir/*
%doc doc/*.txt
%doc %_mandir/*/*

%changelog
