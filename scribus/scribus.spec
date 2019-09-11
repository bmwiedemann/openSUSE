#
# spec file for package scribus
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) Peter Linnell and 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           scribus
Version:        1.4.7
Release:        0
Summary:        Page Layout and Desktop Publishing (DTP)
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Other
Url:            http://www.scribus.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}-icon24.png
Source2:        %{name}-icon32.png
Source3:        %{name}-icon64.png
Source4:        %{name}-icon128.png
Source5:        %{name}-icon256.png
Source6:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE
Patch:          hunspell.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cairo-devel
BuildRequires:  cmake >= 2.6.0
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpodofo-devel
BuildRequires:  libqt4-devel >= 4.6.0
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files

%if 0%{?suse_version}
Requires:       ghostscript-library
Requires:       python-imaging
Requires:       tk
Suggests:       AdobeICCProfiles
Suggests:       Uniconvertor
%endif

%description
Scribus is a page layout program which produces output in PDF and
Postscript.

Scribus supports publishing features such as CMYK and spot colors,
PDF creation, Encapsulated Postscript import and export and creation
of color separations.

%package devel
Summary:        Development files for Scribus
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       freetype2-devel
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       zlib-devel

%description devel
This package provides the development headers for Scribus, used for
developing Scribus plugins.

%prep

%setup -q
%patch -p1

%build
# Delete non-free colour swatches (bnc#763586)
rm resources/swatches/givelife_colors_license.rtf
rm resources/swatches/GiveLife_Color_System*.xml
# All .eps swatches come with the same non-free license by dtp studio Oldenburg.
rm resources/swatches/*.eps
rm resources/swatches/dtp-studio-free-palettes-license.rtf

export CXXFLAGS="%{optflags} -fno-strict-aliasing"
export CFLAGS="$CXXFLAGS"

mkdir build
pushd build
cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  %if "%{_lib}" == "lib64"
  -DWANT_LIB64=1 \
  %endif
  -DWANT_CAIRO=1 \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
  -DCMAKE_SKIP_RPATH=TRUE \
  -DWANT_HUNSPELL=1 \
   ../

make %{_smp_mflags}

%install

pushd build
%make_install
popd

# install hi-res icons for better appearance on gnome-shell
install -D -m 0644 %{S:1} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -D -m 0644 %{S:2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 0644 %{S:3} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -D -m 0644 %{S:4} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -m 0644 %{S:5} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%if 0%{?suse_version}
%suse_update_desktop_file -r -i %{name} Qt Office Publishing WordProcessor

%endif

%fdupes %{buildroot}/%{_prefix}

# INSTALL APPSTREAM METAINFO (SOURCE6)
install -Dm0644 %{S:6} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

#update the mime database

%post
%mime_database_post
%desktop_database_post
%icon_theme_cache_post

%postun
%mime_database_postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%{_bindir}/scribus
%{_mandir}/man?/*.*
%{_mandir}/*/man?/*.*
%{_libdir}/scribus
%{_datadir}/mime/packages/scribus.xml
%{_datadir}/scribus
%{_datadir}/doc/scribus
%{_datadir}/applications/%{name}.desktop
# This should be owned by filesystem or man, but there are only scribus files:
%lang(pl) %dir %{_mandir}/pl
%lang(pl) %{_mandir}/pl/man1
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%files devel
%defattr(-,root,root)
%{_includedir}/scribus

%changelog
