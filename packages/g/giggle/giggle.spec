#
# spec file for package giggle
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           giggle
Version:        0.7
Release:        0
Summary:        A graphical frontend for git
License:        GPL-2.0+
Group:          Development/Tools/Version Control
Url:            http://live.gnome.org/giggle
Source:         http://ftp.acc.umu.se/pub/GNOME/sources/giggle/0.7/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM giggle-gtksourceview38.patch bgo#697220 dimstar@opensuse.org -- Fix build against gtksourceview 3.8
Patch0:         giggle-gtksourceview38.patch
# PATCH-FIX-UPSTREAM giggle-vte-2.91.patch zaitor@opensuse.org -- Fix build with vte-2.91. Patch from archlinux.
Patch1:         giggle-vte-2.91.patch
BuildRequires:  gettext >= 0.18.1
BuildRequires:  git-core >= 1.5
BuildRequires:  intltool
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.30
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.0
BuildRequires:  pkgconfig(vte-2.91) >= 0.26
Recommends:     %{name}-lang
Requires:       git-core >= 1.5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Giggle is a Gtk frontend to the git content tracker.

With Giggle you will be able to visualize and browse easily the revision
tree, view changed files and differences between revisions, visualize
summarized info for the project, commit changes and other useful tasks
for any git managed projects contributor.

%package devel
Summary:        A graphical frontend for git
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}

%description devel
Giggle is a Gtk frontend to the git content tracker.

With Giggle you will be able to visualize and browse easily the revision
tree, view changed files and differences between revisions, visualize
summarized info for the project, commit changes and other useful tasks
for any git managed projects contributor.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p1
translation-update-upstream po giggle

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -G "Git repository viewer" %{name}

%if 0%{?suse_version} <= 1210
# Localized help
for help in %{buildroot}%{_datadir}/help/*/%{name}/; do
    LOCALE=`echo $help | sed "s:.*%{_datadir}/help/\([^/]*\)/%{name}/:\1:g"`
    echo "%%lang($LOCALE) %%dir %%{_datadir}/help/$LOCALE" >> %{name}.help-lang.tmp
    echo "%%lang($LOCALE) %%doc /${help##%{buildroot}}" >> %{name}.help-lang.tmp
done
echo "%%defattr(-,root,root)" >> %{name}.lang
sort -u %{name}.help-lang.tmp | grep -v "^%%lang(C)" >> %{name}.help-lang
%endif

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} > 1130
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%doc %dir %{_datadir}/help
%doc %dir %{_datadir}/help/C
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_libdir}/libgiggle.so.*
%{_libdir}/libgiggle-git.so.*
%dir %{_libdir}/giggle
%dir %{_libdir}/giggle/plugins
%dir %{_libdir}/giggle/plugins/%{version}
%{_libdir}/giggle/plugins/%{version}/*.so
%{_libdir}/giggle/plugins/%{version}/*.xml
%{_datadir}/giggle/

%files lang -f %{name}.lang

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/libgiggle.so
%{_libdir}/libgiggle-git.so

%changelog
