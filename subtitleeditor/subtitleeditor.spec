#
# spec file for package subtitleeditor
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


%define _sover  0
Name:           subtitleeditor
Version:        0.54.0
Release:        0
Summary:        A GTK+3 tool to edit subtitles
License:        GPL-3.0
Group:          Productivity/Multimedia/Video/Editors and Convertors
# http://home.gna.org/subtitleeditor is now dead
Url:            https://github.com/kitone/subtitleeditor
Source0:        https://github.com/kitone/subtitleeditor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.16.3
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamermm-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.10
BuildRequires:  pkgconfig(libxml++-2.6)

%description
Subtitle Editor is a GTK+3 tool to edit subtitles.
It can be used for new subtitles or as a tool to transform, edit, correct
and refine existing subtitle. This program also shows sound waves, which
makes it easier to synchronise subtitles to voices.

%package     -n lib%{name}-devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{_sover} = %{version}

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}%{_sover}.

%package     -n lib%{name}%{_sover}
Summary:        Support library for subtitleeditor
Group:          System/Libraries

%description -n lib%{name}%{_sover}
Support library for subtitleeditor, a GTK+3 tool to edit subtitles.

%lang_package

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -r %{name} GTK AudioVideo AudioVideoEditing
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}

%post -n lib%{name}%{_sover} -p /sbin/ldconfig
%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/menubar.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}/plugins-description/
%{_datadir}/%{name}/plugins-share/
%{_datadir}/%{name}/ui/
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugins
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*

%changelog
