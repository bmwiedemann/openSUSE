#
# spec file for package qelectrotech
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Asterios Dramis <asterios.dramis@gmail.com>.
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


%define src 0.8.0
Name:           qelectrotech
Version:        0.80
Release:        0
Summary:        Application to Design Electric Diagrams
License:        GPL-2.0-or-later AND CC-BY-3.0
Group:          Productivity/Scientific/Electronics
URL:            https://qelectrotech.org/
Source0:        https://git.tuxfamily.org/qet/qet.git/snapshot/qet-%{src}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kcoreaddons-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%if 0%{?suse_version} < 1500
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
%endif

%description
QElectroTech is a Qt5 application to design electric diagrams. It uses XML
files for elements and diagrams, and includes both a diagram editor and an
element editor.

%prep
%setup -q -n qet-%{src}

# Fix compilation and installation paths
sed -e s,%{_prefix}/local/,%{_prefix}/, \
    -e /QET_LICENSE_PATH/s,'doc/,'share/doc/packages/, \
    -e /QET_MIME/s,../,, \
    -e /QET_MAN_PATH/s,'man/','share/man/', \
    -i qelectrotech.pro

# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/g" sources/machine_info.h
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/g" sources/machine_info.h

%build
%qmake5
%make_build

%install
%qmake5_install

# Fix desktop file
%suse_update_desktop_file -r qelectrotech "Education;Engineering"

%fdupes -s %{buildroot}

%find_lang %{name} --with-qt --with-man --all-name

%if 0%{?suse_version} < 1500
%post
%mime_database_post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun
%endif

%files -f %{name}.lang
%doc CREDIT ChangeLog README README.md
%license %{_defaultdocdir}/%{name}/ELEMENTS.LICENSE
%license %{_defaultdocdir}/%{name}/LICENSE
%{_bindir}/qelectrotech
%{_datadir}/appdata/qelectrotech.appdata.xml
%{_datadir}/applications/qelectrotech.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%dir %{_mandir}/fr.ISO8859-1
%dir %{_mandir}/fr.UTF-8
%{_mandir}/man1/qelectrotech.1%{?ext_man}
%dir %{_datadir}/mime/application
%{_datadir}/mime/application/x-qet-element.xml
%{_datadir}/mime/application/x-qet-project.xml
%{_datadir}/mime/application/x-qet-titleblock.xml
%{_datadir}/mime/packages/qelectrotech.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/x-qet-element.desktop
%{_datadir}/mimelnk/application/x-qet-project.desktop
%{_datadir}/mimelnk/application/x-qet-titleblock.desktop
%{_datadir}/qelectrotech/

%changelog
