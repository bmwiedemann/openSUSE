#
# spec file for package OpenBoard
#
# Copyright (c) 2022 SUSE LLC
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


Name:           OpenBoard
%define         dest_dir %{_libdir}/%{name}
%define         namelc openboard
%define         fqname ch.%{namelc}.%{name}
%define         githash  47a96e1d6bbdc0250977d22f1b79f11fcc1cbeee
%define         gitshort 47a96e1
%define         gitdate  20220608
%define         buildver 0608
Version:        1.7.0~git%{gitdate}.%{gitshort}
Release:        0
Summary:        Interactive whiteboard for schools and universities
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            http://openboard.ch
Source0:        https://github.com/OpenBoard-org/OpenBoard/archive/%{githash}.zip#/OpenBoard-%{githash}.zip
Patch0:         0001-Rewrite-libs.pri.patch
Patch1:         0002-Install-to-correct-directories-on-linux.patch
Patch2:         0003-podcast.pri-port-to-pkgconfig.patch
Patch3:         0004-Use-QStandardPaths-to-locate-resources.patch
Patch4:         0005-Add-svg-icon.patch
Patch5:         0006-pro-Remove-UB_THIRDPARTY_INTERACTIVE.patch
Patch6:         0007-Linux-Only-use-onboard-by-default-if-it-s-installed.patch
Patch7:         0008-install-fonts.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/551
Patch551:       0551-common-background-drawing.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/569
Patch569:       0569-scale-mirror-pixmap.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/604
Patch604:       0604-qt-5.12-compatibility.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/629
Patch629:       0629-bug-ruler.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/633
Patch633:       0633-improve-displaymanager.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/637
Patch637:       0637-fix-pdf-background-export.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/641
Patch641:       0641-fix-font-handling.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ffmpeg-devel
BuildRequires:  unzip
BuildRequires:  unzip
%if 0%{?sle_version} > 150200 || 0%{?suse_version} > 1520
BuildRequires:  pkgconfig(quazip1-qt5)
%else
BuildRequires:  pkgconfig(quazip)
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was
originally forked from Open-Sankoré, which was itself based on
Uniboard.

%prep
%setup -n %{name}-%{githash} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch551 -p1
%patch569 -p1
%patch604 -p1
%patch629 -p1
%patch633 -p1
%patch637 -p1
%patch641 -p1

# insert version
sed -i 's/VERSION_BUILD = 0225/VERSION_BUILD = %{buildver}/g' OpenBoard.pro
sed -i 's/OpenBoard 1.6.2/OpenBoard %{version}/g' resources/forms/preferences.ui

# remove x flag from any resource files
find resources -type f -print0 | xargs -0 chmod a-x

%build
lrelease-qt5 %{name}.pro

export QMAKE_CXX_FLAGS="$QMAKE_CXX_FLAGS -fpermissive"
%qmake5 %{name}.pro
%make_jobs

%install
export INSTALL_ROOT=%{buildroot}
%make_install

%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE
%{_datadir}/applications/%{fqname}.desktop
%{_datadir}/icons/hicolor/scalable
%{_datadir}/OpenBoard
%{_bindir}/%{namelc}

%changelog
