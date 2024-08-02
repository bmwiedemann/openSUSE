#
# spec file for package termscp
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


Name:           termscp
Version:        0.14.0
Release:        0
Summary:	Feature rich terminal UI file transfer and explorer
License:        MIT
URL:            https://github.com/veeso/termscp
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM dfe58e6147f66b4c0c74874c954e7d101b3bf026.patch
# https://github.com/veeso/termscp/issues/271
Patch1:         dfe58e6147f66b4c0c74874c954e7d101b3bf026.patch
BuildRequires:  cargo-packaging
BuildRequires:  zstd
BuildRequires:  cargo >= 1.77
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(smbclient)

# error[E0063]: missing fields `bavail`, `bfree`, `blocks` and 3 other fields in initializer of `types::stat::SmbStatVfs`
#
ExcludeArch: i586 ppc64le s390x

%description
Termscp is a feature rich terminal file transfer and explorer, with support for
SCP/SFTP/FTP/Kube/S3/WebDAV. So basically is a terminal utility with an TUI to
connect to a remote server to retrieve and upload files and to interact with
the local file system. It is Linux, MacOS, FreeBSD, NetBSD and Windows
compatible.

%prep
%autosetup -a 1 -p 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
