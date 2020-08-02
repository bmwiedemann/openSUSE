#
# spec file for package sqtop
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define pkg_version 2015-02-08
Name:           sqtop
Version:        2015.02.08
Release:        0
Summary:        'top' for Squid proxy process
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/paleg/sqtop
Source0:        https://github.com/paleg/sqtop/archive/v%{pkg_version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Console applicaton to display information about currently active client connections for a Squid proxy in a convenient way.

%prep
%setup -q -n %{name}-%{pkg_version}

%build
%configure \
  --enable-ui
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README.md
%{_bindir}/sqtop
%{_mandir}/man1/sqtop.1%{ext_man}

%changelog
