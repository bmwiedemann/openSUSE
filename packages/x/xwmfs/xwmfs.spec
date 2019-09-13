#
# spec file for package xwmfs
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


Name:           xwmfs
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
Requires:       fuse
Version:        0.83
Release:        0
Patch0:         cxx-one-definition.patch
Url:            https://github.com/gerstner-hub/xwmfs
Summary:        A file system for accessing X server and window manager features
License:        GPL-2.0-or-later
Group:          System/Filesystems
Source0:        https://github.com/gerstner-hub/xwmfs/releases/download/v%{version}/xwmfs-%{version}-dist.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is xwmfs (X window manager file system), a userspace file system based on
fuse that allows interaction with an EWMH compliant X11 window manager via
files.

Some of its features are:

- newly appearing and disappearing windows in the X server are recognized and
  the file system is updated in an event based manner
- new values for properties of window manager and windows will be reflected in
  the file system in an event based manner
- properties of windows and window manager can be changed via writing to files
  in the file system
- some X operations are accessible via control files in the file system
- the file system can be used for easily implementing scripts that operate on
  the window manager and windows (for example identifying specific windows,
  rename a window, move it around and so on).

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
# get rid of wrongly placed README
rm -rf $RPM_BUILD_ROOT/usr/share/doc/xwmfs

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_mandir}/man1/xwmfs.1.gz
%_bindir/xwmfs

%changelog
