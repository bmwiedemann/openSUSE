#
# spec file for package purple-lurch
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   lurch
Name:           purple-lurch
Version:        0.7.0
Release:        0
Summary:        OMEMO for libpurple
License:        GPL-3.0-only
URL:            https://github.com/gkdr/lurch
Source:         %{_name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libpurple
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(sqlite3)

%description
This plugin brings Double Ratchet to libpurple applications such as
Pidgin by implementing OMEMO.

%package -n libpurple-plugin-%{_name}
Summary:        OMEMO for libpurple
Recommends:     libpurple-plugin-carbons
Enhances:       libpurple

%description -n libpurple-plugin-%{_name}
This plugin brings Double Ratchet to libpurple applications such as
Pidgin by implementing OMEMO.

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS='%{optflags}'
%make_build

%install
%make_install

%files -n libpurple-plugin-%{_name}
%license LICENSE
%doc README.md
%{_libdir}/purple-2/%{_name}.so

%changelog
