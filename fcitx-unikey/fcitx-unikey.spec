#
# spec file for package fcitx-unikey
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


Name:           fcitx-unikey
Version:        0.2.7
Release:        0
Summary:        Vietnamese unikey support for Fcitx
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://gitlab.com/fcitx/fcitx-unikey
Source:         https://download.fcitx-im.org/fcitx-unikey/%{name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM lower qt5 version
Patch0:         qt5-version.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel >= 4.2.3
BuildRequires:  fcitx-qt5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  xz
%{fcitx_requires}
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150200
BuildRequires:  libqt4-devel
%endif

%description
fcitx-unikey provides support for Vietnamese unikey IM.

%prep
%setup -q
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%dir %{_fcitx_libdir}/qt
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/unikey.png
%{_fcitx_inputmethoddir}/unikey.conf
%{_fcitx_libdir}/%{name}.so
%{_fcitx_libdir}/qt/lib%{name}-macro-editor.so

%changelog
