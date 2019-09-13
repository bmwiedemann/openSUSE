#
# spec file for package purple-libsteam
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


%global soname  libsteam
Name:           purple-libsteam
Version:        1.6.1
Release:        0
Summary:        Steam plugin for Pidgin/libpurple
License:        GPL-3.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/EionRobb/pidgin-opensteamworks
Source:         https://github.com/EionRobb/pidgin-opensteamworks/archive/%{version}.tar.gz#/pidgin-opensteamworks-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pidgin-opensteamworks-1.6.1-cflags.patch -- Support setting CFLAGS.
Patch0:         pidgin-opensteamworks-1.6.1-cflags.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(purple)

%description
Adds support for Steam to Pidgin, Adium, Finch and other libpurple
based messengers.

%package -n libpurple-plugin-libsteam
Summary:        Steam plugin for libpurple
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple
# purple-libsteam was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libpurple-plugin-libsteam
Adds support for Steam to Pidgin, Adium, Finch and other libpurple
based messengers.

%package -n pidgin-plugin-libsteam
Summary:        Steam plugin for Pidgin
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-libsteam = %{version}
Supplements:    packageand(libpurple-plugin-libsteam:pidgin)
# pidgin-libsteam was last used in openSUSE Leap 42.2.
Provides:       pidgin-libsteam = %{version}-%{release}
Obsoletes:      pidgin-libsteam < %{version}-%{release}
BuildArch:      noarch
%requires_ge    pidgin

%description -n pidgin-plugin-libsteam
Adds support for Steam to Pidgin, Adium, Finch and other libpurple
based messengers.

This package provides the icon set for Pidgin.

%prep
%setup -q -n pidgin-opensteamworks-%{version}
%patch0 -p1
# Fix 'W: wrong-file-end-of-line-encoding'.
sed -i 's/\r$//' README.md

%build
pushd steam-mobile
make %{?_smp_mflags} V=1 \
  CFLAGS="%{optflags}"
popd

%install
install -Dpm 0644 steam-mobile/%{soname}.so \
  %{buildroot}%{_libdir}/purple-2/%{soname}.so

for size in 16 22 48; do
    install -Dpm 0644 "steam-mobile/steam$size.png" \
      "%{buildroot}%{_datadir}/pixmaps/pidgin/protocols/$size/steam.png"
done

%files -n libpurple-plugin-libsteam
%defattr(-,root,root)
%doc README.md
%{_libdir}/purple-2/%{soname}.so

%files -n pidgin-plugin-libsteam
%defattr(-,root,root)
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/steam.*

%changelog
