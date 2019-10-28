#
# spec file for package mypaint
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


Name:           mypaint
Version:        1.1.0
Release:        0
Summary:        Graphics application for digital painters
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
Url:            http://mypaint.org
Source:         https://github.com/mypaint/mypaint/releases/download/v1.1.0/mypaint-1.1.0.tar.bz2
# PATCH-FIX-UPSTREAM mypaint-scons-to-python3.patch badshah400@opensuse.org -- Convert SCons* to python3 for compatibility with openSUSE > 1320 where scons is python3 based
Patch0:         mypaint-scons-to-python3.patch
# PATCH-FIX-UPSTREAM
Patch1:         reproducible.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-cairo-devel
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
BuildRequires:  python-numpy >= 1.5
BuildRequires:  python-numpy-devel
%if 0%{?suse_version} > 1320
# Just because numpy detection relies on direct import in scons script (i.e. ran by python3)
# Shouldn't cause problem though as it's only needed for numpy/arrayobject.h which does not
# depend on the python version
BuildRequires:  python3-numpy
BuildRequires:  python3-numpy-devel
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  scons >= 1.2
BuildRequires:  swig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(lcms2)
Recommends:     %{name}-lang = %{version}
Requires:       python-numpy >= 1.7
%{py_requires}
%lang_package

%description
MyPaint is a graphics application for digital painters. It supports
graphics tablets made by Wacom, and many similar devices. The
standard brushes can emulate traditional media like charcoal,
pencils, ink, or paint.

%prep
%setup -q
%if 0%{?suse_version} > 1320
%patch0 -p1
%endif
%patch1 -p1

#FIXME Set correct library path for build arch
sed -i 's|lib/mypaint|%{_lib}/mypaint|g' SConscript SConstruct mypaint.py
sed -i 's|lib/pkgconfig|%{_lib}/pkgconfig|g' brushlib/SConscript
#FIXME fix incorrect icon sizes as per rpmlint report
cd desktop/icons/hicolor/
ICONSIZE="16 22 24 32 48"
for i in $ICONSIZE; do
    rsvg-convert -h $i -w $i scalable/actions/mypaint-tool-scratchpad.svg -o ${i}x${i}/actions/mypaint-tool-scratchpad.png
done

%build
scons python_config=python2.7-config python_binary=python2.7 prefix=%{_prefix} \
    %{?jobs:-j %jobs}

%install
scons python_config=python2.7-config python_binary=python2.7 prefix=%{_prefix} \
    --install-sandbox=install_tmp
cp -r {.,po,brushlib,brushlib/po}/install_tmp/* %{buildroot}
#FIXME incorrect file permissions, source has them as 0755
chmod 0755 %{buildroot}%{_datadir}/%{name}/brushes/label-brush-mypaint.sh
chmod 0755 %{buildroot}%{_datadir}/%{name}/brushlib/generate.py
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dm0644 desktop/icons/hicolor/48x48/apps/%{name}.png \
        %{buildroot}%{_datadir}/pixmaps/
%suse_update_desktop_file %{name}
%find_lang %{name}

# Updated libmypaint already provides its own lang files
find %{buildroot} -name "libmypaint.mo" -print -delete

# Fix env-based hashbang
sed -E -i "s:/usr/bin/env python*.*:/usr/bin/python2:" %{buildroot}%{_bindir}/mypaint

# Nuke the devel pkg: no one is using it and libmypaint-devel >= 1.3 obsoletes it
rm -r %{buildroot}%{_includedir}/lib%{name}
rm %{buildroot}%{_libdir}/pkgconfig/lib%{name}.pc
rm %{buildroot}/usr/lib/lib%{name}.a

%fdupes %{buildroot}/%{_prefix}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc changelog README
%license COPYING COPYING.cursors LICENSE
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/_mypaintlib.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/mypaint*
%{_datadir}/icons/hicolor/*/*/brush*
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
