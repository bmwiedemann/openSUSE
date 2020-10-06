#
# spec file for package manpageeditor
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


%define oname ManPageEditor

Name:           manpageeditor
Version:        0.1.1
Release:        0
Summary:        A simple manual pages editor
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            http://gtk-apps.org/content/show.php?content=160219
Source0:        http://khapplications.darktech.org/zips/manpageeditor/%{oname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE vs. various errors & warnings about desktop files.
Patch1:         manpageeditor-desktop-warnings.diff

BuildRequires:  aspell-devel
BuildRequires:  ctags
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  groff
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtksourceview-2.0)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description
Create, edit, import, preview man-pages.

%prep
%setup -q -n %{oname}-%{version}
%patch1

%build
%configure \
           --enable-aspell

%install
%make_install

# Let's use %%doc macro.
rm %{buildroot}%{_datadir}/%{oname}/docs/gpl-3.0.txt

%fdupes -s %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%doc BUGS-ETC ChangeLog README ManPageEditor/resources/docs/gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_mandir}/man1/manpageeditor.1*
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{oname}.png

%changelog
