#
# spec file for package ocaml-menhir
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


Name:           ocaml-menhir
Version:        20170712
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        LR(1) parser generator for the OCaml programming language
License:        LGPL-2.0
Group:          Development/Languages/OCaml
Url:            http://gallium.inria.fr/~fpottier/menhir/
Source:         http://gallium.inria.fr/~fpottier/menhir/menhir-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LR(1) parser generator

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n menhir-%{version}

%build
o=
make \
%if 0%{?ocaml_native_compiler}
	TARGET=native \
%else
	TARGET=byte \
%endif
	PREFIX=${o}%{_prefix} \
	%{?_smp_mflags} \
	-j 1

%install
o=%{buildroot}
OCAMLFIND_DESTDIR=%{buildroot}`ocamlc -where`
mkdir -vp ${OCAMLFIND_DESTDIR}
make \
	install \
%if 0%{?ocaml_native_compiler}
	TARGET=native \
%else
	TARGET=byte \
%endif
	PREFIX=${o}%{_prefix} \
	OCAMLFIND_DESTDIR=${OCAMLFIND_DESTDIR} \
	%{?_smp_mflags} \
	-j 1
rm -rfv %{buildroot}/usr/share/doc

%files
%defattr(-,root,root)
%doc CHANGES.md LICENSE manual.pdf
%{_bindir}/*
%{_datadir}/menhir
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/META
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.o
%endif
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmo

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%{_mandir}/*/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.ml

%changelog
