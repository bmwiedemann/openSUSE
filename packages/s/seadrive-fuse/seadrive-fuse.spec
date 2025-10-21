#
# spec file for package seadrive-fuse
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           seadrive-fuse
Version:        3.0.16
Release:        0
Summary:        SeaDrive daemon with FUSE interface
License:        GPL-2.0-only
URL:            https://github.com/haiwen/seadrive-fuse/
Source0:        https://github.com/haiwen/seadrive-fuse/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  argon2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  fuse-devel >= 2.7.3
BuildRequires:  intltool
BuildRequires:  libsearpc-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel >= 4.0.20
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)

%description
The Drive client enables you to access files on the server without
syncing to local disk. It works like a network drive.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%fdupes %{buildroot}%{python3_sitearch}/seadrive

%files
%doc README.md
%license LICENSE
%{_bindir}/seadrive
%dir %{python3_sitearch}/seadrive
%{python3_sitearch}/seadrive/__init__.py
%{python3_sitearch}/seadrive/rpcclient.py
%dir %{python3_sitearch}/seadrive/__pycache__
%{python3_sitearch}/seadrive/__pycache__/__init__.cpython*
%{python3_sitearch}/seadrive/__pycache__/rpcclient.cpython*

%changelog
