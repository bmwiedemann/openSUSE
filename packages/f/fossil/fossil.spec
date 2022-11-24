#
# spec file for package fossil
#
# Copyright (c) 2022 SUSE LLC
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


%define fossil_uuid 210e89a0597f225f49722b096cf5563bf193e920e02a9bd38503a906deacd416
%if 0%{?suse_version} > 1500
%bcond_without system_sqlite
%else
%bcond_with system_sqlite
%endif
%bcond_without tests
Name:           fossil
Version:        2.20
Release:        0
Summary:        Distributed software configuration management
License:        BSD-2-Clause
Group:          Development/Tools/Version Control
URL:            https://fossil-scm.org/
Source:         https://fossil-scm.org/home/tarball/%{fossil_uuid}/%{name}-%{version}.tar.gz
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  tcl
BuildRequires:  zlib-devel
%if %{with system_sqlite}
BuildRequires:  sqlite3-devel >= 3.38.0
%endif

%description
Fossil is a distributed software configuration management system with
these features:
* integrated bug tracking and wiki
* built-in web-interface
* uses HTTP, with proxy support
* everything is in a single executable and CGI-enabled
* sqlite-backed database

%prep
%autosetup -p0
# test package version and source version match
grep -qFx %{version} VERSION

%build
%{?set_build_flags: %{set_build_flags}}
%{!?set_build_flags: export CFLAGS="%{optflags}"}
# FIXME: you should use the %%configure macro
./configure \
        --prefix=%{_prefix} \
        --with-openssl=auto \
%if %{with system_sqlite}
        --disable-internal-sqlite
%endif

%make_build

%install
%make_install
install -D -m 644 -t %{buildroot}%{_mandir}/man1 fossil.1

%check
%if %{with tests}
tclsh test/tester.tcl %{buildroot}%{_bindir}/%{name}
%endif

%files
%license COPYRIGHT-BSD2.txt
%{_bindir}/fossil
%{_mandir}/*/*

%changelog
