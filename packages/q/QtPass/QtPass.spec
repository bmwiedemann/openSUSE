#
# spec file for package QtPass
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


Name:           QtPass
Version:        1.3.1
Release:        0
Summary:        A multi-platform gui for pass
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://qtpass.org/
Source0:        https://github.com/IJHack/qtpass/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       password-store
Recommends:     git-core
Recommends:     gpg2
Recommends:     pwgen

%description
QtPass is a multi-platform GUI for pass, the standard unix password manager.

%prep
%autosetup

%build
export QT_HASH_SEED=0
%qmake5 PREFIX=%{_prefix}
%make_jobs

%install
%qmake5_install
%suse_update_desktop_file -i qtpass
install -Dpm644 artwork/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qtpass-icon.svg
install -Dpm644 qtpass.1 %{buildroot}%{_mandir}/man1/qtpass.1

# do not ship tests
rm -rf %{buildroot}%{_prefix}%{_prefix}/tests

%files
%license LICENSE
%doc README.md
%{_bindir}/qtpass
%{_datadir}/applications/qtpass.desktop
%{_datadir}/icons/hicolor/scalable/apps/qtpass-icon.svg
%{_mandir}/man1/qtpass.1%{?ext_man}

%changelog
