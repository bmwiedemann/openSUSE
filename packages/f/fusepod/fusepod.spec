#
# spec file for package fusepod
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fusepod
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libgpod-devel
BuildRequires:  pkgconfig
BuildRequires:  taglib-devel
Requires:       fuse
Summary:        FUSEPod is a virtual user-space filesystem that mounts your iPod
License:        GPL-2.0+
Group:          System/Filesystems
Version:        0.5.2
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch:          include_fix.patch
Url:            http://sourceforge.net/projects/fusepod/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FUSEPod is a virtual user-space filesystem that mounts your iPod into a
directory for easy browsing of the songs it contains. It can discover
where your iPod is mounted, supports read and remove operations, and
has a configurable directory layout.

%prep
%setup -q
%patch

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS README* THANKS
%{_bindir}/*
%{_mandir}/man1/fusepod.1.gz

%changelog
