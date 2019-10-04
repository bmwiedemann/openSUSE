#
# spec file for package tuxpaint
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


%define         gnomedir   %(gnome-config --prefix)
Name:           tuxpaint
Version:        0.9.23
Release:        0
Summary:        Drawing Program for Young Children
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://www.tuxpaint.org/
Source:         http://sourceforge.net/projects/tuxpaint/files/tuxpaint/%{version}/%{name}-%{version}.tar.gz
Source1:        tuxpaint-rpmlintrc
# PATCH-FIX-OPENSUSE 0001-Prepare-the-kdelibs4-removal.patch
Patch0:         kdelibs4-removal.patch
Patch1:         tuxpaint-import-eval.patch
BuildRequires:  SDL-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel > 2.0.8
BuildRequires:  fribidi-devel
BuildRequires:  gperf
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
#
# openSUSE
#
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  librsvg-devel
BuildRequires:  update-desktop-files
Requires:       freefont
Requires:       netpbm
Recommends:     tuxpaint-config
Recommends:     tuxpaint-stamps
%endif
#
# Fedora
#
%if 0%{?fedora_version}
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel >= 2.0
BuildRequires:  gettext
BuildRequires:  librsvg2-devel
BuildRequires:  netpbm-devel
# This should guarantee the proper permissions on
# all of the /usr/share/icons/hicolor/* directories.
Requires:       hicolor-icon-theme
%endif

%description
Tux Paint" is a drawing program for young children. It has a simple
interface and fixed canvas size, and provides access to previous images
using a thumbnail browser (it provides no access to the underlying
filesystem).

Unlike popular drawing programs such as "The GIMP," it has a very
limited toolset. However, it provides a much simpler interface, and has
entertaining, child-oriented additions such as sound effects.

%package devel
Summary:        Devel files of tuxpaint
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       SDL-devel
Requires:       SDL_Pango-devel
Requires:       SDL_image-devel
Requires:       SDL_mixer-devel
Requires:       SDL_ttf-devel
Requires:       fribidi-devel
Requires:       libpaper-devel
Requires:       libpng-devel
Requires:       zlib-devel
%if 0%{?suse_version}
Requires:       gcc-c++
Requires:       gettext-devel
Requires:       librsvg-devel
%endif
%if 0%{?fedora_version}
Requires:       gettext
Requires:       librsvg2-devel
%endif

%description devel
Header files and development documentation for tuxpaint.

%prep
%setup -q
%patch0 -p1
%patch1  -b .import-eval-patch
find . -name CVS   -print0 | xargs -0 rm -rf
find docs/ -type f -print0 | xargs -0 chmod -v 644

make PREFIX=%{_prefix} MAGIC_PREFIX=%{_libdir}/%{name}/plugins tp-magic-config

%build
make %{?_smp_mflags} \
     PREFIX=%{_prefix} \
     CFLAGS="%{optflags}" \
     MAGIC_PREFIX=%{_libdir}/%{name}/plugins -lpng14

%install
%if ! 0%{?suse_version}
mkdir -p %{buildroot}
%endif
make install install-kde-icons \
             PREFIX="%{_prefix}" \
             X11_ICON_PREFIX="%{buildroot}/%{_datadir}/pixmaps" \
             MAGIC_PREFIX="%{buildroot}/%{_libdir}/%{name}/plugins" \
             GNOME_PREFIX="%{_prefix}" \
             KDE_ICON_PREFIX="%{_datadir}/icons" \
%if 0%{?suse_version}
             DEVDOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}-devel" \
             DOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}" \
%endif
             DESTDIR=%{buildroot}

find %{buildroot}/%{_mandir} -type f -exec chmod 644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

%if 0%{?suse_version}
find %{buildroot} -name "*.desktop" -exec rm -v {} \;
%suse_update_desktop_file -i %{name} Game KidsGame
%fdupes -s %{buildroot}
%else
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --vendor %{vendor} \
    --add-category KidsGame \
    --delete-original \
    %{buildroot}/%{_datadir}/applications/tuxpaint.desktop
rm -rf %{buildroot}/%{_docdir}/%{name}
%endif
# remove unneeded scripts
rm %{buildroot}/%{_datadir}/%{name}/fonts/locale/zh_tw_docs/*.{sh,py,pe}
# find lang
%find_lang %{name}

%files -f %{name}.lang
%if 0%{?suse_version}
%doc %{_defaultdocdir}/%{name}
%endif
%{_mandir}/man1/tuxpaint*
%{_mandir}/pl/man1/tuxpaint.1%{?ext_man}
%dir %{_sysconfdir}/%{name}
%dir %{_mandir}/pl
%dir %{_mandir}/pl/man1
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/bash_completion.d/tuxpaint-completion.bash
%{_bindir}/%{name}
%{_bindir}/tuxpaint-import
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor
%if 0%{?suse_version} <= 1130
# locales not in official openSUSE distribution
%dir %{_datadir}/locale/en_ZA
%dir %{_datadir}/locale/en_ZA/LC_MESSAGES
%dir %{_datadir}/locale/gos
%dir %{_datadir}/locale/gos/LC_MESSAGES
%dir %{_datadir}/locale/nr
%dir %{_datadir}/locale/nr/LC_MESSAGES
%dir %{_datadir}/locale/oj
%dir %{_datadir}/locale/oj/LC_MESSAGES
%dir %{_datadir}/locale/tlh
%dir %{_datadir}/locale/tlh/LC_MESSAGES
%if ! %{defined fedora}
%dir %{_datadir}/locale/twi
%dir %{_datadir}/locale/twi/LC_MESSAGES
%endif
%dir %{_datadir}/locale/shs
%dir %{_datadir}/locale/shs/LC_MESSAGES
%dir %{_datadir}/locale/son
%dir %{_datadir}/locale/son/LC_MESSAGES
%dir %{_datadir}/locale/zam
%dir %{_datadir}/locale/zam/LC_MESSAGES
%endif

%files devel
%if 0%{?suse_version}
%doc %{_defaultdocdir}/%{name}-devel
%endif
%{_mandir}/man1/tp-magic-config*
%dir %{_includedir}/%{name}
%{_bindir}/tp-magic-config
%{_includedir}/%{name}/*

%changelog
