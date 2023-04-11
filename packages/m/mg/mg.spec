#
# spec file for package mg
#
# Copyright (c) 2022-2023 Tomasz Hołubowicz <alternateved@pm.me>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           mg
Version:        3.6
Release:        0
Summary:        Micro GNU Emacs clone
License:        Unlicense
Group:          Productivity/Text/Editors
URL:            https://man.troglobit.com/man1/mg.1.html
Source:         https://github.com/troglobit/mg/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf automake
BuildRequires:  ncurses-devel

%description
Mg is micro GNU Emacs clone without lisp interpreter.

%prep
%setup -q

%build
autoreconf -i
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ %{buildroot}%{_docdir}/%{name}/

rm %{buildroot}/usr/share/mg/tutorial.gz
rm %{buildroot}/usr/share/doc/packages/mg/.mg
rm %{buildroot}/usr/share/doc/packages/mg/UNLICENSE

%files
%license UNLICENSE
%doc README.md ChangeLog.md tutorial
%doc %{_docdir}/mg/
%{_bindir}/mg
%{_mandir}/man1/mg.1%{?ext_man}

%changelog
