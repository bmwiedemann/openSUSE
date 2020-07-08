#
# spec file for package fossil
#
# Copyright (c) 2020 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without system_sqlite
%else
%bcond_with system_sqlite
%endif
Name:           fossil
Version:        2.11.1
Release:        0
Summary:        Distributed software configuration management
License:        BSD-2-Clause
Group:          Development/Tools/Version Control
URL:            https://www.fossil-scm.org/
Source:         https://www.fossil-scm.org/index.html/uv/%{name}-src-%{version}.tar.gz
Patch1:         fossil-2.7-remove_date_time.patch
# PATCH-FIX-UPSTREAM https://fossil-scm.org/fossil/info/1a894c08206f4c71bcc3
Patch2:         fossil-2.11-reproducible.patch
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  tcl
BuildRequires:  zlib-devel
%if %{with system_sqlite}
BuildRequires:  sqlite3-devel >= 3.25.0
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
%setup -q
# test package version and source version match
grep -qFx %{version} VERSION
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -DFOSSIL_BUILD_EPOCH=${SOURCE_DATE_EPOCH:-42}"
# FIXME: you should use the %%configure macro
./configure \
        --prefix=%{_prefix} \
        --with-openssl=auto \
%if %{with system_sqlite}
        --disable-internal-sqlite
%endif

make %{?_smp_mflags}

%install
%make_install

%files
%license COPYRIGHT-BSD2.txt
%{_bindir}/fossil

%changelog
