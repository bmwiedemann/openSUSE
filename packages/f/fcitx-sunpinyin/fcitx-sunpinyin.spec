#
# spec file for package fcitx-sunpinyin
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


Name:           fcitx-sunpinyin
Version:        0.4.2
Release:        0
Summary:        Sunpinyin module for fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese 
Url:            https://github.com/fcitx/fcitx-sunpinyin
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pango-devel
%if 0%{?suse_version}
BuildRequires:  dbus-1-devel
%else
BuildRequires:  dbus-devel
%endif
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-skin-classic
BuildRequires:  fcitx-skin-dark
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  sunpinyin-devel
BuildRequires:  xz
Source:         http://download.fcitx-im.org/fcitx-sunpinyin/%{name}-%{version}.tar.xz
Provides:       locale(fcitx:zh_CN;zh_SG)
%{fcitx_requires}

%description
SunPinyin
===

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model. 

Currently, SunPinyin 2.0 is available on IBus.

fcitx-sunpinyin
===

fcitx-sunpinyin is a wrapper around SunPinyin which enables user to use
SunPinyin with fcitx. 

%prep
%setup -q -n %{name}-%{version}

%build
%{__mkdir} -pv build
pushd build
%if 0%{?suse_version} < 1140
CXXFLAGS="%{optflags} -I/usr/include/sunpinyin-2.0/" cmake \
%else
cmake  \
%endif
        -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} \
        ..
make

%install
pushd build
make DESTDIR=%{buildroot} install
popd
%find_lang %{name}

%{__strip} %{buildroot}%{_libdir}/fcitx/%{name}.so

%if 0%{?suse_version}
%fdupes %{buildroot}
%else
fdupes -qnr %{buildroot}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/sunpinyin.png
%{_fcitx_inputmethoddir}/sunpinyin.conf
%{_fcitx_skindir}/classic/sunpinyin.png
%{_fcitx_skindir}/dark/sunpinyin.png
%{_fcitx_skindir}/default/sunpinyin.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
