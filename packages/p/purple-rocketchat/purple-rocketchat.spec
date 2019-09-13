#
# spec file for package purple-rocketchat
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


%define _name   rocketchat
Name:           purple-rocketchat
Version:        0.0+hg20190218
Release:        0
Summary:        RocketChat protocol plugin for libpurple
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://bitbucket.org/EionRobb/purple-rocketchat
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(purple)

%description
RocketChat protocol plugin for libpurple-based applications.

%package -n libpurple-plugin-%{_name}
Summary:        RocketChat protocol plugin for libpurple
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple

%description -n libpurple-plugin-%{_name}
RocketChat protocol plugin for libpurple-based applications.

%package -n pidgin-plugin-%{_name}
Summary:        RocketChat protocol plugin for Pidgin
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-%{_name} = %{version}
%requires_ge    pidgin
Supplements:    packageand(libpurple-plugin-%{_name}:pidgin)
BuildArch:      noarch

%description -n pidgin-plugin-%{_name}
RocketChat protocol plugin for libpurple-based applications.

This package provides the icon set for Pidgin.

%prep
%setup -q

%build
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libpurple-plugin-%{_name}
%license LICENSE
%doc README.md
%{_libdir}/purple-2/lib%{_name}.so

%files -n pidgin-plugin-%{_name}
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/%{_name}.*

%changelog
