#
# spec file for package logtop
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           logtop
Version:        0.7
Release:        0
Summary:        Statistics generator for logs
License:        BSD-2-Clause
Group:          Productivity/Text/Utilities
URL:            https://julienpalard.github.io/logtop/
Source:         https://github.com/JulienPalard/logtop/archive/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(ncursesw)

%description
Logtop is a basic log analyzer.
It allows piping logs into it to obtain statistics.

%prep

%setup -q -n %{name}-%{name}-%{version}

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install
install -D -m0644 doc/logtop.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog README.md
%license COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
