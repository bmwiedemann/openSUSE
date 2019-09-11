#
# spec file for package ibus-kkc
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


Name:           ibus-kkc
Version:        1.5.21
Release:        0
Summary:        Japanese Kana Kanji input engine for IBus
License:        GPL-2.0+
Group:          System/I18n/Japanese
Url:            https://gitorious.org/libkkc/ibus-kkc
Source:         %{name}-%{version}.tar.gz
# for autogen.sh
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  libkkc-devel >= 0.3.4
BuildRequires:  vala
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ibus-kkc is a Japanese Kana Kanji input engine for IBus IMF.

%prep
%setup -q

%build
./autogen.sh
%configure --libexecdir=%{_libdir}/ibus
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name}


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README COPYING
%{_libdir}/ibus/ibus-engine-kkc
%{_libdir}/ibus/ibus-setup-kkc
%{_datadir}/applications/ibus-setup-kkc.desktop
%{_datadir}/ibus-kkc/
%{_datadir}/ibus/component/kkc.xml

%changelog
