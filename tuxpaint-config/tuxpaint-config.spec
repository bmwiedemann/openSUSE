#
# spec file for package tuxpaint-config
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


Name:           tuxpaint-config
Version:        0.0.13
Release:        0
Summary:        Configuration tool for Tux Paint
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://www.tuxpaint.org/
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libpaper-devel
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       %{name}-lang = %{version}
Recommends:     tuxpaint
%endif
Source:         %{name}-%{version}.tar.bz2
Patch1:         tuxpaint-config-docpath.patch
Patch2:         tuxpaint-config-desktop.patch
Patch3:         tuxpaint-config-manpage.patch
Patch4:         tuxpaint-config-missing_includes.patch
# PATCH-FIX-UPSTREAM bmwiedemann https://sourceforge.net/p/tuxpaint/tuxpaint-config/merge-requests/2/ boo#1047218
Patch5:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tux Paint has a rich set of configuration options, controllable via
command-line options or configuration files. This configuration tool
provides a point-and-click interface for administrators to tailor
Tux Paint to suit the needs of their users.

%if 0%{?suse_version}
%{lang_package ca da el en_GB es fr it ja nl nn pt_BR pt_PT ru sk sl son sv uk zh_TW}
%endif

%prep
%setup -q
find . -name CVS | xargs rm -rf
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%build
make  CFLAGS="%optflags" PREFIX="%{_prefix}" X11_ICON_PREFIX=/usr/include/X11/pixmaps/

%install
mkdir -p %{buildroot}/%{_bindir}
make PREFIX="%{buildroot}/%{_prefix}" \
     X11_ICON_PREFIX="%{buildroot}/%{_includedir}/X11/pixmaps/" \
     DOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}" install
install -D -m644 src/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
# desktop file
%if 0%{?suse_version}
%suse_update_desktop_file -n %{name}
%endif
# fix file permissions
find %{buildroot}%_defaultdocdir/%{name} -type f -exec chmod 644 {} \;
find %{buildroot}%{_mandir} -type f -exec chmod 644 {} \;
# reduce space
%if 0%{?suse_version}
%fdupes -s %{buildroot}
%endif
%find_lang %{name}

%clean
rm -rf %{buildroot}

%if 0%{?fedora_version}
%files -f %{name}.lang
%defattr(-,root,root)
%else
%files
%defattr(-,root,root)
%endif
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/tuxpaint-config
%doc %_defaultdocdir/%{name}
%dir %{_includedir}/X11/pixmaps
%{_includedir}/X11/pixmaps/tuxpaint-config.xpm
%{_mandir}/man1/*
%{_datadir}/tuxpaint-config/
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%if 0%{?suse_version}
%files lang -f %{name}.lang
%defattr(-,root,root)
%if 0%{?suse_version} <= 1130
%defattr(-,root,root)
# unrecogniced locales
%dir %{_datadir}/locale/ach
%dir %{_datadir}/locale/ach/LC_MESSAGES
%dir %{_datadir}/locale/an
%dir %{_datadir}/locale/an/LC_MESSAGES
%dir %{_datadir}/locale/cgg
%dir %{_datadir}/locale/cgg/LC_MESSAGES
%dir %{_datadir}/locale/ff
%dir %{_datadir}/locale/ff/LC_MESSAGES
%dir %{_datadir}/locale/sat
%dir %{_datadir}/locale/sat/LC_MESSAGES
%dir %{_datadir}/locale/son
%dir %{_datadir}/locale/son/LC_MESSAGES
%dir %{_datadir}/locale/vec
%dir %{_datadir}/locale/vec/LC_MESSAGES
%endif
%endif

%changelog
