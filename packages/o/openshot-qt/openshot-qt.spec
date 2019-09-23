#
# spec file for package openshot-qt
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


Name:           openshot-qt
Version:        2.4.4
Release:        0
Summary:        Non-linear video editor with broad format support
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://openshot.org/
Source:         openshot-qt-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-httplib2
BuildRequires:  python3-openshot
BuildRequires:  python3-pyzmq
BuildRequires:  python3-setuptools
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(python3)
# Check list of dependencies:
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-xdg
Requires:       python3-httplib2
Requires:       python3-openshot
Requires:       python3-pyzmq
Requires:       python3-qt5
Requires:       python3-requests
Requires:       python3-xdg
Requires:       python(abi) = %{py3_ver}
Provides:       openshot = %{version}
Obsoletes:      openshot < %{version}
BuildArch:      noarch

%description
OpenShot Video Editor is a non-linear video editor. It can create and
edit videos and movies using many video, audio, and image formats.

%prep
%setup -q
sed -e 's|pixmaps|icons/hicolor/scalable/apps|' \
    -e '/lib.mime.packages/d' \
    -i setup.py

find . -type f -name '*.py' \
  -exec perl -n -i -e 'print $_ unless ($.==1 and /^#!/)' {} \;

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%suse_update_desktop_file -r %{name} AudioVideo AudioVideoEditing
# fix broken symlink
ln -sf "color shift.png" \
       %buildroot%{python3_sitelib}/openshot_qt/effects/icons/shift.png
%fdupes -s %{buildroot}%{python3_sitelib}

%files
%defattr(-,root,root,-)
%doc AUTHORS README.md
%license COPYING
%dir /usr/share/icons/hicolor/*/apps
%dir /usr/share/icons/hicolor/*
%{_bindir}/%{name}
%{python3_sitelib}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/openshot-qt.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/%{name}.??g

%changelog
