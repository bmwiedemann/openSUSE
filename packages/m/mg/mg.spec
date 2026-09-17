#
# spec file for package mg
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


Name:           mg
Version:        4.1
Release:        0
Summary:        Micro GNU Emacs clone
License:        Unlicense
URL:            https://man.troglobit.com/man1/mg.1.html
Source0:        https://github.com/troglobit/mg/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

%description
Mg is micro GNU Emacs clone without lisp interpreter.

%prep
%autosetup -p1

%build
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
rm -f %{buildroot}%{_docdir}/%{name}/UNLICENSE
# hidden example rc; rpmlint hidden-file-or-dir
rm -f %{buildroot}%{_docdir}/%{name}/.mg

%files
%license UNLICENSE
%{_docdir}/%{name}/
%{_bindir}/mg
%{_mandir}/man1/mg.1%{?ext_man}
%dir %{_datadir}/mg
%{_datadir}/mg/tutorial.gz

%changelog
