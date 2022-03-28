#
# spec file for package klavaro
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} >= 1500
%define espeak    espeak-ng-compat
%else
%define espeak    espeak
%endif
Name:           klavaro
Version:        3.13
Release:        0
Summary:        Typing tutor
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            https://klavaro.sourceforge.io/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libcurl-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkdatabox) >= 1.0
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{espeak}
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
Klavaro  is a touch typing tutor that is very
flexible and supports customizable keyboard
layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by
the program was designed to not depend on specific
layouts.

%lang_package

%prep
%setup -q

%build
# Disable static linking when libgtkdatabox gtk3 appears
%configure --disable-shared
%make_build

%install
%make_install

%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name}

%if 0%{?suse_version} >= 1500
%suse_update_desktop_file -r klavaro Education X-KDE-Edu-Teaching
%else
%suse_update_desktop_file -r klavaro Education Teaching
%endif

%files -f %{name}.lang
%{_bindir}/klavaro
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/klavaro.1%{?ext_man}
%{_datadir}/klavaro/
%dir %{_datadir}/appdata
%{_datadir}/appdata/klavaro.appdata.xml
%{_datadir}/applications/klavaro.desktop
%{_datadir}/icons/hicolor/*/apps/klavaro.png
# Remove static lib processing when libgtkdatabox gtk3 apppears
%exclude %{_libdir}/libgtkdataboks.*

%changelog
