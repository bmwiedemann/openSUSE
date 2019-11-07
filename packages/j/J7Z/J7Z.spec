#
# spec file for package J7Z
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


%if 0%{?suse_version} > 1320 || 0%{?is_opensuse}
%bcond_without  kf5
%endif
Name:           J7Z
Version:        1.4.2
Release:        0
Summary:        Java-based P7Zip GUI for data compression and backup
License:        LGPL-3.0-or-later
Url:            http://j7z.xavion.name
Source:         https://downloads.sourceforge.net/project/k7z/J7Z%%20%%28All%%29/%{version}/J7Z-%{version}-src.tar.bz2
BuildRequires:  ImageMagick
BuildRequires:  ant >= 1.8.0
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel >= 1.8
BuildRequires:  p7zip
BuildRequires:  update-desktop-files
Requires:       java >= 1.8
Requires:       p7zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if %{with kf5}
BuildRequires:  kf5-filesystem
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  strip-nondeterminism
%endif

%description
J7Z is an alternative 7-Zip GUI. (7-Zip is a file archiver.)
With J7Z, you can update existing archive, backup multiple
directories to a storage location, create or extract protected
archives. It allows using archiving profiles and lists.

%if %{with kf5}
%package kf5
Summary:        KF5 service menu for J7Z
Requires:       J7Z

%description kf5
J7Z is an alternative 7-Zip GUI.
This package contains the KF5 service menu.
%endif

%prep
%setup -q -n J7Z
sed -i -e 's|Qt;KDE;Utility;Archiving;Compression|Qt;KDE;Utility;Archiving|g' \
	Linux/Desktop/Menu/J7Z.desktop

%build
pushd Linux/Build
make %{?_smp_mflags}
popd
%if 0%{?suse_version} > 1320
strip-nondeterminism `find -name \*.jar`
%endif

%install
pushd Linux/Build
make Install.AllUsers DESTDIR=%{buildroot}
popd

rm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/J7Z.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,64x64,128x128}/apps
for size in 32x32 48x48 64x64 128x128 ; do
  convert -strip -size 256x256 Source/Image/apps/J7Z.png -resize $size %{buildroot}%{_datadir}/icons/hicolor/$size/apps/J7Z.png
done

%if %{with kf5}
echo "X-SuSE-translate=true" >> %{buildroot}%{_kf5_servicesdir}/ServiceMenus/J7Z-Create.desktop
echo "X-SuSE-translate=true" >> %{buildroot}%{_kf5_servicesdir}/ServiceMenus/J7Z-Extract.desktop
rm -rf %{buildroot}%{_datadir}/kde4
%else
rm -rf %{buildroot}%{_datadir}/kde4
rm -rf %{buildroot}%{_datadir}/kservices5
%endif
echo "X-SuSE-translate=true" >> %{buildroot}%{_datadir}/J7Z/Desktop/KDE/J7Z-Create.desktop
echo "X-SuSE-translate=true" >> %{buildroot}%{_datadir}/J7Z/Desktop/KDE/J7Z-Extract.desktop
echo "X-SuSE-translate=true" >> %{buildroot}%{_datadir}/J7Z/Desktop/Menu/J7Z.desktop

%fdupes %{buildroot}/%{_prefix}

%files
%defattr(-,root,root)
%{_bindir}/J7Z.sh
%{_datadir}/J7Z/
%{_datadir}/applications/J7Z.desktop
%{_datadir}/icons/hicolor/16x16/actions/*.png
%{_datadir}/icons/hicolor/*/apps/J7Z.png

%if %{with kf5}
%files kf5
%defattr(-,root,root)
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_servicesdir}/ServiceMenus/*.desktop
%endif

%changelog
