#
# spec file for package splint
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


Name:           splint
Version:        3.1.2
Release:        0
Summary:        A tool for statically checking C programs
License:        GPL-2.0+
Group:          Development/Languages/C and C++
Url:            http://www.splint.org/
Source0:        http://www.splint.org/downloads/splint-%{version}.src.tgz
Source1:        %{name}-rpmlintrc
Patch0:         %{name}-3.1.2-fixes.patch
# PATCH-FIX-OPENSUSE https://github.com/ravenexp/splint/issues/8
Patch1:         splint-3.1.2-build-date-override.patch
Patch2:         splint-3.1.2-no-uname.patch
BuildRequires:  flex

%description
With minimal effort, LCLint can be used as a better lint.  If additional
effort is invested adding annotations to programs, LCLint can perform
stronger checks than can be done by any standard lint.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
# Parallel build fails at linking
make --jobs=1 LDFLAGS="-lfl" V=1

%check
make %{?_smp_mflags} test

%install
%make_install
rm -f doc/html/{header,footer}.html

%files
%defattr(644,root,root,755)
%doc README doc/manual.pdf doc/html doc/manual.css
%{_datadir}/splint/
%{_mandir}/man1/*
%defattr(755,root,root)
%{_bindir}/*

%changelog
