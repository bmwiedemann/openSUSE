#
# spec file for package fuse-overlayfs
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


Name:           fuse-overlayfs
Version:        1.10
Release:        0
Summary:        FUSE implementation for overlayfs
License:        GPL-3.0-only
Group:          System/Management
URL:            https://github.com/containers/fuse-overlayfs
Source0:        https://github.com/containers/fuse-overlayfs/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse3-devel
BuildRequires:  gcc

%description
An implementation of overlay+shiftfs in FUSE for rootless containers.

%prep
%setup -q

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install INSTALL="install -p"

%files
# Binaries
%{_bindir}/fuse-overlayfs
%doc README.md
%license COPYING
%doc %{_mandir}/man1/%{name}.1.gz

%changelog
