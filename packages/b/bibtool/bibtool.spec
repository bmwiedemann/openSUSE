#
# spec file for package bibtool
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           bibtool
Version:        2.68
Release:        0
Summary:        Tool for Manipulating BibTeX Databases
License:        CC-BY-SA-3.0 AND GPL-1.0-or-later
URL:            http://www.gerd-neugebauer.de/software/TeX/BibTool/index.en.html
Source0:        http://www.gerd-neugebauer.de/software/TeX/BibTool/BibTool-%{version}.tar.gz
Source1:        http://www.gerd-neugebauer.de/software/TeX/BibTool/BibTool-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch1:         bibtool-use-system-regex.patch
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BibTool is a tool for manipulating BibTeX databases. BibTeX provides a means to
integrate citations into LaTeX documents. BibTool allows the manipulation of
BibTeX files which goes beyond the possibilities - and intentions - of BibTeX.

%prep
%setup -q -n BibTool
# %%patch -P 1 -p1

%build
%configure
make %{?_smp_mflags} all

%install
make INSTALLPREFIX=%{buildroot} install install-man

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%attr(0644,root,root) %{_mandir}/man1/bibtool.1%{ext_man}
%{_bindir}/bibtool
%{_libdir}/BibTool

%changelog
