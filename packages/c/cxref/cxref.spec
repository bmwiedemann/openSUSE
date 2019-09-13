#
# spec file for package cxref
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 by Philipp Thomas <pth@suse.de>
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


Name:           cxref
Version:        1.6e
Release:        0
Summary:        C Cross Referencing & Documenting tool
License:        GPL-2.0
Group:          Development/Tools/Building
Url:            http://www.gedanken.org.uk/software/cxref/
Source0:        http://www.gedanken.org.uk/software/cxref/download/%{name}-%{version}.tgz
Source1:        http://www.gedanken.org.uk/software/cxref/download/%{name}-%{version}.tgz.asc
Source2:        %{name}.keyring
Patch0:         allow_redirect_of_cxref_cpp_configure_output_in_postinst.patch
Patch1:         cxref-new_float_types.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cxref is a program that will produce documentation (in LaTeX, HTML, RTF or SGML)
including cross-references from C program source code.

Works for ANSI C, including most gcc extensions.

The documentation for the program is produced from comments in the code that
are appropriately formatted. The cross referencing comes from the code itself
and requires no extra work.

The documentation is produced for each of the following:

Files            - A comment that applies to the whole file.
Functions        - A comment for the function, including a description of
                   each of the arguments and the return value.
Variables        - A comment for each of a group of variables and/or
                   individual variables.
#include         - A comment for each included file.
#define          - A comment for each pre-processor symbol definition, and
                   for macro arguments.
Type definitions - A comment for each defined type and for each element of a
                   structure or union type.

Any or all of these comments can be present in suitable places in the
source code.

The cross referencing is performed for the following items

Files           - The files that the current file is included in
                  (even when included via other files).

#includes       - Files included in the current file.
                - Files included by these files etc.

Variables       - The location of the definition of external variables.
                - The files that have visibility of global variables.
                - The files / functions that use the variable.

Functions       - The file that the function is prototyped in.
                - The functions that the function calls.
                - The functions that call the function.
                - The files and functions that reference the function.
                - The variables that are used in the function.

Each of these items is cross referenced in the output.

Includes extensive README and FAQ with details and examples on how to use the
program.

%prep
%setup -q
%patch0 -p1
%patch1

%build
export CFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}
make %{?_smp_mflags} docs

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -m 755 contrib/knr2ansi.pl %{buildroot}%{_bindir}/knr2ansi

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1.gz

%changelog
