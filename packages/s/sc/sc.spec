#
# spec file for package sc
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Guido Berhoerster.
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


Name:           sc
Version:        7.16
Release:        0
Summary:        Spreadsheet Calculator
License:        SUSE-Public-Domain
Group:          Productivity/Office/Spreadsheets
Url:            http://ibiblio.org/pub/Linux/apps/financial/spreadsheet/
Source:         http://ibiblio.org/pub/Linux/apps/financial/spreadsheet/sc-%{version}.tar.gz
Patch0:         sc-fix-malloc-redefinition.patch
Patch1:         sc-fix-missing-includes.patch
Patch2:         sc-fix-uninitialized-variables.patch
Patch3:         sc-fix-execl-call.patch
Patch4:         sc-fix-missing-return-value.patch
Patch5:         sc-fix-conflicting-macro.patch
Patch6:         sc-fix-missing-prototypes.patch
Patch7:         sc-fix-parentheses.patch
Patch8:         sc-do-not-use-reserved-symbols.patch
Patch9:         sc-fix-eval-parser.patch
BuildRequires:  bison
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
sc is a free curses-based spreadsheet program that uses key bindings similar to
vi and less.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
make %{?_smp_mflags} LIBDIR="%{_docdir}/%{name}" CFLAGS="%{optflags} -DSYSV3" all sc.1 psc.1

%install
install -p -D -m 755 sc "%{buildroot}%{_bindir}/sc"
install -p -D -m 755 psc "%{buildroot}%{_bindir}/psc"
install -p -D -m 755 scqref "%{buildroot}%{_bindir}/pscqref"
install -p -D -m 644 sc.1 "%{buildroot}%{_mandir}/man1/sc.1"
install -p -D -m 644 psc.1 "%{buildroot}%{_mandir}/man1/psc.1"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES README tutorial.sc
%doc %{_mandir}/man1/sc.1*
%doc %{_mandir}/man1/psc.1*
%{_bindir}/sc
%{_bindir}/psc
%{_bindir}/pscqref

%changelog
