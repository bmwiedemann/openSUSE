#
# spec file for package gob2
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


Name:           gob2
Version:        2.0.20
Release:        0
Summary:        Preprocessor to Write GObject objects
License:        GPL-2.0-or-later
Group:          Development/Tools/GUI Builders
Url:            http://www.5z.com/jirka/gob.html
Source:         http://download.gnome.org/sources/gob2/2.0/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  glib2-devel >= 2.4.0

%description
GOB is a preprocessor for making GObject objects with
inline C code so that generated files are not editted. The syntax is
inspired by Java, yacc/bison and lex.

%prep
%setup -q
rm src/lexer.c

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm examples/Makefile*

%files
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%doc examples
%{_bindir}/gob2
%{_datadir}/aclocal/gob2.m4
%{_mandir}/man1/gob2.1%{?ext_man}

%changelog
