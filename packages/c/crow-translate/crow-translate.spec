#
# spec file for package crow-translate
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           crow-translate
Version:        2.3.2
Release:        0
Summary:        A Qt GUI for Google, Yandex and Bing translators
# QOnlineTranslator is licensed under GPL-3.0
# QHotkey is licensed under BSD-3-Clause
# QTaskbarControl is licensed under BSD-3-Clause
# SingleApplication is icensed under MIT
License:        GPL-3.0-only
Group:          Productivity/Networking/Web/Frontends
URL:            https://crow-translate.github.io/
#Git-Clone:     https://github.com/crow-translate/crow-translate.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtmultimedia-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  update-desktop-files
Recommends:     gstreamer-plugins-good

%description
A simple and lightweight translator that allows to translate and speak
text using Google, Yandex and Bing written with Qt5.

%prep
%setup -q

%build
%qmake5
%make_jobs

%install
%qmake5_install
mv %{buildroot}/%{_datadir}/applications/io.crow_translate.CrowTranslate.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -i %{name} Office Dictionary Network

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/crow
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
