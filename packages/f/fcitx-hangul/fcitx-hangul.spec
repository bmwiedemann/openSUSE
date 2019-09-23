#
# spec file for package fcitx-hangul
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


Name:           fcitx-hangul
Version:        0.3.1
Release:        0
Summary:        Hangul Module for Fcitx IM Framework
License:        GPL-2.0
Group:          System/I18n/Korean
Url:            https://github.com/fcitx/fcitx-hangul
Source:         http://download.fcitx-im.org/fcitx-hangul/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fcitx-devel >= 4.2.2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libhangul-devel >= 0.1.0
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       locale(fcitx:ko)
%{fcitx_requires}

%description
Fcitx-hangul is a Korean Wrapper for Fcitx IM Framework.
It's generally an IBus hangul implementation on Fcitx.

%prep
%setup -q

%build
mkdir -p build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} ..
make %{?_smp_mflags}

%install
pushd build
make DESTDIR=%{buildroot} install
popd

strip %{buildroot}%{_libdir}/fcitx/%{name}.so

# Fix incorrect-fsf-address
sed -i "s/59\ Temple\ Place,\ Suite\ 330,\ Boston,\ MA\ \ 02111-1307\ \ USA/51\ Franklin\ Street,\ Fifth\ Floor,\ Boston,\ MA\ \ 02110-1301\ \ USA/" COPYING

%find_lang %{name}
%if 0%{?suse_version}
%fdupes %{buildroot}
%else
fdupes -q -n -r %{buildroot}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_datadir}/hangul
%{_fcitx_imicondir}/hangul.png
%{_fcitx_inputmethoddir}/hangul.conf
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/status/*.png

%changelog
