#
# spec file for package fcitx-cloudpinyin
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


Name:           fcitx-cloudpinyin
Version:        0.3.7
Release:        0
Summary:        Cloudpinyin module for fcitx
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese 
URL:            https://github.com/fcitx/fcitx-cloudpinyin
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libcurl-devel
%if 0%{?suse_version}
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  xz
Source:         http://download.fcitx-im.org/fcitx-cloudpinyin/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       locale(fcitx:zh_CN;zh_SG)
%{fcitx_requires}

%description
Cloulpinyin is an based cloud compute input method
 
%prep
%setup -q -n %{name}-%{version}

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

%{__strip} %{buildroot}%{_libdir}/fcitx/%{name}.so
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc

%changelog
