#
# spec file for package thunar-vcs-plugin
#
# Copyright (c) 2025 SUSE LLC
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


Name:           thunar-vcs-plugin
Version:        0.3.0
Release:        0
Summary:        Thunar Plugin Providing VCS Integration
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/thunar-plugins/thunar-vcs-plugin
Source0:        http://archive.xfce.org/src/thunar-plugins/thunar-vcs-plugin/0.3/%{name}-%{version}.tar.bz2
Source99:       %{name}.changes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel
BuildRequires:  pkgconfig(apr-1) >= 0.9.7
BuildRequires:  pkgconfig(exo-2) >= 0.11.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(thunarx-3) >= 1.2.0
Requires:       thunar >= 1.7.0
Recommends:     %{name}-lang = %{version}
Provides:       thunar-plugin-vcs = %{version}
Obsoletes:      thunar-plugin-vcs < %{version}

%description
The Thunar VCS Plugin provides integration with Subversion and GIT VCS and
makes VCS actions available through the context menu.

%lang_package

%prep
%autosetup

%build
export SOURCE_DATE_EPOCH=$(date +%s -r %{S:99})
%configure \
            --enable-git \
            --disable-static

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/thunarx-3/thunar-vcs-plugin.la

%find_lang %{name} %{?no_lang_C}

%files
%doc README.md ChangeLog NEWS AUTHORS
%license COPYING
%{_libexecdir}/tvp-git-helper
%{_libexecdir}/tvp-svn-helper
%{_libdir}/thunarx-3/%{name}.so
%{_datadir}/icons/hicolor/*/apps/git.png
%{_datadir}/icons/hicolor/*/apps/subversion.png

%files lang -f %{name}.lang

%changelog
