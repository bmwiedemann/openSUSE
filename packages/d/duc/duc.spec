#
# spec file for package duc
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


Name:           duc
Version:        1.4.4
Release:        0
Summary:        Collection of tools for inspecting and visualizing disk usage
License:        LGPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/zevv/duc
Source:         https://github.com/zevv/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cairo-devel
BuildRequires:  libglfw-devel
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  sqlite3-devel
BuildRequires:  pkgconfig(gobject-2.0)

%description
Duc is a collection of tools for inspecting and visualizing disk usage.

Duc scales quite well, it has been tested on systems with more than 500 million files and several petabytes of storage.

%prep
%setup -q

%build
# add missing linker dependency to gobject library
LIBS="`pkg-config --libs gobject-2.0`"
export LIBS
%configure --enable-opengl \
  --disable-x11 \
  --enable-cairo \
  --with-db-backend=sqlite3

make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc ChangeLog
%{_bindir}/duc
%{_mandir}/man1/duc.1%{ext_man}

%changelog
