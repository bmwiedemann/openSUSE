#
# spec file for package rawtherapee
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Marcin Bajor
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


Name:           rawtherapee
Version:        5.8
Release:        1%{?dist}
Summary:        Cross-platform raw image processing program
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            http://rawtherapee.com

%define _name rawtherapee

%if (0%{?suse_version} || 0%{?sles_version})
%define liblcms2_name liblcms2-2
%else
%define liblcms2_name lcms2
%endif

Requires:       %{liblcms2_name} >= 2.6

BuildRequires:  cmake

%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} == 1320
BuildRequires:  gcc49-c++
#!BuildIgnore: libgcc_s1
%endif

%if 0%{?sle_version} == 120100
# Leap 42.1 / SLE12SP2
BuildRequires:  gcc5-c++
%endif

%if 0%{?sle_version} == 120200
# Leap 42.2+ / SLE12SP2Backports
%if 0%{?is_opensuse}
BuildRequires:  gcc6-c++
#!BuildIgnore:  libasan3
%else
BuildRequires:  gcc5-c++
%endif
%endif

%if 0%{?sle_version} == 120300
# Leap 42.3+ / SLE12SP2Backports
%if 0%{?is_opensuse}
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc5-c++
%endif
%endif

%if 0%{?sle_version} == 120400
BuildRequires:  gcc5-c++
%endif

%if 0%{?suse_version} == 1315
#!Buildignore:  libgcc_s1
%endif

BuildRequires:  libiptcdata-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gtkmm-2.4)
%if 0%{?fedora_version} >= 24
BuildRequires:  libsigc++20-devel
%else
%if 0%{?mageia} 
BuildRequires:  libsigc++2.0-devel
%else
BuildRequires:  libsigc++2-devel
%endif
%endif
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
%if (0%{?suse_version} || 0%{?sles_version})
BuildRequires:  gtkmm3-devel
%else
%if 0%{?mageia} 
BuildRequires:  gtkmm3.0-devel
%else
BuildRequires:  gtkmm30-devel
%endif
%endif
BuildRequires:  fftw3-devel
%if (0%{?suse_version} > 1320 || 0%{?sle_version} > 120100) || 0%{?mageia}
BuildRequires:  libcanberra-gtk3-devel
%else
BuildRequires:  libcanberra-devel
%endif

%if 0%{?fedora_version}
BuildRequires:  libatomic
%endif

%if 0%{?mageia}
BuildRequires:  libatomic-devel
%endif

%if (0%{?suse_version} || 0%{?fedora_version})
BuildRequires:  fdupes
%endif

%if (0%{?suse_version} || 0%{?sles_version})
BuildRequires:  libexpat-devel
BuildRequires:  liblcms2-devel >= 2.6
BuildRequires:  update-desktop-files
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%else
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  lcms2-devel >= 2.6
%endif

BuildRequires:  lensfun-devel

%if 0%{?fedora_version}
BuildRequires:  librsvg2-devel
%else
BuildRequires:  librsvg-devel
%endif

Source0:        %{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      rawtherapee-stable-3.x
Conflicts:      rawtherapee-nosse
Conflicts:      rawtherapee-unstable
Conflicts:      rawtherapee-nosse-unstable
Conflicts:      rawtherapee-gtk3
Conflicts:      rawtherapee-gtk3-nosse
Conflicts:      rawtherapee-gtk2
Conflicts:      rawtherapee-gtk2-nosse
Conflicts:      rawtherapee-gtk2-unstable
Conflicts:      rawtherapee-gtk2-nosse-unstable

%description
RawTherapee is a cross platform image processing software equipped with the essential tools for high quality and efficient RAW photo development.
%ifarch i386 i486 i586 i686
Latest stable build from "releases" branch with SSE2 support.
%else
Latest stable build from "releases" branch.
%endif
%prep
%setup -q

%build
test -x "$(type -p gcc-4.9)" && export CC=gcc-4.9
test -x "$(type -p g++-4.9)" && export CXX=g++-4.9
test -x "$(type -p gcc-5)" && export CC=gcc-5
test -x "$(type -p g++-5)" && export CXX=g++-5
test -x "$(type -p gcc-6)" && export CC=gcc-6
test -x "$(type -p g++-6)" && export CXX=g++-6
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7

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

#fix LICENSE.txt EOL
sed -i 's/\r$//' LICENSE.txt
cmake \
                -DCMAKE_INSTALL_PREFIX=%{_prefix} \
                -DLIBDIR=%{_libdir} \
                -DCMAKE_BUILD_TYPE=release \
                -DDOCDIR=%{_datadir}/doc/packages/%{_name} \
                -DCREDITSDIR=%{_datadir}/doc/packages/%{_name} \
                -DLICENCEDIR=%{_datadir}/doc/packages/%{_name} \
                -DCACHE_NAME_SUFFIX="" \
                -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
                -DCMAKE_C_FLAGS="$CFLAGS" .

%__make %{?_smp_mflags}

%install
%make_install

%if (0%{?suse_version} || 0%{?sles_version})
%suse_update_desktop_file %{_name}
%else
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{_name}.desktop
%endif

%if (0%{?suse_version} || 0%{?fedora_version})
# create symlinks for man pages
%fdupes -s %buildroot/%_mandir
# create hardlinks for the rest
%fdupes %buildroot/%_prefix
%endif

%post

%if (0%{?suse_version} || 0%{?sles_version})
%desktop_database_post
%icon_theme_cache_post
%else
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%postun

%if (0%{?suse_version} || 0%{?sles_version})
%desktop_database_postun
%icon_theme_cache_postun
%else
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%posttrans

%if !(0%{?suse_version} || 0%{?sles_version})
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%clean

rm -rf %{buildroot}

%files

%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/%{_name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/com.rawtherapee.RawTherapee.appdata.xml
%{_datadir}/%{_name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/doc/packages/%{_name}
%{_datadir}/man/*/%{_name}*

%changelog
