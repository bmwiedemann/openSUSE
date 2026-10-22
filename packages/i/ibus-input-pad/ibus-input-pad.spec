#
# spec file for package ibus-input-pad
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ibus-input-pad
Version:        1.5.0
Release:        0
Summary:        Input Pad for IBus
License:        GPL-2.0-or-later
URL:            https://github.com/fujiwarat/ibus-input-pad
Source0:        https://github.com/fujiwarat/ibus-input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0) >= 2.37
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5.3
BuildRequires:  pkgconfig(input-pad) >= 1.0.99
Requires:       ibus

%description
The input pad engine for IBus platform.

%prep
%setup -q

%build
%configure --disable-static --libexecdir=%{_ibus_libexecdir}
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_ibus_libexecdir}/ibus-engine-input-pad
%{_ibus_libexecdir}/ibus-setup-input-pad
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-input-pad.desktop

%changelog
