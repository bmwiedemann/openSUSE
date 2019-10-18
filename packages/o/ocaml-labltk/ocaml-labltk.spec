#
# spec file for package ocaml-labltk
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


Name:           ocaml-labltk
Version:        8.06.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Tcl/Tk framework for ocaml
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/garrigue/labltk
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml = 4.05.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRequires:  tcl-devel
BuildRequires:  tk-devel

%description
LablTk is an interface to the Tcl/Tk GUI framework. It allows to
develop GUI applications in a speedy and type safe way. A legacy
Camltk interface is included. The OCamlBrowser library viewer is
also part of this project.

%package devel
Summary:        Development files for labltk
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       tcl-devel
Requires:       tk-devel
Requires:       xorg-x11-libX11-devel

%description devel
Labltk is a library for interfacing Objective Caml with the scripting
language Tcl/Tk.

This package contains the development files.  It includes the ocaml
browser for code editing and library browsing.
%prep
%autosetup -p1

%build
./configure --use-findlib
make \
	byte
%if 0%{?ocaml_native_compiler}
make \
	opt
%endif

%install
ld_conf=$PWD/ld.conf
> $ld_conf
d="$RPM_BUILD_ROOT`ocamlfind printconf destdir`"
mkdir -vp $d/labltk
mkdir -vp $d/stublibs
env \
OCAMLFIND_LDCONF=$ld_conf \
OCAMLFIND_DESTDIR=$d \
make \
	BINDIR="$RPM_BUILD_ROOT%{_bindir}" \
	INSTALLDIR=$d/labltk \
	STUBLIBDIR=$d/stublibs \
	install

find examples* -type f -exec chmod -v 644 {} \;
cat $ld_conf
#
%ocaml_create_file_list

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.files
%{_bindir}/*

%files devel -f %{name}.files.devel
%{_libdir}/ocaml/*/labltktop
%{_libdir}/ocaml/*/pp
%{_libdir}/ocaml/*/tkcompiler

%changelog
