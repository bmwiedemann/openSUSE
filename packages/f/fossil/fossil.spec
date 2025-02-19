#
# spec file for package fossil
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


# From https://fossil-scm.org/home/uv/releases.md
%define fossil_uuid 8f798279d5f7c3288099915f2ea88c57b6d6039f3f05eac5e237897af33376dc
%bcond_without tests
Name:           fossil
Version:        2.25
Release:        0
Summary:        Distributed software configuration management
License:        BSD-2-Clause
Group:          Development/Tools/Version Control
URL:            https://fossil-scm.org/
Source:         https://fossil-scm.org/home/tarball/%{fossil_uuid}/%{name}-%{version}.tar.gz
Patch0:         overflow.patch
BuildRequires:  pkgconfig
BuildRequires:  tcl
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(sqlite3) >= 3.46.0
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
%autosetup -p1
# test package version and source version match
grep -qFx %{version} VERSION

%build
%configure \
	--host="" \
        --with-openssl=%{_prefix} \
        --with-zlib=%{_prefix} \
%if 0%{?suse_version} > 1600
        --disable-internal-sqlite \
	--with-sqlite=%{_prefix} \
%endif
	%{nil}
%make_build

%install
%make_install
install -D -m 644 -t %{buildroot}%{_mandir}/man1 fossil.1

%check
%if %{with tests}
# Tests fail on Leap due to TCL "time value too large/small to represent"
%if 0%{?suse_version} > 1600
tclsh test/tester.tcl %{buildroot}%{_bindir}/%{name}
%endif
%endif

%files
%license COPYRIGHT-BSD2.txt
%{_bindir}/fossil
%{_mandir}/man1/fossil.1%{?ext_man}

%changelog
