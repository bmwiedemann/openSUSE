#
# spec file for package jo
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


Name:           jo
Version:        1.2
Release:        0
Summary:        JSON output from a shell
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/jpmens/jo/
#Git-Clone:     https://github.com/jpmens/jo.git
Source:         https://github.com/jpmens/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pandoc

%description
This is jo, a small utility to create JSON objects

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc README ChangeLog AUTHORS
%{_bindir}/jo
%{_mandir}/man1/jo.1%{?ext_man}

%changelog
