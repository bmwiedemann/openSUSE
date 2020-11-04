#
# spec file for package WindowMaker
#
# Copyright (c) 2020 SUSE LLC
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


Name:           WindowMaker
Summary:        A Colorful and Flexible Window Manager
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND SUSE-Public-Domain
Group:          System/GUI/Other
Version:        0.95.9
Release:        0
URL:            http://windowmaker.org/
Source:         http://windowmaker.org/pub/source/release/%{name}-%{version}.tar.gz
Source1:        %{name}-extra-0.1.tar.bz2
Source2:        theme.tar.bz2
Source4:        README.SUSE
Source5:        %{name}.desktop
Source6:        windowmaker
Source7:        %{name}-rpmlintrc
Patch1:         %{name}-config.patch
Patch2:         %{name}-menu.patch
Patch3:         fix_wmgenmenu_paths.patch
#
Patch101:       wm-giflib.patch
# PATCH-FEATURE-OPENSUSE
Patch102:       WindowMaker-reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wallpaper-branding-openSUSE
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
Requires:       wallpaper-branding-openSUSE
Requires:       xdg-menu
Provides:       windowmanager
Provides:       wmaker

%description
Window Maker is an X11 window manager originally designed to provide
integration support for the GNUstep Desktop Environment. In every way
possible, it reproduces the elegant look and feel of the NEXTSTEP user
interface. It is fast, feature rich, easy to configure, and easy to
use. It is also free software, with contributions being made by
programmers from around the world.

Window Maker has a stable user interface since many years and comes
with a powerful GUI configuration editor called WPrefs, which removes
the need to edit text-based config files by hand. It supports running
dockapps which make everyday tasks such as monitoring system 
performance and battery usage, mounting devices or connecting to the
internet very easy. Please see the features section for more specifics
on what Window Maker can do, and how it compares with other popular
window managers.

%package devel
Summary:        Development files for WindowMaker
License:        GPL-2.0-or-later
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
This package contains the header files and libraries necessary for
developing applications which use WindowMaker.

%prep
%setup -q -n %{name}-%{version} -a 1
mkdir menu_orig
cp %{name}/{menu.*,plmenu.*} menu_orig
%patch1
%patch2
%patch3
%patch101
%patch102
cp %{S:4} .
cp %{S:6} .
%if 0%{?suse_version} < 1140
rename no nb po/no.*
%endif
# ---------------------------------------------------------------------------

%build
bash -x ./autogen.sh
export LINGUAS="be bg bs ca cs da de el es et fi fr gl hr hu hy it ja ko ms nl no pl pt ro ru sk sv tr zh_CN zh_TW"
export CFLAGS="$RPM_OPT_FLAGS $(freetype-config --cflags)"
%configure \
  --prefix=/usr \
  --datadir=/usr/share \
  --disable-static \
  --with-pic\
  --sysconfdir=/etc/X11 \
  --enable-xinerama \
  --localedir=/usr/share/locale \
  --with-pixmapdir=/usr/share/%{name}/Pixmaps \
  --with-gnustepdir=/usr/lib/GNUstep

make %{?_smp_mflags}
(cd %{name}-extra-0.1
%configure \
  --prefix=/usr \
  --disable-static \
  --with-pic\
  --with-pixmapdir=/usr/share/%{name}/Pixmaps

make %{?_smp_mflags}
)
# ---------------------------------------------------------------------------

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -m 755 dockit $RPM_BUILD_ROOT/usr/bin/dockit
install -m 755 windowmaker $RPM_BUILD_ROOT/usr/bin/windowmaker
cd %{name}-extra-0.1
make DESTDIR=$RPM_BUILD_ROOT install
tar -xvjf %SOURCE2 -C $RPM_BUILD_ROOT/usr/share/%{name}/Themes/
find $RPM_BUILD_ROOT/usr/share/%{name}/Themes -type f -exec chmod 644 {} \;
find $RPM_BUILD_ROOT/usr/share/%{name}/Themes -type d -exec chmod 755 {} \;
# use default openSUSE wallpaper in SUSE theme
pushd %{buildroot}/usr/share/%{name}/Themes/SUSE.themed/
ln -sf /usr/share/wallpapers/openSUSEdefault/contents/images/1600x1200.jpg default.jpg
popd
#----------------------------------------------------------------------
# not packaged
rm -f $RPM_BUILD_ROOT/%{_mandir}/{cs,ru,sk}/man1/*
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
# install kdm/gdm entry
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/xsessions/
install -m 0644 %SOURCE5 $RPM_BUILD_ROOT/usr/share/xsessions/
%suse_update_desktop_file $RPM_BUILD_ROOT/usr/share/xsessions/%{name}.desktop
cd ..
%find_lang %{name}
%find_lang WINGs %{name}.lang
%find_lang WPrefs %{name}.lang
%find_lang wmgenmenu %{name}.lang

# rpmlint
%fdupes -s $RPM_BUILD_ROOT/usr/share/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS BUGFORM BUGS COPYING COPYING.WTFPL ChangeLog FAQ
%doc NEWS README* TODO
%doc menu_orig
%dir /etc/X11/%{name}
%config /etc/X11/%{name}/*
/usr/lib/GNUstep
/usr/bin/*
%{_libdir}/*.so.*
%{_mandir}/man1/*
/usr/share/WINGs
/usr/share/%{name}
/usr/share/xsessions/*
#/usr/X11R6/share/%{name}
#/usr/X11R6/GNUstep

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
