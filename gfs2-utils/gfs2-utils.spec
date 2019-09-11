#
# spec file for package gfs2-utils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gfs2-utils
Version:        3.1.9
Release:        0
Summary:        Utilities for managing the global file system (GFS2)
License:        GPL-2.0+ and LGPL-2.0+
Group:          System/Filesystems
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  check-devel
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  kernel-headers
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
Url:            https://fedorahosted.org/cluster/wiki/HomePage

# The source for this package was pulled from the upstream git tree.
# Use the following commands to generate the tarball:
# git clone git://git.fedorahosted.org/gfs2-utils.git
# cd gfs2-utils
# ./make-tarball.sh
#
Source0:        https://fedorahosted.org/released/gfs2-utils/%{name}-%{version}.tar.xz
#Source0:        gfs2-utils-%{version}.tar.gz

%description
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
file systems.

%prep
%setup -q 

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{_smp_mflags}

#%check
#make check

%install
rm -rf %{buildroot}
make -C gfs2 install DESTDIR=%{buildroot}
# Don't ship gfs2_{trace,lockcapture} in this package
rm -f %{buildroot}%{_sbindir}/gfs2_trace
rm -f %{buildroot}%{_sbindir}/gfs2_lockcapture
rm -f %{buildroot}%{_mandir}/man8/gfs2_trace.8
rm -f %{buildroot}%{_mandir}/man8/gfs2_lockcapture.8

%files
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.* doc/*.txt
%dir /usr/lib/udev
%dir /usr/lib/udev/rules.d
%{_sbindir}/fsck.gfs2
%{_sbindir}/glocktop
%{_sbindir}/mkfs.gfs2
%{_sbindir}/tunegfs2
%{_sbindir}/gfs2_*
/usr/lib/udev/rules.d/82-gfs2-withdraw.rules
%{_mandir}/man8/*gfs2*
%{_mandir}/man5/*
%{_mandir}/man8/glocktop.8.gz

%changelog
