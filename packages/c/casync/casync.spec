#
# spec file for package casync
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


%define revision_short a8f6c841
%define revision a8f6c841ccfe59ca8c68aad64df170b64042dce8
Name:           casync
Version:        2+%{revision_short}
Release:        0
Summary:        Content Addressable Data Synchronization Tool
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/systemd/casync
#Source0:        https://github.com/systemd/casync/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/systemd/casync/archive/%{revision}.zip#/%{name}-%{version}.zip
# PATH-FIX-OPENSUSE compiler_error_nonnull.patch -- fix for nonnull gcc error, see https://github.com/systemd/casync/issues/83
Patch0:         compiler_error_nonnull.patch
BuildRequires:  cmake
BuildRequires:  diffutils
BuildRequires:  gcc >= 5
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libzstd-devel
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcurl) >= 7.32.0
BuildRequires:  pkgconfig(liblzma) >= 5.1.0
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64

%description
casync provides a way to efficiently transfer files which change over
time over the Internet. It will split a given set into a git-inspired
content-addressable set of smaller compressed chunks, which can then
be conveniently transferred using HTTP. On the receiving side, these
chunks will be uncompressed and merged together to recreate the
original data. When the original data is modified, only the new chunks
have to be transferred during an update.

%prep
%setup -qn %{name}-%{revision}
%patch0 -p1

%build
%meson
%meson_build

%check
%{meson_test}

%install
%meson_install

%files
%license LICENSE.LGPL2.1
%doc NEWS README.md TODO
%{_bindir}/casync
%dir %{_prefix}/lib/casync
%dir %{_prefix}/lib/casync/protocols
%{_prefix}/lib/casync/protocols/casync-ftp
%{_prefix}/lib/casync/protocols/casync-sftp
%{_prefix}/lib/casync/protocols/casync-http
%{_prefix}/lib/casync/protocols/casync-https
%{_prefix}/lib/udev/rules.d/75-casync.rules
%{_mandir}/man1/casync.1%{?ext_man}
%{_datadir}/bash-completion/completions/casync

%changelog
