#
# spec file for package s3fs
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           s3fs
Version:        1.96
Release:        0
Summary:        FUSE file system backed by Amazon S3 bucket
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(fuse3) >= 3.0.0
BuildRequires:  pkgconfig(libcrypto) >= 0.9
BuildRequires:  pkgconfig(libcurl) >= 7.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
Requires:       fuse3

%description
FUSE-based file system backed by Amazon S3. Mount a bucket as a local
file system read/write. Store files/folders natively and transparently

%prep
%autosetup -p1 -n s3fs-fuse-%{version}

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1%{?ext_man}

%changelog
