#
# spec file for package whatsapp-for-linux
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


Name:           whatsapp-for-linux
Version:        1.5.1
Release:        0
Summary:        WhatsApp for Linux
License:        GPL-3.0-only
URL:            https://github.com/eneshecan/whatsapp-for-linux
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.34

%description
An unofficial WhatsApp desktop application written in C++.

%lang_package

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/icons

%find_lang %{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.eneshecan.WhatsAppForLinux.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/metainfo/*.xml
%doc README.md
%license LICENSE

%files lang -f %{name}.lang
%{_datadir}/locale/??/LC_MESSAGES/%{name}.mo

%changelog
