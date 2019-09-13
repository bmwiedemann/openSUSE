#
# spec file for package ucm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ucm
%define	appdefdir  /usr/share/X11
%define xmandir    /usr/share/man
%define xbindir    /usr/bin
Summary:        Unicode Font Viewer
License:        BSD-3-Clause and MIT
Group:          System/X11/Utilities
Version:        0.3
Release:        0
Requires:       gnu-unifont
Url:            http://www.pps.jussieu.fr/~jch
Source:         http://www.pps.jussieu.fr/~jch/software/files/ucm-0.3.tar.bz2
Patch0:         ucm-0.3.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)

%description
Ucm is a small xfs-like widget specifically designed for Unicode fonts.
 As opposed to xfs, ucm allows you to select an arbitrary character
which can then be pasted into another application or identify an
arbitrary character by pasting it into ucm.

%prep
%setup -q
%patch0 -p 1
head -n 20 ucm.c > License

%build
export CFLAGS="$RPM_OPT_FLAGS" 
xmkmf
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
make install.man DESTDIR=$RPM_BUILD_ROOT

%clean

%files
%defattr(-,root,root)
%doc README License
%{xbindir}/*
%{xmandir}/man1/*
%{appdefdir}/app-defaults

%changelog
