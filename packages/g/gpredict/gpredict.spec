#
# spec file for package gpredict
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


Name:           gpredict
Version:        2.2.1
Release:        0
Summary:        Realtime satellite tracking and orbit prediction application
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            http://gpredict.oz9aec.net/
Source:         https://github.com/csete/gpredict/releases/download/v%{version}/gpredict-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcurl) >= 7.19
BuildRequires:  pkgconfig(libgps)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     %{name}-lang
Recommends:     hamlib

%description
Gpredict is a real-time satellite tracking and orbit prediction
application. It can track a large number of satellites and display
their position and other data in lists, tables, maps, and polar plots
(radar view). Gpredict can also predict the time of future passes for a
satellite, and provide you with detailed information about each pass.

%lang_package

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
%configure \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
%suse_update_desktop_file -c gpredict Gpredict "Satellite tracking program" gpredict gpredict-icon "Network;HamRadio"
%fdupes -s %{buildroot}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/gpredict
%{_datadir}/applications/gpredict.desktop
%{_datadir}/gpredict/
%{_datadir}/pixmaps/gpredict-icon.png
%{_datadir}/pixmaps/gpredict/
%{_mandir}/man1/gpredict.1%{ext_man}

%files lang -f %{name}.lang

%changelog
