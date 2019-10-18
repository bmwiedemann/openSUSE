#
# spec file for package ocaml-curses
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


Name:           ocaml-curses
Version:        1.0.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml bindings for ncurses
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            http://savannah.nongnu.org/projects/ocaml-tmk/
Source0:        http://download.savannah.gnu.org/releases/ocaml-tmk/%{name}-%{version}.tar.gz
Patch0:         curses.const.patch
Patch1:         curses.getsyx.patch
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OCaml bindings for ncurses.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
sed 's/@BOOL_WIDE_CURSES@/true/' config.ml.in | tee config.ml
gcc -x c -E curses.ml | tee curses.ml~
mv -v curses.ml~ curses.ml
tee -a config.h <<_EOF_
#define CURSES_HEADER <ncursesw/curses.h>
#define CURSES_TERM_H <ncursesw/term.h>
#define HAVE_TERMIOS_H 1
#define HAVE_SYS_IOCTL_H 1
_EOF_
rm -fv setup.ml myocamlbuild.ml META* _* */_*
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        curses
Version:     0
Synopsis:    OCaml bindings for ncurses
Authors:     Paul Pelzl
License:     %{license}
LicenseFile: LICENSE
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library curses
 Path: .
 Install: true
 Modules: Curses
 CSources: ml_curses.c, config.h
 CCOpt: %{optflags} -fPIC -I$PWD -Werror -D_GNU_SOURCE -DHAVE_CONFIG_H
 CCLib: -lncursesw

Document curses
 Title:                API reference for curses
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: curses
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
%ocaml_create_file_list

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.files

%files devel -f %{name}.files.devel
%{oasis_docdir_html}

%changelog
