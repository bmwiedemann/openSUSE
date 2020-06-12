#
# spec file for package osdlyrics
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


%define  with_mpd     0
# %define  commit       18cc4a872c3a18e99a33ac233f7c8cb2f5dfc624
# %define  shortcommit  18cc4a8
%define _version 0.5.5-rc2

Name:           osdlyrics
Version:        0.4.99.2
Release:        0
Summary:        A third-party lyrics display program
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Visualization
URL:            https://github.com/osdlyrics/osdlyrics
Source0:        https://github.com/osdlyrics/osdlyrics/archive/%{_version}/%{name}-%{_version}.tar.gz
# Source0:        https://github.com/osdlyrics/osdlyrics/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{name}.appdata.xml
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  gnome-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sqlite3)
Requires:       gtk2
Requires:       python3-chardet
Requires:       python3-future
Requires:       python3-pycurl
Requires:       sqlite3
Recommends:     %{name}-lang
Recommends:     python3-%{name}
%if %{with_mpd}
BuildRequires:  mpd
%endif

%description
OSD Lyrics is a lyrics show compatible with various media players. It is not a
plugin but a standalone program. OSD Lyrics shows lyrics on your desktop, in the
style similar to KaraOK. It also provides another displaying style, in which
lyrics scroll from bottom to top. OSD Lyrics can download lyrics from the
network automatically.

%package -n python3-%{name}
Summary:        Python module for osdlyrics
Group:          Productivity/Multimedia/Sound/Visualization
Requires:       %{name} = %{version}
Obsoletes:      python-%{name} <= %{version}

%description -n python3-osdlyrics
This package contains python3 module for osdlyrics

%lang_package

%prep
%setup -q -n %{name}-%{_version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure  --enable-appindicator \
            PYTHON=/usr/bin/python3 \
%if %{with_mpd}
            --enable-mpd
%else
            --disable-mpd
%endif

%make_build

%install
%make_install
install -d %{buildroot}%{_datadir}/metainfo
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo

%suse_update_desktop_file %{name}

%find_lang %{name}
%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-create-lyricsource
%{_bindir}/%{name}-daemon
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/org.%{name}.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml

%files -n python3-%{name}
%{python3_sitelib}/%{name}

%files lang -f %{name}.lang

%changelog
