#
# spec file for package seafile
#
# Copyright (c) 2023 SUSE LLC
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


Name:           seafile
Version:        8.0.10
Release:        0
Summary:        Cloud storage client
License:        GPL-2.0-only
URL:            https://github.com/haiwen/seafile/
Source0:        https://github.com/haiwen/seafile/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  libsearpc-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_core)
BuildRequires:  pkgconfig(libevent_extra)
BuildRequires:  pkgconfig(libevent_openssl)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  sqlite-devel
%else
BuildRequires:  pkgconfig(sqlite3)
%endif

%description
Seafile is an open source cloud storage system with features on privacy protection and teamwork. Collections of files are
called libraries, and each library can be synced separately. A library can also be encrypted with a user chosen password.
Seafile also allows users to create groups and easily sharing files into groups.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     libseafile0
Summary:        Library files for %{name}

%description -n libseafile0
The libseafile0 package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n seafile-%{version}
sed -i -e /\(DESTDIR\)/d lib/libseafile.pc.in
sed -i -e 's@#!%{_bindir}/env python@#!%{_bindir}/python3@' app/seaf-cli
sed -i -e 's@#!%{_bindir}/python33@#!%{_bindir}/python3@' app/seaf-cli

%build
./autogen.sh
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name 'seafile.desktop' -exec rm -f {} ';'
find %{buildroot} -type f -name "*.opt-1.pyc" -delete -print

%post -n libseafile0 -p /sbin/ldconfig
%postun -n libseafile0 -p /sbin/ldconfig

%files
%doc README.markdown
%license LICENSE.txt
%{python3_sitearch}/%{name}/
%{python3_sitearch}/seafile/
%{_bindir}/seaf-cli
%{_bindir}/seaf-daemon
%{_mandir}/man1/*.1%{?ext_man}

%files -n libseafile0
%{_libdir}/libseafile.so.0*

%files devel
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog
