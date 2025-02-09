#
# spec file for package ibus-kkc
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


Name:           ibus-kkc
Version:        1.5.22
Release:        0
Summary:        Japanese Kana Kanji input engine for IBus
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/ueno/ibus-kkc
Source:         %{URL}/releases/download/v%{version}/ibus-kkc-%{version}.tar.gz
BuildRequires:  gnome-common
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(ibus-1.0) >= 1.5
BuildRequires:  pkgconfig(kkc-1.0) >= 0.3.4

%description
ibus-kkc is a Japanese Kana Kanji input engine for IBus IMF.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
NOCONFIGURE=1 gnome-autogen.sh
%configure --libexecdir=%{_ibus_libexecdir}
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_ibus_libexecdir}/ibus-engine-kkc
%{_ibus_libexecdir}/ibus-setup-kkc
%{_datadir}/applications/ibus-setup-kkc.desktop
%{_datadir}/ibus-kkc/
%{_datadir}/ibus/component/kkc.xml

%changelog
