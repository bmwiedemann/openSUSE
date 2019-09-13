#
# spec file for package tvtime
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


Name:           tvtime
Version:        1.0.11
Release:        0
Summary:        High Quality Television Application
License:        GPL-2.0-or-later
Group:          Hardware/TV
Url:            http://tvtime.net/
Source:         http://www.linuxtv.org/downloads/tvtime/%{name}-%{version}.tar.gz
Patch0:         tvtime-1.0.11-sysmacros.diff
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(xxf86vm)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%lang_package

%description
tvtime is a high quality television application for use with video
capture cards.	tvtime processes the input from a capture card and
displays it on a computer monitor or projector.  Unlike other
television applications, tvtime focuses on high visual quality.

%prep
%setup -q
%patch0 -p1

%build
#autoreconf -i -f
%ifarch %ix86
RPM_OPT_FLAGS="%{optflags} -mmmx"
export CXXFLAGS="-mmmx"
%endif
export CFLAGS="%{optflags}"
%configure --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file -i tvtime AudioVideo TV
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-, root, root)
%doc NEWS AUTHORS COPYING ChangeLog README docs/html
%doc data/COPYING*
%{_bindir}/*
%dir %{_sysconfdir}/tvtime
%config(noreplace) %{_sysconfdir}/tvtime/*
%{_datadir}/tvtime
%{_datadir}/applications/tvtime.desktop
%{_datadir}/appdata/tvtime.appdata.xml
%dir %{_datadir}/appdata/
%{_datadir}/icons/hicolor/*/apps/tvtime.*
%{_mandir}/*/*

%files lang -f %{name}.lang
%defattr(-, root, root)

%changelog
