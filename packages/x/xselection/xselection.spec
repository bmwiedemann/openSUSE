#
# spec file for package xselection
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


Name:           xselection
Url:            http://sunsite.mff.cuni.cz/MIRRORS/ftp.xfree86.org/pub/mirror/X.Org/R5contrib/
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       xselect
Obsoletes:      xselect
Summary:        Manipulate the XSelection
License:        MIT
Group:          System/X11/Utilities
Version:        1.6.1
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-qt.patch
Patch2:         %{name}-%{version}-help.patch
Patch3:         %{name}-%{version}-warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
With this little tool, pipe the currently selected text under X into a
file or vice versa.

Help can be found by reading the man page with

man xselection

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
xmkmf -a
make %{?jobs:-j%jobs} CCOPTIONS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/%{_xorg7bin}/xselection
%doc %{_xorg7_mandir}/man1/xselection.1x.gz

%changelog
