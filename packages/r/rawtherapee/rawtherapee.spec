#
# spec file for package rawtherapee
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2022 Marcin Bajor
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


%define _name rawtherapee
%if (0%{?suse_version} || 0%{?sles_version})
%define liblcms2_name liblcms2-2
%else
%define liblcms2_name lcms2
%endif
Name:           rawtherapee
Version:        5.11
Release:        3%{?dist}
Summary:        Cross-platform raw image processing program
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://rawtherapee.com
Source0:        https://rawtherapee.com/shared/source/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gtk3-devel >= 3.24.3
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2) >= 0.24
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libiptcdata)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libraw) >= 0.21
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
Requires:       %{liblcms2_name} >= 2.6
Conflicts:      rawtherapee-gtk2
Conflicts:      rawtherapee-gtk2-nosse
Conflicts:      rawtherapee-gtk2-nosse-unstable
Conflicts:      rawtherapee-gtk2-unstable
Conflicts:      rawtherapee-gtk3
Conflicts:      rawtherapee-gtk3-nosse
Conflicts:      rawtherapee-nosse
Conflicts:      rawtherapee-nosse-unstable
Conflicts:      rawtherapee-stable-3.x
Conflicts:      rawtherapee-unstable
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} == 1315
#!BuildIgnore:  libgcc_s1
%endif
%if 0%{?fedora_version} >= 24
BuildRequires:  libsigc++20-devel
%else
%if 0%{?mageia}
BuildRequires:  libsigc++2.0-devel
%else
BuildRequires:  pkgconfig(sigc++-2.0)
%endif
%endif
%if (0%{?suse_version} || 0%{?sles_version})
BuildRequires:  pkgconfig(gtkmm-3.0)
%else
%if 0%{?mageia}
BuildRequires:  gtkmm3.0-devel
%else
BuildRequires:  gtkmm30-devel
%endif
%endif
%if (0%{?suse_version} > 1320 || 0%{?sle_version} > 120100) || 0%{?mageia}
BuildRequires:  pkgconfig(libcanberra-gtk3)
%else
BuildRequires:  libcanberra-devel
%endif
%ifarch x86_64
%if 0%{?fedora_version}
BuildRequires:  libatomic
%endif
%endif
%if 0%{?mageia}
BuildRequires:  libatomic-devel
%endif
%if (0%{?suse_version} || 0%{?fedora_version})
BuildRequires:  fdupes
%endif
%if (0%{?suse_version} || 0%{?sles_version})
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(lcms2)  >= 2.6
Requires(post): desktop-file-utils
Requires(postun):desktop-file-utils
%else
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  lcms2-devel >= 2.6
%endif
%if 0%{?fedora_version}
BuildRequires:  librsvg2-devel
%else
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.52
%endif

%description
RawTherapee is a cross platform image processing software equipped with the essential tools for high quality and efficient RAW photo development.
%ifarch i386 i486 i586 i686
Latest stable build from "releases" branch with SSE2 support.
%else
Latest stable build from "releases" branch.
%endif

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif

# Adding -fno-tree-loop-vectorize due to https://github.com/Beep6581/RawTherapee/issues/5749
export CFLAGS="%(echo %{optflags} | sed 's/-O2/-O3/' | sed 's/-D_FORTIFY_SOURCE=2/-D_FORTIFY_SOURCE=3/') -fno-tree-loop-vectorize"
export CXXFLAGS="$CFLAGS"

%ifarch i386 i486 i586 i686
export CFLAGS+=" -msse2"
export CXXFLAGS+=" -msse2"

%if 0%{?fedora_version} == 24
    export CFLAGS=$(echo $CFLAGS | sed -e "s/\-mtune=atom//g")
    export CXXFLAGS=$(echo $CXXFLAGS | sed -e "s/\-mtune=atom//g")
%endif

%endif

echo "CFLAGS: "$CFLAGS
echo "CXXFLAGS= "$CXXFLAGS

# FIXME: you should use the %%cmake macros
cmake \
                -DWITH_SYSTEM_LIBRAW=1 \
                -DCMAKE_INSTALL_PREFIX=%{_prefix} \
                -DLIBDIR=%{_libdir} \
                -DCMAKE_BUILD_TYPE=release \
                -DDOCDIR=%{_docdir}/%{_name} \
                -DCREDITSDIR=%{_docdir}/%{_name} \
                -DLICENCEDIR=%{_docdir}/%{_name} \
                -DCACHE_NAME_SUFFIX="" \
                -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
                -DCMAKE_C_FLAGS="$CFLAGS" .

%make_build

%install
%make_install

%if (0%{?suse_version} || 0%{?sles_version})
%suse_update_desktop_file %{_name}
%else
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{_name}.desktop
%endif

%if (0%{?suse_version} || 0%{?fedora_version})
# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}/%{_prefix}
%endif

%post

%if (0%{?suse_version} || 0%{?sles_version})
%desktop_database_post
%icon_theme_cache_post
%else
%{_bindir}/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun

%if (0%{?suse_version} || 0%{?sles_version})
%desktop_database_postun
%icon_theme_cache_postun
%else
%{_bindir}/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%posttrans

%if !(0%{?suse_version} || 0%{?sles_version})
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files

%{_bindir}/*
%{_datadir}/applications/%{_name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/com.rawtherapee.RawTherapee.appdata.xml
%{_datadir}/%{_name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_docdir}/%{_name}
%{_mandir}/*/%{_name}*

%changelog
