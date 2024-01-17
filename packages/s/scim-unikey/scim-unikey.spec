#
# spec file for package scim-unikey
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scim-unikey
Version:        0.3.2
Release:        0
Summary:        Vietnamese Input Method Engine for SCIM using Unikey IME
License:        GPL-2.0
Group:          System/Localization
Url:            https://github.com/scim-im/scim-unikey
Source:         https://github.com/scim-im/scim-unikey/archive/v%{version}/scim-unikey-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  scim-devel >= 1.4.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SCIM (Smart Common Input Method) is an input method (IM) platform.
scim-unikey is a IME for scim. Use for type Vietnamese
Support via forum at: http://forum.ubuntu-vn.com/viewforum.php?f=85

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --libdir=%{_libdir}
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_scim_enginedir}/unikey.so
%{_scim_helperdir}/unikey-helper.so
%{_libexecdir}/scim-setup-unikey
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/setup
%{_datadir}/%{name}/setup/setup-macro.glade
%{_datadir}/%{name}/setup/setup-main.glade
%{_libdir}/libunikey-scim.so
%{_libdir}/libunikey-scim.so.1
%{_libdir}/libunikey-scim.so.1.0.0
%{_scim_icondir}/scim-unikey-check.png
%{_scim_icondir}/scim-unikey-configure.png
%{_scim_icondir}/scim-unikey.png

%changelog
