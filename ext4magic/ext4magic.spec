#
# spec file for package ext4magic
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 robi@users.berlios.de
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


Name:           ext4magic
Version:        0.3.2
Release:        0
Summary:        Tool for recovering deleted files on ext3/4 filesystems
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://sourceforge.net/projects/ext4magic/
#Doc_Url:	http://ext4magic.sourceforge.net/ext4magic_en.html
Source0:        http://sourceforge.net/projects/ext4magic/files/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ext4magic-0.3.2-rename-i_dir_acl.patch -- Fix FTBFS (boo#1115053)
Patch0:         ext4magic-0.3.2-rename-i_dir_acl.patch
# PATCH-FIX-UPSTREAM Fix-undefined-reference-to-makedev.patch
Patch1:         Fix-undefined-reference-to-makedev.patch
BuildRequires:  file-devel > 5.05
BuildRequires:  libblkid-devel
BuildRequires:  libbz2-devel
BuildRequires:  zlib-devel

%if 0%{?suse_version} || 0%{?fedora_version} || 0%{?rhel_version}
BuildRequires:  libuuid-devel
%else
BuildRequires:  uuid-devel
%endif

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  e2fsprogs-devel
%else
BuildRequires:  libext2fs-devel >= 1.42.6
%endif

%description
ext4magic is a tool which can help recover accidentally deleted or
overwritten files from ext3 or ext4 file systems. Especially private
computers may lack an adequate, frequent or reliable backup.

%prep
%autosetup -p1

%build
%configure \
 --enable-file-attr \
 --enable-expert-mode
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_sbindir}/ext4magic
%{_mandir}/man8/ext4magic.8%{?ext_man}

%changelog
