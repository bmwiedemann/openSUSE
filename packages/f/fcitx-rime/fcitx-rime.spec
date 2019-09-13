#
# spec file for package fcitx-rime
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


Name:           fcitx-rime
Version:        0.3.2
Release:        0
Summary:        Rime input engine support for Fcitx
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-rime
Source:         http://download.fcitx-im.org/fcitx-rime/%{name}-%{version}.tar.xz
BuildRequires:  brise
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-skin-classic
BuildRequires:  fcitx-skin-dark
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  librime-devel
%if 0%{?fedora_version}
# resolve "have choice"
BuildRequires:  libyaml-cpp0_3
%endif
BuildRequires:  xz
# explicitly requires brise (rime-data)
Requires:       brise
%{fcitx_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

This package is the Fcitx implentation of RIME.

%prep
%setup -q

%build
mkdir -p build
pushd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
pushd build
%make_install
popd

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
%{_fcitx_inputmethoddir}/rime.conf
%{_fcitx_imicondir}/rime.png
%{_fcitx_skindir}/default/rime-*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/*/status/*.*

%changelog
