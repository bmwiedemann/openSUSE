#
# spec file for package purple-mattermost
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   mattermost
Name:           purple-mattermost
Version:        1.2
Release:        0
Summary:        A libpurple/Pidgin plugin to connect to Mattermost
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/EionRobb/purple-mattermost
Source:         https://github.com/EionRobb/purple-mattermost/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(purple)

%description
A third-party plugin for the Pidgin multi-protocol instant
messenger.
It connects libpurple-based instant messaging clients with the
Mattermost server.

%package -n libpurple-plugin-%{_name}
Summary:        A libpurple plugin to connect to Mattermost
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple

%description -n libpurple-plugin-%{_name}
A third-party plugin for the Pidgin multi-protocol instant
messenger.
It connects libpurple-based instant messaging clients with the
Mattermost server.

This package provides the protocol plugin for libpurple clients.

%package -n pidgin-plugin-%{_name}
Summary:        A Pidgin plugin to connect to Mattermost
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-%{_name} = %{version}
%requires_ge    pidgin
Supplements:    packageand(libpurple-plugin-%{_name}:pidgin)
BuildArch:      noarch

%description -n pidgin-plugin-%{_name}
A third-party plugin for the Pidgin multi-protocol instant
messenger.
It connects libpurple-based instant messaging clients with the
Mattermost server.

This package provides the icon set for Pidgin.

%prep
%setup -q

%build
make %{?_smp_mflags} V=1 \
  CFLAGS="%{optflags} -DMATTERMOST_PLUGIN_VERSION='\"%{version}\"'"

%install
%make_install

%files -n libpurple-plugin-%{_name}
%license LICENSE
%doc README.md VERIFICATION.md
%{_libdir}/purple-2/lib%{_name}.so

%files -n pidgin-plugin-%{_name}
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/%{_name}.*

%changelog
