#
# spec file for package fcitx-chewing
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


Name:           fcitx-chewing
Version:        0.2.3
Release:        0
Summary:        Chewing Wrapper for Fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-chewing
Source:         http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
#PATCH-FIX-OPENSUSE marguerite@opensuse.org build for 12.3
Patch:          %{name}-openSUSE-12.3.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libchewing-devel
BuildRequires:  xz
Provides:       locale(fcitx:zh_TW)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fcitx-chewing is a Chewing(新酷音) Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese Phonetic IME.

%prep
%setup -q
%patch -p1

%build
mkdir -pv build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB_INSTALL_DIR=%{_lib} ..
make %{?_smp_mflags}

%install
pushd build
%make_install
popd

strip %{buildroot}%{_libdir}/fcitx/%{name}.so
%if 0%{?suse_version}
%fdupes %{buildroot}
%else
fdupes -n -q -r %{buildroot}
%endif
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/fcitx/
%{_datadir}/fcitx/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
