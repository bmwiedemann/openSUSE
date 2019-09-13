#
# spec file for package s3fs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.85
Release:        0
Summary:        FUSE file system backed by Amazon S3 bucket
License:        GPL-2.0-only
Group:          System/Filesystems
Url:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       fuse

%description
FUSE-based file system backed by Amazon S3. Mount a bucket as a local
file system read/write. Store files/folders natively and transparently

%prep
%setup -q -n s3fs-fuse-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{!?_licensedir:%global license %doc}
%license COPYING
%doc ChangeLog README.md
%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1%{ext_man}

%changelog
