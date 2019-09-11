#
# spec file for package fcitx-skk
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


Name:           fcitx-skk
Version:        0.1.4
Release:        0
Summary:        Japanese SKK IME Wrapper for Fcitx
License:        GPL-3.0+
Group:          System/I18n/Japanese
Url:            https://github.com/fcitx/fcitx-skk
Source:         http://download.fcitx-im.org/fcitx-skk/%{name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM lower qt5 version
Patch:          qt5-version.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel >= 4.2.8
BuildRequires:  fcitx-qt5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libskk-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{fcitx_requires}

%description
fcitx-skk is an input method engine for Fcitx, which uses libskk as its backend.

%prep
%setup -q
%patch -p1

%build
mkdir -p build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd

%find_lang %{name}

%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README.md
%dir %{_fcitx_libdir}/qt
%{_fcitx_libdir}/%{name}.so
%{_fcitx_libdir}/qt/libfcitx-skk-config.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/skk.png
%{_fcitx_inputmethoddir}/skk.conf
%{_fcitx_datadir}/skk
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
