#
# spec file for package s3backer
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


# Should we try to include NDB support?
%if 0%{?sle_version} >= 150300
%define         include_nbd 1
%define         runfilesdir /run
%define         nbdsockdir  %{runfilesdir}/s3backer-nbd
%define         tmpfileconf s3backer-nbd.conf
%endif

Name:           s3backer
Version:        2.1.3
Release:        0
Summary:        FUSE and NBD single file backing store via Amazon S3
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/archiecobbs/%{name}
Source:         https://s3.amazonaws.com/archie-public/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  fuse-devel >= 2.5
BuildRequires:  libcurl-devel >= 7.16.2
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
%if 0%{?include_nbd}
BuildRequires:  libzstd-devel
%endif
%if 0%{?include_nbd}
BuildRequires:  nbd
BuildRequires:  nbdkit-devel
BuildRequires:  nbdkit-server
Requires:       nbd
Requires:       nbdkit-server
%endif
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
s3backer is a filesystem that contains a single file backed by the Amazon
Simple Storage Service (Amazon S3).  As a filesystem, it is very simple:
it provides a single normal file having a fixed size.  Underneath, the
file is divided up into blocks, and the content of each block is stored
in a unique Amazon S3 object.  In other words, what s3backer provides is
really more like an S3-backed virtual hard disk device, rather than a
filesystem.

In typical usage, a `normal' filesystem is mounted on top of the file
exported by the s3backer filesystem using a loopback mount (or disk image
mount on Mac OS X).

s3backer can also function as a Network Block Device (NBD) plug-in.

%prep
%setup -q

%build
export SUSE_ASNEEDED=0

# This is needed so /usr/sbin/nbdkit, etc. will be found by AC_PATH_PROGS
export PATH="${PATH}:%{_sbindir}"

%configure
%make_build

%install
make install DESTDIR='%{buildroot}'
install -m 0644 COPYING %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%if 0%{?include_nbd}
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{tmpfileconf} << 'xxxEOFxxx'
# See tmpfiles.d(5) for details
d %{nbdsockdir} 0700 root root -
xxxEOFxxx
%endif

%if 0%{?include_nbd}
%post
%tmpfiles_create %{_tmpfilesdir}/%{tmpfileconf}
%endif

%files
%{_bindir}/*
%{_mandir}/man1/*
%if 0%{?include_nbd}
%{_libdir}/nbdkit/plugins/*
%{_tmpfilesdir}/%{tmpfileconf}
%ghost %dir %attr(0700,root,root) %{nbdsockdir}
%endif
%{_docdir}/%{name}

%changelog
