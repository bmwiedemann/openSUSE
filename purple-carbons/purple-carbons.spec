#
# spec file for package purple-carbons
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


%define _name carbons
%define _purple_plugindir %(pkg-config --variable plugindir purple)
Name:           purple-carbons
Version:        0.2.2
Release:        0
Summary:        Experimental XEP-0280: Message Carbons plugin for libpurple
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/gkdr/carbons
Source:         https://github.com/gkdr/%{_name}/archive/v%{version}.tar.gz#/%{_name}-%version.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(purple)

%description
Experimental XEP-0280: Message Carbons plugin for libpurple
(Pidgin, Finch, etc).

%package -n libpurple-plugin-%{_name}
Summary:        Experimental XEP-0280: Message Carbons plugin for libpurple
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple

%description -n libpurple-plugin-%{_name}
Experimental XEP-0280: Message Carbons plugin for libpurple
(Pidgin, Finch, etc).

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
make %{?_smp_mflags} V=1

%install
%make_install \
  PURPLE_PLUGIN_DIR="%{_purple_plugindir}"

%files -n libpurple-plugin-%{_name}
%doc README.md
%{_purple_plugindir}/%{_name}.so

%changelog
