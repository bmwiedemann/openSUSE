#
# spec file for package ibus-unikey
#
# Copyright (c) 2023 SUSE LLC
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
Group:          System/Localization
URL:            http://code.google.com/p/ibus-unikey/
Source:         http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM i@marguerite.su fix narrowing conversion from char to unsigned char
Patch0:         ibus-unikey-static_cast.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  ibus
BuildRequires:  ibus-devel
BuildRequires:  intltool
Requires:       ibus
Provides:       locale(ibus:vi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A Vietnamese engine for IBus input platform that uses Unikey.

%prep
%setup -q
%patch0 -p1

%build
%configure --libexecdir=%{_ibus_libexecdir}
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog
%{_datadir}/%{name}
%{_datadir}/ibus/component/*
%{_ibus_libexecdir}/ibus-*-unikey

%changelog
