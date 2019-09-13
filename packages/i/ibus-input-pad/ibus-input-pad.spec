#
# spec file for package ibus-input-pad
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


Name:           ibus-input-pad
Version:        1.4.99.20140916
Release:        0
Summary:        Input Pad for IBus
License:        GPL-2.0+
Group:          System/Localization
Url:            https://github.com/fujiwarat/ibus-input-pad
Source0:        https://github.com/fujiwarat/ibus-input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  input-pad-devel >= 1.0.99
BuildRequires:  intltool
BuildRequires:  libtool
Requires:       ibus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The input pad engine for IBus platform.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libexecdir}/ibus-engine-input-pad
%{_libexecdir}/ibus-setup-input-pad
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-input-pad.desktop

%changelog
