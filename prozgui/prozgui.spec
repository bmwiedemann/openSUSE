#
# spec file for package prozgui
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


Name:           prozgui
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
Summary:        GUI Advanced Linux Download Manager
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
Version:        2.0.5beta
Release:        0
Url:            http://prozilla.genesys.ro
Source0:        http://prozilla.genesys.ro/downloads/prozgui/tarballs/prozgui-2.0.5beta.tar.bz2
Source1:        COPYING
Patch0:         prozgui-2.0.5beta-autoconf.diff
Patch1:         prozgui-2.0.5beta-gettext.diff
Patch2:         prozgui-2.0.5beta-strcpy.diff
Patch3:         prozgui-2.0.5beta-include.diff
Patch4:         prozgui-2.0.5beta-oldmacros.diff
Patch5:         prozgui-retval.diff
Patch6:         prozgui-gcc4.diff
Patch7:         prozgui-2.0.5beta-qualification.diff
Patch8:         prozgui-2.0.5beta-locale.diff
Patch9:         prozgui-2.0.5beta_remove-redefinitions.patch
Patch10:        prozgui-fltk13.diff
Patch11:        prozgui-2.0.5beta-automake-1.13.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the GUI version of ProZilla. It uses libprozilla and the GUI is
created and designed with the Fast Light Tool Kit (fltk).

ProZilla is a download accelerator program written for Linux to speed
up the normal file download process. It often gives speed increases of
around 200% to 300%. It supports both the FTP and HTTP protocols, and
the theory behind it is very simple. The program opens multiple
connections to a server, and each of the connections downloads a part
of the file, thus defeating existing Internet congestion prevention
methods which slow down a single connection based download.

%prep
%setup
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10 -p1
%patch11 -p1
rm INSTALL

%build
export CFLAGS="$RPM_OPT_FLAGS" 
export CXXFLAGS="$RPM_OPT_FLAGS"
gettextize -f --no-changelog
gettextize -f --no-changelog libprozilla
autoreconf -fi
test -f po/Makevars || cp po/Makevars.template po/Makevars
test -f libprozilla/po/Makevars || cp libprozilla/po/Makevars.template libprozilla/po/Makevars
# changed the prefix to /usr due to new X.org doesnt use X11R6 dir anymore 
# fltk should be checked in at the same time
# FLTK_PREFIX=/usr/X11R6
FLTK_PREFIX=/usr
CFLAGS="$RPM_OPT_FLAGS" \
CXXFLAGS="$RPM_OPT_FLAGS" \
%configure \
	--with-fltk-libs="$FLTK_PREFIX/%{_lib}" \
	--with-fltk-includes="$FLTK_PREFIX/include" \
	--enable-shared \
	--disable-static \
	--with-pic
# C[XX]FLAGS must be used this way. For some unknown reasons it is not enough
# to just export them
make \
CFLAGS="-Wall -ggdb -D_REENTRANT $RPM_OPT_FLAGS" \
CXXFLAGS="-I$FLTK_PREFIX/include $RPM_OPT_FLAGS"

%install
make DESTDIR=%{buildroot} install
install -D -m 644 src/images/Pz12.xpm %{buildroot}%{_datadir}/pixmaps/prozgui.xpm
install -d -m 755 %{buildroot}%{_includedir}/prozilla
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/prozilla/
%find_lang %{name}
%find_lang libprozilla %{name}.lang  

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr (-,root,root)
%doc COPYING ChangeLog CREDITS* README TODO docs/FAQ libprozilla/docs/HACKING
%{_bindir}/prozgui
%{_includedir}/prozilla
%{_libdir}/libprozilla*
%{_datadir}/pixmaps/*
%{_mandir}/man1/prozgui*

%changelog
