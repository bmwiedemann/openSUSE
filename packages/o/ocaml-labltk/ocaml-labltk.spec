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
Url:            https://forge.ocamlcore.org/projects/labltk/
Source:         labltk-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros >= 4.05.0
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q -n labltk-%{version}

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
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/stublibs
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/labltk
/etc/ld.so.conf.d/*.conf
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%endif
%{_libdir}/ocaml/*/*.so
%{_libdir}/ocaml/*/*.so.owner

%files devel
%defattr(-,root,root,-)
%doc examples_labltk
%doc examples_camltk
%{_bindir}/ocamlbrowser
%{_libdir}/ocaml/*/labltktop
%{_libdir}/ocaml/*/pp
%{_libdir}/ocaml/*/tkcompiler
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmo
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
