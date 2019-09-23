#
# spec file for package xstroke
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xstroke
Version:        0.6
Release:        0
Summary:        Fullscreen gesture recognition for X
License:        GPL-2.0+
Group:          Hardware/Mobile
Url:            http://xstroke.org/
Source:         xstroke-%{version}.tar.bz2
Source1:        xstroke.png
Source2:        xstroke.desktop
# please upstream it
Patch0:         xstroke-no-copy-dt-needed-entries.patch
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1220
BuildRequires:  xorg-x11-devel
%else
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
%endif
#Requires:

%description
xstroke is a full-screen gesture recognition program for the X Window
System. It captures gestures performed with a pointer device, (such as
a mouse, a stylus, or a pen/tablet), recognizes the gestures and
performs actions based on the gestures.

%prep
%setup -q
%patch0 -p1
autoreconf -f --install

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} mandir=%{_mandir} libdir=%{_libdir} install
%suse_update_desktop_file -i xstroke
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -pr AUTHORS COPYING ChangeLog NEWS README TODO %{buildroot}%{_defaultdocdir}/%{name}/

%files
%defattr(-, root, root)
%{_bindir}/xstroke
%dir %{_sysconfdir}/xstroke
%config %{_sysconfdir}/xstroke/alphabet
%doc %{_defaultdocdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
