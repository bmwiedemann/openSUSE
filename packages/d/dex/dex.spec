#
# spec file for package dex
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           dex
Version:        0.10.1
Release:        0
Summary:        DesktopEntry Execution
License:        GPL-3.0-or-later
URL:            https://github.com/jceb/dex
Source:         https://github.com/jceb/dex/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  python3-Sphinx
BuildRequires:  python3-base
Requires:       python3
BuildArch:      noarch

%description
A program to generate and execute Desktop Entry files of type Application
and to process XDG autostart entries.

%prep
%autosetup

%build
# Makefile defaults VERSION to `git tag`; there is no git in the build.
%make_build VERSION=%{version}

%install
%make_install PREFIX=%{_prefix} DOCPREFIX=%{_docdir}/%{name} MANPREFIX=%{_mandir} VERSION=%{version}
rm -rf %{buildroot}%{_docdir}/%{name}
sed -i '1s|#!%{_bindir}/env python3|#!%{_bindir}/python3|' %{buildroot}%{_bindir}/%{name}

%check
%{buildroot}%{_bindir}/%{name} --test -v

%files
%license LICENSE
%doc README.rst CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
