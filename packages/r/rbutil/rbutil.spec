#
# spec file for package rbutil
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           rbutil
Version:        1.4.1
Release:        0
Summary:        Rockbox Firmware Manager
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://www.rockbox.org/wiki/RockboxUtility
Source:         http://download.rockbox.org/rbutil/source/RockboxUtility-v%{version}-src.tar.bz2
Patch1:         rbutil-fix-versionstring.patch
Patch2:         0001-imxtools-sbtools-fix-compilation-with-gcc-10.patch
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} < 1330
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif

%description
Firmware manager for Rockbox MP3 players.

%prep
%setup -q -n RockboxUtility-v%{version}
%patch1 -p1
%patch2 -p1

%build
cd rbutil/rbutilqt
%qmake5
make %{?_smp_mflags}

%install
install -Dm 0755 rbutil/rbutilqt/RockboxUtility %{buildroot}%{_bindir}/RockboxUtility
install -d %{buildroot}/%{_datadir}/pixmaps/
install -Dm 0644 rbutil/rbutilqt/icons/rockbox-256.png %{buildroot}/%{_datadir}/pixmaps/rbutil.jpg
%suse_update_desktop_file -c rbutil rbutil "Rockbox opensource firmware manager" RockboxUtility rbutil "Qt;AudioVideo;Utility;X-SuSE-SyncUtility;"

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%endif

%if 0%{?suse_version} < 1330
%postun
%desktop_database_postun
%endif

%files
%license docs/COPYING
%doc rbutil/rbutilqt/changelog.txt
%{_bindir}/RockboxUtility
%{_datadir}/applications/rbutil.desktop
%{_datadir}/pixmaps/rbutil.jpg

%changelog
