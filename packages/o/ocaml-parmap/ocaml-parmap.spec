#
# spec file for package ocaml-parmap
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-parmap
Version:        20190330.8d19c66
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Multicore architecture exploitation for OCaml programs with minimal modifications
License:        LGPL-2.0-only
Group:          Development/Languages/OCaml
URL:            http://rdicosmo.github.io/parmap/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(graphics)
BuildRequires:  ocamlfind(unix)
BuildRequires:  pkgconfig(x11)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
If you want to use your many cores to accelerate an operation
which happens to be a map, fold or map/fold (map-reduce), just use
Parmap's parmap, parfold and parmapfold primitives in place of the
standard List.map and friends; you can specify the number of
subprocesses to use with the optional parameter ncores, and the
size of granularity of the parallel computation with the optional
parameter chunksize.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

%build
echo -n > config.h
if grep -w sched_setaffinity /usr/include/sched.h
then
tee -a config.h <<_EOF_
#define HAVE_DECL_SCHED_SETAFFINITY 1
_EOF_
fi
rm -fv setup.ml myocamlbuild.ml META* _* */_*
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        parmap
Version:     0
Synopsis:    library to exploit multicore architectures (parallel programming)
Authors:     Marco Danelutto and Roberto Di Cosmo
License:     WTFPL
LicenseFile: LICENSE
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library parmap
 Path: .
 Install: true
 Modules: Parmap
 CSources: bytearray_stubs.c, setcore_stubs.c, config.h
 CCOpt: %{optflags} -I$PWD -Werror -D_GNU_SOURCE

Document parmap
 Title:                API reference for parmap
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: parmap

Executable "%{name}-mandels"
 Install: true
 Path: example
 MainIs: mandels.ml
 CompiledObject: best
 BuildDepends: parmap, graphics, unix, bigarray
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/parmap
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README.md LICENSE
/etc/ld.so.conf.d/*.conf
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.so

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%{oasis_docdir_html}
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
