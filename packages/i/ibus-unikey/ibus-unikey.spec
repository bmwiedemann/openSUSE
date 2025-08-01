#
# spec file for package ibus-unikey
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ibus-unikey
Version:        0.6.1
Release:        0
Summary:        Vietnamese engine for IBus input platform
License:        GPL-3.0-only
Group:          System/I18n/Vietnamese
URL:            https://github.com/vn-input/ibus-unikey/
Source:         https://github.com/vn-input/ibus-unikey/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE ibus-unikey-static_cast.patch boo#985186 i@marguerite.su -- fix narrowing conversion from char to unsigned char
Patch0:         ibus-unikey-static_cast.patch
#PATCH-FIX-UPSTREAM ibus-unikey-rm-mouse-capture.patch bco#1246569 qzhao@suse.com -- Remove mouse capture fuction to get rid of X11-devel dependence.
Patch1:         ibus-unikey-rm-mouse-capture.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libtool
Requires:       ibus
Provides:       locale(ibus:vi)

%description
A Vietnamese engine for IBus input platform that uses Unikey.

%lang_package

%prep
%autosetup -p1

%build
./autogen.sh                   \
        --with-debuginfod=no   \
        --disable-static       \
        --disable-silent-rules \
        --prefix=%{_prefix}   \
        --libexecdir=%{_ibus_libexecdir} \
        --with-gtk-version=3

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING
%doc README AUTHORS ChangeLog
%{_ibus_libexecdir}/ibus-engine-unikey
%{_ibus_libexecdir}/ibus-setup-unikey
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/icons/
%dir %{_datadir}/%{name}/ui/
%{_datadir}/%{name}/icons/ibus-unikey.png
%{_datadir}/%{name}/ui/setup-macro.ui
%{_datadir}/%{name}/ui/setup-main.ui
%{_datadir}/ibus/component/unikey.xml

%changelog
