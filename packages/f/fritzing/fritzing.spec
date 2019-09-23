#
# spec file for package fritzing
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fritzing
Version:        0.9.3b
Release:        0
Summary:        Electronic Design Automation platform featuring prototype to product
License:        GPL-3.0+
Group:          Productivity/Scientific/Electronics
Url:            http://fritzing.org/
Source0:        https://github.com/fritzing/fritzing-app/archive/%{version}.tar.gz
#PATCH-FIX-UPSTREAM fritzing-restore-qt5.1-compatibility.patch -- this patch restores compatibility with Qt5.1
Patch0:         fritzing-restore-qt5.1-compatibility.patch
#PATCH-FIX-UPSTREAM fritzing-libgit-0.24.patch -- make fritzing compatible with libgit2 > 0.23
Patch1:         fritzing-libgit-0.24.patch
#PATCH-FIX-UPSTREAM fritzing-cleanup-build-files.patch -- use system boost, libgit and clean up build files
Patch2:         fritzing-cleanup-build-files.patch
#PATCH-FIX-UPSTREAM fritzing-folderutils-fix.patch -- fix folderutils to properly return parts folder
Patch3:         fritzing-folderutils-fix.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost_1_58_0-devel
%endif
BuildRequires:  fdupes
BuildRequires:  libgit2-devel >= 0.23
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
%if 0%{?suse_version} < 1320
BuildRequires:  libQt5SerialPort-devel
BuildRequires:  libQt5Svg-devel
Requires:       libqt5-sql-sqlite
%else
BuildRequires:  libqt5-qtserialport-devel
BuildRequires:  libqt5-qtsvg-devel
Requires:       libQt5Sql5-sqlite
%endif
Requires:       fritzing-parts = %{version}
Requires(post):    shared-mime-info
Requires(postun):  shared-mime-info
Requires(post):    desktop-file-utils
Requires(postun):  desktop-file-utils

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fritzing is an initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to an actual product. It is in the spirit of Processing and Arduino which
allow users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

%prep
%setup -q -n %{name}-app-%{version}
%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's/\r$//' LICENSE.CC-BY-SA
chmod -x LICENSE* readme.md Fritzing.1

%build
# QMAKE_CFLAGS_ISYSTEM= added to work around gcc6 build problems
qmake-qt5 QMAKE_CFLAGS_ISYSTEM=
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
install -d %{buildroot}%{_datadir}/pixmaps/
mv %{buildroot}%{_datadir}/icons/fritzing.png %{buildroot}%{_datadir}/pixmaps/
sed -i '/X-SuSE-translate=false/d' fritzing.desktop
sed -i '/Version=/d' fritzing.desktop
sed -i '/Categories=/d' fritzing.desktop
sed -i 's/icons\/fritzing_icon.png/fritzing/g' fritzing.desktop
%suse_update_desktop_file -i -r %name Development IDE
find %{buildroot}%{_datadir}/%{name}/ -type f -exec chmod -x {} \;
rm -rf %{buildroot}%{_datadir}/%{name}/parts
%fdupes %{buildroot}%{_datadir}/%{name}/sketches

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme.md LICENSE.GPL2 LICENSE.GPL3 LICENSE.CC-BY-SA
%{_bindir}/Fritzing
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/fritzing.desktop
%{_mandir}/man1/Fritzing.*
%{_datadir}/mime/packages/*.xml

%post
%desktop_database_post
%mime_database_post

%postun
%desktop_database_postun
%mime_database_postun

%changelog
