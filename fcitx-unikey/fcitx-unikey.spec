#
# spec file for package fcitx-unikey
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


Name:           fcitx-unikey
Version:        0.2.7
Release:        0
Summary:        Vietnamese unikey support for Fcitx
License:        GPL-3.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-unikey
Source:         http://download.fcitx-im.org/fcitx-unikey/%{name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM lower qt5 version
Patch:          qt5-version.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel >= 4.2.3
BuildRequires:  fcitx-qt5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{fcitx_requires}
%if 0%{?suse_version} >= 1220
BuildRequires:  libqt4-devel
%endif

%description
fcitx-unikey provides support for Vietnamese unikey IM.

%prep
%setup -q
%patch -p1

%build
mkdir build && cd build
CXXFLAGS+="%{optflags}" cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	..
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_fcitx_libdir}/%{name}.so
%if 0%{?suse_version} >= 1220
%dir %{_fcitx_libdir}/qt
%{_fcitx_libdir}/qt/lib%{name}-macro-editor.so
%endif
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_imicondir}/unikey.png
%{_fcitx_inputmethoddir}/unikey.conf
%{_fcitx_descdir}/%{name}.desc
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
