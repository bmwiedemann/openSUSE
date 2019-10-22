#
# spec file for package xob
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


Name:           xob
Version:        0.1.1
Release:        0
Summary:        Overlay volume (or anything) bar for the X Window System
License:        GPL-3.0-only
URL:            https://github.com/florentc/xob
Source:         https://github.com/florentc/xob/archive/v%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(x11)

%description
Overlay volume (or anything) bar for the X Window System

%prep
%setup -q

%build
%make_build

%install
%make_install prefix=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/xob
%{_prefix}%{_sysconfdir}/
%{_prefix}%{_sysconfdir}/xob/
%{_mandir}/man1/xob.1%{?ext_man}

%changelog
