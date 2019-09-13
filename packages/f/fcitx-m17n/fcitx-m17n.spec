#
# spec file for package fcitx-m17n
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fcitx-m17n
Version:        0.2.4
Release:        0
Summary:        M17N engine for fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese 
Url:            https://github.com/fcitx/fcitx-m17n
Source:         http://download.fcitx-im.org/fcitx-m17n/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fcitx >= 4.2.1
BuildRequires:  fcitx-devel >= 4.2.1
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  m17n-lib-devel
%if 0%{?suse_version}
BuildRequires:  pkg-config
%else
BuildRequires:  libotf
BuildRequires:  pkgconfig
%endif
BuildRequires:  xz
%{fcitx_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
M17N engine for fcitx. It allows input of many languages using the input table maps from m17n-db.

%prep
%setup -q

%build
mkdir build
cd build
cmake   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DLIB_INSTALL_DIR=%{_libdir} \
        ..
make

%install
pushd build
make DESTDIR=$RPM_BUILD_ROOT install
popd

%find_lang %{name}

strip %{buildroot}%{_fcitx_libdir}/%{name}.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_datadir}/m17n

%changelog
