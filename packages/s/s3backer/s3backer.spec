#
# spec file for package s3backer
#
# Copyright (c) 2020 SUSE LLC
# Copyright 2008 Archie L. Cobbs.
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


Name:           s3backer
Version:        1.5.5
Release:        0
Summary:        FUSE-based single file backing store via Amazon S3
License:        GPL-2.0-or-later
Group:          System/Filesystems
Source:         https://s3.amazonaws.com/archie-public/%{name}/%{name}-%{version}.tar.gz
URL:            https://github.com/archiecobbs/%{name}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1100
BuildRequires:  libcurl-devel >= 7.16.2
BuildRequires:  libopenssl-devel
%else
BuildRequires:  curl-devel >= 7.16.2
BuildRequires:  openssl-devel
%endif
BuildRequires:  fuse-devel >= 2.5
BuildRequires:  zlib-devel
%if 0%{?suse_version} < 1000 || 0%{?fedora_version} != 0 || 0%{?centos_version} != 0
BuildRequires:  expat
%else
BuildRequires:  libexpat-devel
%endif
BuildRequires:  pkgconfig

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

%prep
%setup -q

%build
export SUSE_ASNEEDED=0
%{configure}
make %{?_smp_mflags}

%install
make install DESTDIR='%{buildroot}'
install -m 0644 COPYING %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_docdir}/%{name}

%changelog
