#
# spec file for package extrace
#
# Copyright (c) 2023 SUSE LLC
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


Name:           extrace
Version:        0.9
Release:        0
Summary:        Traces all program executions occurring on a system
License:        GPL-2.0-only
URL:            https://github.com/leahneukirchen/extrace
Source:         extrace-%{version}.tar.xz

%description
extrace traces all program executions occurring on a system and prints the process call hierarchy in a human-readable form.

While process tracing is exact, looking up all information is inherently sensitive to race conditions. In doubt, you can only trust the PID was written correctly.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=/usr
mkdir %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/extrace %{buildroot}%{_sbindir}/extrace
# Avoid conflict with procps:
mv %{buildroot}%{_bindir}/pwait %{buildroot}%{_sbindir}/extrace-pwait
mv %{buildroot}%{_mandir}/man1/pwait.1 %{buildroot}%{_mandir}/man1/extrace-pwait.1

%files
%license LICENSE
%doc NEWS.md README
%{_mandir}/man1/extrace.1%{?ext_man}
%{_mandir}/man1/extrace-pwait.1%{?ext_man}
%{_sbindir}/extrace
%{_sbindir}/extrace-pwait

%changelog
