#
# spec file for package tuxpaint
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


%if 0%{?suse_version} >= 1550
%bcond_without sdl2
%else
%bcond_with sdl2
%endif

%define sdlver %{?with_sdl2:2}%{!?with_sdl2:%{nil}}
%define srcver %{?with_sdl2:2}%{!?with_sdl2:1}
Name:           tuxpaint
Version:        0.9.28
Release:        0
Summary:        Drawing Program for Young Children
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://www.tuxpaint.org/
Source0:        https://download.sourceforge.net/project/tuxpaint/tuxpaint/%{version}/%{name}-%{version}-sdl1.tar.gz
Source1:        https://download.sourceforge.net/project/tuxpaint/tuxpaint/%{version}/%{name}-%{version}-sdl2.tar.gz
Source2:        tuxpaint-rpmlintrc
Patch0:         tuxpaint-import-eval.patch
# PATCH-FIX-OPENSUSE tuxpaint-makefile.patch -- Disable update-desktop-database, because it do not work
Patch1:         tuxpaint-makefile.patch
%if 0%{?suse_version} >= 1550
# PATCH-FIX-UPSTREAM tuxpaint-pango-cflags.patch -- Include cflags from pango's pkgconfig file, needed only for sdl2 flavour
Patch2:         tuxpaint-pango-cflags.patch
%endif
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(sdl%{?sdlver})
BuildRequires:  pkgconfig(SDL%{?sdlver}_Pango)
BuildRequires:  pkgconfig(SDL%{?sdlver}_image)
BuildRequires:  pkgconfig(SDL%{?sdlver}_mixer)
BuildRequires:  pkgconfig(SDL%{?sdlver}_ttf)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  gperf
%if 0%{?suse_version} <= 01530
BuildRequires:  libimagequant-devel
%else
BuildRequires:  pkgconfig(imagequant)
%endif
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(zlib)
#
# openSUSE
#
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(SDL%{?sdlver}_gfx)
BuildRequires:  pkgconfig(librsvg-2.0)
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

Unlike drawing programs such as "The GIMP", it has a very
limited toolset. However, it provides a much simpler interface, and has
entertaining, child-oriented additions such as sound effects.

%package devel
Summary:        Devel files of tuxpaint
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(sdl%{?sdlver})
Requires:       pkgconfig(SDL%{?sdlver}_Pango)
Requires:       pkgconfig(SDL%{?sdlver}_image)
Requires:       pkgconfig(SDL%{?sdlver}_mixer)
Requires:       pkgconfig(SDL%{?sdlver}_ttf)
Requires:       pkgconfig(fribidi)
Requires:       libpaper-devel
Requires:       libpng-devel
Requires:       pkgconfig(zlib)
%if 0%{?suse_version}
Requires:       gcc-c++
Requires:       gettext-devel
Requires:       pkgconfig(librsvg-2.0)
%endif
%if 0%{?fedora_version}
Requires:       gettext
Requires:       librsvg2-devel
%endif

%description devel
Header files and development documentation for tuxpaint.

%prep
%if %{with sdl2}
%autosetup -p1 -T -b1 -n %{name}-%{version}-sdl%{?srcver}
%else
%autosetup -p1 -n %{name}-%{version}-sdl%{?srcver}
%endif
find . -name CVS -exec rm -rf {} +
find docs/ -type f -exec chmod -v 644 {} +

sed -Ei "s/\r$//" docs/outdated/*/*.txt

%build
%make_build \
     PREFIX=%{_prefix} \
     MAGIC_PREFIX=%{_libdir}/%{name}/plugins \
     CFLAGS="%{optflags}" \
     tp-magic-config
%make_build \
     PREFIX=%{_prefix} \
     CFLAGS="%{optflags}" \
     MAGIC_PREFIX=%{_libdir}/%{name}/plugins

%install
%if ! 0%{?suse_version}
mkdir -p %{buildroot}
%endif
%make_install \
     PREFIX="%{_prefix}" \
     X11_ICON_PREFIX="%{buildroot}/%{_datadir}/pixmaps" \
     MAGIC_PREFIX="%{buildroot}/%{_libdir}/%{name}/plugins" \
%if 0%{?suse_version}
     DEVDOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}-devel" \
     DOC_PREFIX="%{buildroot}/%{_defaultdocdir}/%{name}" \
%endif
     GNOME_PREFIX="%{_prefix}" \
     KDE_ICON_PREFIX="%{_datadir}/icons"

find %{buildroot}%{_mandir} -type f -exec chmod 644 {} +
find %{buildroot} -type d -exec chmod 0755 {} +
# Delete hidden thumbnail files
find %{buildroot}%{_datadir}/%{name} -name ".thumbs" -print -exec rm -fr {} +

%if 0%{?suse_version}
find %{buildroot} -name "*.desktop" -print -delete
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

%if 0%{?suse_version} >= 01500
# move bash-completion to new home
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions/
mv 	%{buildroot}%{_sysconfdir}/bash_completion.d/tuxpaint-completion.bash \
	%{buildroot}%{_datadir}/bash-completion/completions/
rmdir %{buildroot}%{_sysconfdir}/bash_completion.d
%endif

# find lang
%find_lang %{name}

%files -f %{name}.lang
%if 0%{?suse_version}
%doc %{_defaultdocdir}/%{name}
%endif
%{_mandir}/*
%exclude %{_mandir}/man1
%exclude %{_mandir}/man1/tp-magic-config*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%if 0%{?suse_version} >= 01500
%{_datadir}/bash-completion/completions/tuxpaint-completion.bash
%else
%config(noreplace) %{_sysconfdir}/bash_completion.d/tuxpaint-completion.bash
%endif
%{_bindir}/%{name}
%{_bindir}/tuxpaint-import
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*%{name}.*
%{_datadir}/applications/*.desktop

%files devel
%if 0%{?suse_version}
%doc %{_defaultdocdir}/%{name}-devel
%endif
%{_mandir}/man1/tp-magic-config*
%dir %{_includedir}/%{name}
%{_bindir}/tp-magic-config
%{_includedir}/%{name}/*

%changelog
