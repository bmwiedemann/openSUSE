#
# spec file for package httperf
#
# Copyright (c) 2024 SUSE LLC
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


Name:           httperf
Version:        0.9.0+git.20201206
Release:        0
Summary:        A tool for measuring web server performance
License:        SUSE-GPL-2.0+-with-openssl-exception
URL:            https://github.com/httperf/httperf
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
httperf is a tool for measuring web server performance. It provides a
flexible facility for generating various HTTP workloads and for measuring
server performance.

%prep
%autosetup
chmod -x AUTHORS ChangeLog NEWS README.md TODO

%build
mkdir m4
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README.md TODO
%{_bindir}/httperf
%{_mandir}/man1/httperf.1%{?ext_man}
%{_mandir}/man1/idleconn.1%{?ext_man}

%changelog
