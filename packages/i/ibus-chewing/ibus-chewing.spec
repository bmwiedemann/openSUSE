#
# spec file for package ibus-chewing
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ibus-chewing
Version:        1.5.1
Release:        0
Summary:        The Chewing engine for IBus input platform
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
Url:            https://github.com/definite/ibus-chewing
Source:         https://github.com/definite/ibus-chewing/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://fedorahosted.org/releases/c/m/cmake-fedora/cmake-fedora-modules-only-latest.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gob2
BuildRequires:  ibus-devel >= 1.3
BuildRequires:  libchewing-devel >= 0.3.3
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(x11)
Requires:       ibus >= 1.3
Provides:       locale(zh_TW)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%glib2_gsettings_schema_requires 

%description
IBus-chewing is an IBus front-end of Chewing, an intelligent Chinese input
method for Zhuyin (BoPoMoFo) users.
It supports various Zhuyin keyboard layout, such as standard (DaChen),
IBM, Gin-Yeah, Eten, Eten 26, Hsu, Dvorak, Dvorak-Hsu, and DaChen26.

Chewing also support toned Hanyu pinyin input.

%prep
%setup -q
tar -xzvf %{_sourcedir}/cmake-fedora-modules-only-latest.tar.gz -C .

%build
%cmake -DLIBEXEC_DIR=%{_libdir}/ibus
make %{?_smp_mflags}

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# make translations doesn't work
pushd po
for i in *.po ; do
	mkdir -p %{buildroot}%{_datadir}/locale/`echo $i | sed 's/\.po//'`/LC_MESSAGES/
	msgfmt ${i} -o %{buildroot}%{_datadir}/locale/`echo $i | sed 's/\.po//'`/LC_MESSAGES/%{name}.mo
done
popd

%find_lang %{name}

%post
/sbin/ldconfig
%glib2_gsettings_schema_post

%postun
/sbin/ldconfig
%glib2_gsettings_schema_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{_libdir}/ibus/ibus-engine-chewing
%{_libdir}/ibus/ibus-setup-chewing
%{_datadir}/applications/ibus-setup-chewing.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.IBus.Chewing.gschema.xml
%{_datadir}/ibus-chewing
%{_datadir}/ibus/component/chewing.xml

%changelog
