#
# spec file for package nfoview
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


Name:           nfoview
Version:        1.26
Release:        0
Summary:        Simple Viewer for NFO Files
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
Url:            http://otsaloma.io/nfoview/
Source:         https://github.com/otsaloma/nfoview/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     %{name}-lang
Recommends:     terminus-font
BuildArch:      noarch

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a text
editor are preset font and encoding settings, automatic window size and
clickable hyperlinks.

%lang_package

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}

%suse_update_desktop_file -r %{name} Office Viewer

%find_lang %{name}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS.md COPYING NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man?/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/*.egg-info

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
