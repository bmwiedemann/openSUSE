#
# spec file for package vidcutter
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           vidcutter
Version:        6.0.0
Release:        0
Summary:        Video cutter and joiner
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://vidcutter.ozmartians.com/
Source0:        https://github.com/ozmartian/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FEATURE-OPENSUSE vidcutter-susepaths.patch aloisio@gmx.com -- use default SUSE paths
Patch0:         vidcutter-susepaths.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  mpv-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       ffmpeg
Requires:       libmpv1
Requires:       mediainfo
Requires:       python3-opengl
Requires:       python3-qt5
Requires:       python3-typing
%if 0%{?suse_version} <= 1320
BuildRequires:  desktop-file-utils
BuildRequires:  update-desktop-files
%endif

%description
Vidcutter is a Qt5-based application for video trimming/splitting
and merging/joining. The backend is driven by FFmpeg.

%prep
%setup -q
%patch0 -p1
# remove shebang
for f in $(find ./vidcutter -name "*.py"); do
   sed '0,/^#!/{//d;}' -i ${f}
done

%build
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}
%fdupes -s %{buildroot}%{_datadir}

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc CHANGELOG README.md
%license LICENSE
%if 0%{?suse_version} < 1500
%dir %{_datadir}/metainfo
%endif
%{_bindir}/%{name}
%{python3_sitearch}/%{name}-%{version}-py*.egg-info/
%{python3_sitearch}/%{name}/
%{_datadir}/applications/com.ozmartians.VidCutter.desktop
%{_datadir}/icons/hicolor/16x16/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/22x22/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/24x24/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/32x32/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/48x48/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/64x64/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/128x128/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/256x256/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/512x512/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/scalable/apps/com.ozmartians.VidCutter.svg
%{_datadir}/metainfo/com.ozmartians.VidCutter.appdata.xml
%{_datadir}/mime/packages/com.ozmartians.VidCutter.xml

%changelog
