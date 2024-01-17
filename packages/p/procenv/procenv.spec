#
# spec file for package procenv
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           procenv
Version:        0.60
Release:        0
Summary:        Process Environment Dump Tool
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://launchpad.net/procenv/
Source:         https://github.com/jamesodhunt/procenv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libcap-devel
BuildRequires:  libnuma-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

%description
procenv is a tool that dumps all attributes of its environment. It can be run
as a test tool, to understand what environment a process runs in and for system
comparison.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
