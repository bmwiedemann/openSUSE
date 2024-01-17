#
# spec file for package fcitx-sayura
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fcitx-sayura
Version:        0.1.2
Release:        0
Summary:        Fcitx input module for Sinhala
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-sayura
Source:         http://download.fcitx-im.org/fcitx-sayura/%{name}-%{version}.tar.xz
# remove next release
Source1:        COPYING
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{fcitx_requires}

%description
Fcitx is a Flexible Context-aware Input Tool with eXtension.

Fcitx-Sayura is a Sinhala input method for Fcitx input method framework ported from IBus-Sayura.

%prep
%setup -q
cp -r %{SOURCE1} ./

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install
cd ..

%find_lang %{name}

%if 0%{?suse_version}
%fdupes %{buildroot}
%else
fdupes -nqr %{buildroot}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.md COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_imicondir}/sayura.png
%{_fcitx_inputmethoddir}/sayura.conf
%{_fcitx_skindir}/default/sayura.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/sayura.svg

%changelog
