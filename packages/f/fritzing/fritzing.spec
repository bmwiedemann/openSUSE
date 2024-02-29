#
# spec file for package fritzing
#
# Copyright (c) 2024 SUSE LLC
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


Name:           fritzing
Version:        0.9.9+git20210922.f0af53a
Release:        0
Summary:        Electronic Design Automation platform featuring prototype to product
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://fritzing.org/
Source0:        %{name}-app-%{version}.tar.gz
#PATCH-FIX-OPENSUSE 0001-Use-system-libgit2.patch -- use system libgit, upstream wants to use bundled version
Patch1:         0001-Use-system-libgit2.patch
#PATCH-FIX-OPENSUSE 0002-Fix-appdata.xml-url-type.patch -- fix appdata url type
Patch2:         0002-Fix-appdata.xml-url-type.patch
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  libboost_headers-devel
BuildRequires:  libgit2-devel >= 0.23
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtserialport-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Requires:       fritzing-parts
Requires:       libQt5Sql5-sqlite
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info

%description
Fritzing is an initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to an actual product. It is in the spirit of Processing and Arduino which
allow users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

%prep
%autosetup -p1 -n %{name}-app-%{version}

sed -i 's/\r$//' LICENSE.CC-BY-SA
chmod -x LICENSE* README.md Fritzing.1

%build
# QMAKE_CFLAGS_ISYSTEM= added to work around gcc6 build problems
qmake-qt5 QMAKE_CFLAGS_ISYSTEM=
%make_build

%install
make INSTALL_ROOT=%{buildroot} install
sed -i '/Categories=/d' org.fritzing.Fritzing.desktop
%suse_update_desktop_file -i -r org.fritzing.Fritzing Development IDE
find %{buildroot}%{_datadir}/%{name}/ -type f -exec chmod -x {} \;
#rm -rf %%{buildroot}%%{_datadir}/%%{name}/parts
%fdupes %{buildroot}%{_datadir}/%{name}/sketches
appstream-util validate-relax --nonet org.fritzing.Fritzing.appdata.xml

%files
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.CC-BY-SA
%doc README.md
%{_bindir}/Fritzing
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/org.fritzing.Fritzing.desktop
%{_mandir}/man1/Fritzing.*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/org.fritzing.Fritzing.appdata.xml

%changelog
