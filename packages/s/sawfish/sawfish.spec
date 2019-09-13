#
# spec file for package sawfish
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 Jan Nieuwenhuizen <jnieuwenhuizen@novell.com>
# Copyright (c) 2000 John Harper <john@dcs.warwick.ac.uk>
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


Name:           sawfish
Version:        1.12.90
Release:        0
Summary:        A highly configurable window manager for X11
License:        GPL-2.0+
Group:          System/GUI/Other
%if 0%{?suse_version} > 1230
%else
%endif

Url:            http://sawfish.wikia.com/
Source:         http://download.tuxfamily.org/sawfish/%{name}_%{version}.tar.xz
# Autoload feature for Emacs in editing sawfish files
Source1:        suse-start-sawfish.el
# PATCH-FIX-OPENSUSE toganm@opensuse.org avoid unnecessary rebuilds
Patch1:         sawfish-1.9.1-remove-buildtime.patch
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(ice) >= 1.0
BuildRequires:  pkgconfig(librep) >= 0.92.1
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(rep-gtk) >= 0.90.7
BuildRequires:  pkgconfig(sm) >= 1.0
BuildRequires:  pkgconfig(x11) >= 1.0
BuildRequires:  pkgconfig(xft) >= 1.0
BuildRequires:  pkgconfig(xinerama) >= 1.0
BuildRequires:  pkgconfig(xrandr) >= 1.0
BuildRequires:  pkgconfig(xtst) >= 1.0
%if 0%{?suse_version} <= 1210
BuildRequires:  xz
%endif
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif

Requires(pre):  %install_info_prereq
Requires:       librep
Requires:       rep-gtk
Recommends:     %name-sounds
Recommends:     %{name}-lang
Recommends:     %{name}-pager
Recommends:     pulseaudio-utils
Obsoletes:      %{name}-lisp < %{version}
Provides:       %{name}-lisp = %{version}
# windowmanager is a generic provides for every WM - there are things (like Xvnc)
# That rely on the prsence of 'a WM', but do not care which one it is
Provides:       windowmanager
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sawfish is an extensible window manager using an Emacs Lisp-like
scripting language -- all window decorations are configurable, the basic
idea is to have as much user-interface policy as possible controlled
through the Lisp language. This is no layer on top of twm, but a wholly
new architecture.

Despite this extensibility its policy is currently very minimal
compared to most window managers. Its aim is simply to manage windows
in the most flexible and attractive manner possible. As such it does
not implement desktop backgrounds, applications docks, or other things
that may be achieved through separate applications.

%package sounds
Summary:        A highly configurable window manager for X11 - Sound files
License:        Artistic-2.0
Group:          System/GUI/Other
%if 0%{?suse_version} > 1230
%else
%endif
BuildArch:      noarch

%description sounds
Sawfish is an extensible window manager using an Emacs Lisp-like
scripting language -- all window decorations are configurable, the basic
idea is to have as much user-interface policy as possible controlled
through the Lisp language. This is no layer on top of twm, but a wholly
new architecture.

Despite this extensibility its policy is currently very minimal
compared to most window managers. Its aim is simply to manage windows
in the most flexible and attractive manner possible. As such it does
not implement desktop backgrounds, applications docks, or other things
that may be achieved through separate applications.


%package devel
Summary:        A highly configurable window manager for X11 - Development Files
License:        GPL-2.0+
Group:          Development/Languages/Scheme
%if 0%{?suse_version} > 1230
%else
%endif
Requires:       %{name} = %{version}
Requires:       librep-devel
Requires:       rep-gtk-devel

%description devel
Sawfish is an extensible window manager using an Emacs Lisp-like
scripting language -- all window decorations are configurable, the basic
idea is to have as much user-interface policy as possible controlled
through the Lisp language. This is no layer on top of twm, but a wholly
new architecture.

Despite this extensibility its policy is currently very minimal
compared to most window managers. Its aim is simply to manage windows
in the most flexible and attractive manner possible. As such it does
not implement desktop backgrounds, applications docks, or other things
that may be achieved through separate applications.


%prep
%setup -q -n %{name}_%{version}
%patch1 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing "
export CXXFLAGS="$CFLAGS"
export CPPFLAGS="$CFLAGS"
./autogen.sh
%configure

make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}
# Change sr@Latn to sr@latin
mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
# Change no to nb_NO
mv %{buildroot}%{_datadir}/locale/no %{buildroot}%{_datadir}/locale/nb_NO
%find_lang %{name} %{?no_lang_C}
# Name[el] is not valid UTF-8
sed -i "s/Name\[el\].*//" %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i "s/Name\[el\].*//" %{buildroot}%{_datadir}/xsessions/%{name}.desktop
%suse_update_desktop_file %{name}
%suse_update_desktop_file %{buildroot}%{_datadir}/gnome/wm-properties/%{name}-wm.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/apps/ksmserver/windowmanagers/sawfish.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/ksmserver/windowmanagers/sawfish.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/%{name}.desktop

install -d %buildroot/%_datadir/emacs/site-lisp
install -m 644 %name.el %buildroot/%_datadir/emacs/site-lisp/%name.el
install -m 644 %{S:1} %buildroot/%_datadir/emacs/site-lisp/

find %{buildroot}%{_libdir} -name "*.la" -delete
find %{buildroot}%{_libdir} -name "*.a" -delete
%fdupes  %{buildroot}%{_datadir}/%{name}
%fdupes %{buildroot}%{_libexecdir}/%{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%desktop_database_post
%icon_theme_cache_post

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING CONTRIBUTING MAINTAINERS NEWS README README.IMPORTANT 
%doc doc/
%doc lisp/sawfish/cfg/WIDGETS-LIST
%{_bindir}/sawfish
%{_bindir}/sawfish-about
%{_bindir}/sawfish-client
%{_bindir}/sawfish-config
%{_bindir}/%{name}-*-session

%{_datadir}/%{name}
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/wm-properties
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/apps
%dir %{_datadir}/kde4/apps/ksmserver
%dir %{_datadir}/kde4/apps/ksmserver/windowmanagers
%dir %{_datadir}/ksmserver
%dir %{_datadir}/ksmserver/windowmanagers
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-config.desktop
%{_datadir}/gnome/wm-properties/%{name}-wm.desktop
%{_datadir}/kde4/apps/ksmserver/windowmanagers/sawfish.desktop
%{_datadir}/ksmserver/windowmanagers/sawfish.desktop
%{_datadir}/icons/hicolor/32x32/apps/sawfish-config.png
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/xsessions/%{name}-*.desktop
%{_libdir}/%{name}/
%{_libdir}/rep/%{name}/
%doc %{_infodir}/%{name}.*
%doc %{_mandir}/man?/sawfish.*
%doc %{_mandir}/man?/sawfish-client.*
%doc %{_mandir}/man?/sawfish-config.*
%exclude %_datadir/%name/sounds/*
%dir %_datadir/emacs/site-lisp
%_datadir/emacs/site-lisp/%name.el
%_datadir/emacs/site-lisp/suse-start-sawfish.el

%files devel
%defattr(-,root,root)
%{_includedir}/sawfish/
%{_libdir}/pkgconfig/*.pc

%files sounds
%defattr(-,root,root)
%doc COPYING.SOUNDS
%_datadir/%name/sounds/*.wav

%changelog
