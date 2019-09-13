#
# spec file for package meld
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


Name:           meld
Version:        3.20.1
Release:        0
Summary:        Visual diff and merge tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://meldmerge.org/
Source0:        https://download.gnome.org/sources/meld/3.20/%{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE meld-nodocs.patch dimstar@opensuse.org -- We do not want COPYING and NEWS installed like this
Patch0:         meld-nodocs.patch

BuildRequires:  fdupes
# Needed for typelib() Requires
BuildRequires:  gobject-introspection-devel
# Needed for highcolor macros
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  python3 >= 3.3
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
# needed for VCS diffs
Requires:       patch
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
# Suggest various vcs that meld can handle
Suggests:       bzr
Suggests:       cvs
# Not in Factory, but still in OBS
Suggests:       darcs
Suggests:       fossil
Suggests:       git
Suggests:       mercurial
Suggests:       monotone
Suggests:       subversion
Suggests:       tla
#
BuildArch:      noarch
%if 0%{?suse_version} < 1330
# Needed for shared-mime-info macros
BuildRequires:  shared-mime-info
%glib2_gsettings_schema_requires
%endif

%description
Meld is a visual diff and merge tool. Two or three files can be
compared and be edited in place. (The diffs update dynamically). Two
or three directories can be compared and file comparisons be launched.
The working copy directory from version control systems such as CVS,
Subversion, Bazaar-ng and Mercurial can be browsed and viewed.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
python3 setup.py build

%install
python3 setup.py \
    --no-update-icon-cache \
    --no-compile-schemas \
    install --root %{buildroot} --prefix %{_prefix}
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.meld IDE
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%glib2_gsettings_schema_post
%icon_theme_cache_post
%icon_theme_cache_post HighContrast
%mime_database_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%icon_theme_cache_postun
%icon_theme_cache_postun HighContrast
%mime_database_postun
%endif

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.gnome.meld.appdata.xml
%{_datadir}/applications/org.gnome.meld.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%doc %{_datadir}/help/C/meld/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/HighContrast/
%{_datadir}/mime/packages/org.gnome.meld.xml
%{_mandir}/man1/meld.1%{?ext_man}
%{python3_sitelib}/meld/
%{python3_sitelib}/meld*egg-info*

%files lang -f %{name}.lang

%changelog
