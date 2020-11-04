#
# spec file for package lxqt-themes
#
# Copyright (c) 2020 SUSE LLC
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


Name:           lxqt-themes
Version:        0.16.0
Release:        0
Summary:        Themes, graphics and icons for LXQt
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-themes
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        lxqt-themes.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildArch:      noarch

%description
Themes, graphics and icons for LXQt.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/lxqt/themes

%files
%license COPYING
%doc CHANGELOG README.md
%dir %{_datadir}/lxqt
%{_datadir}/lxqt/graphics
%{_datadir}/lxqt/themes
%{_datadir}/icons/hicolor/*/places/*.??g
%{_datadir}/icons/hicolor/*/apps/*.??g

%changelog
