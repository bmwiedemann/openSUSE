#
# spec file for package deltafs
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           deltafs
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  pkg-config
Requires:       fuse
Summary:        Delta Filesystem
Version:        1.0
Release:        0
License:        GPL-2.0
Group:          System/Filesystems
Source:         %{name}-%{version}.tar.bz2
Url:            http://git.kernel.org/?p=linux/kernel/git/mszeredi/deltafs.git
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deltafs combines a read-only lower directory and a read-write upper
directory into a new filesystem.  Currently it works very similarly to
a union filesystem, where upon modification whole files are copied up
to the upper layer.  There are plans to store differences more
efficiently in the future.

%prep
%setup -n %{name}-%{version}

%build
%{?suse_update_config:%{suse_update_config -f}}
aclocal
autoheader
automake --foreign --add-missing
autoconf
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/*/*
%{_bindir}/*

%changelog
