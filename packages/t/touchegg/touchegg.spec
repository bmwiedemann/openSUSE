#
# spec file for package touchegg
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


Name:           touchegg
Version:        1.1.1
Release:        0
Summary:        A multitouch gesture recogniser for GNU/Linux
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Hardware/Other
Url:            https://github.com/JoseExposito/touchegg
Source:         https://github.com/JoseExposito/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE touchegg-1.1.1-slowdown-scroll-speed.patch
Patch0:         touchegg-1.1.1-slowdown-scroll-speed.patch
# PATCH-FEATURE-OPENSUSE touchegg-qt5.patch sor.alexei@meowr.ru -- Build with Qt5.
Patch1:         touchegg-qt5.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libgeis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Suggests:       %{name}-gui >= %{version}

%description
Touchegg is a multitouch gesture recogniser for GNU/Linux that
allows associating actions to each gesture. Written in C++ with Qt4
and geis library.

%package gui
Summary:        Multitouch gesture recogniser GUI
Group:          System/GUI/Other
Requires:       %{name} >= %{version}

%description gui
Graphical user interface for a multitouch gesture recogniser for
GNU/Linux.

%prep
%setup -q
%patch0
%patch1 -p1

%build
for dir in %{name} %{name}-gui; do
    pushd "$dir"
    %qmake5
    make %{?_smp_mflags} V=1
    popd
done

%install
for dir in %{name} %{name}-gui; do
    pushd "$dir"
    %qmake5_install
    popd
done

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mv -f %{buildroot}%{_datadir}/icons/%{name}-gui.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-gui.png

%suse_update_desktop_file -r %{name}-gui Utility DesktopUtility

%if 0%{?suse_version} < 1500
%post gui
%desktop_database_post
%icon_theme_cache_post

%postun gui
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license %{name}/COPYING
%else
%doc %{name}/COPYING
%endif
%doc %{name}/{CHANGELOG,README}
%{_bindir}/%{name}
%{_datadir}/%{name}/

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-gui.*

%changelog
