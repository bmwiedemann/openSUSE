#
# spec file for package wasistlos
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


Name:           wasistlos
Version:        1.7.0~20241019.b483456
Release:        0
Summary:        WhatsApp for Linux
License:        GPL-3.0-only
URL:            https://github.com/xeco23/WasIstLos
Source0:        WasIstLos-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Provides:       whatsapp-for-linux = %{version}
Obsoletes:      whatsapp-for-linux < %{version}
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
An unofficial WhatsApp desktop application written in C++.
Previously named whatsapp-for-linux.

%lang_package

%prep
%setup -q -n WasIstLos-%{version}

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXX="g++-11"
%endif

%cmake
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/icons
rm  %{buildroot}%{_datadir}/locale/zh_Hans/LC_MESSAGES/wasistlos.mo

%find_lang %{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/com.github.xeco23.WasIstLos.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/status/*.png
%{_datadir}/metainfo/*.xml
%doc README.md
%license LICENSE

%files lang -f %{name}.lang

%changelog
