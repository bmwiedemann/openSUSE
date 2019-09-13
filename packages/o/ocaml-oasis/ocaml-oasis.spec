#
# spec file for package ocaml-oasis
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


%global __ocaml_requires_opts -i OASISAstTypes -i MainGettext
Name:           ocaml-oasis
Version:        0.4.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Architecture for building OCaml libraries and applications
License:        LGPL-2.1
Group:          Development/Languages/OCaml

Url:            http://oasis.forge.ocamlcore.org/
Source0:        oasis-%{version}.tar.xz
Patch0:         ocaml-oasis.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       ocamlfind(findlib)
Requires:       ocamlfind(ocamlbuild)

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlify
BuildRequires:  ocamlmod
BuildRequires:  ocamlfind(dynlink)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(ocamlbuild)
BuildRequires:  ocamlfind(unix)

%description
OASIS generates a full configure, build and install system for your
application. It starts with a simple `_oasis` file at the toplevel of
your project and creates everything required.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n oasis-%{version}
%patch0 -p1

%build
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root,-)
%doc COPYING.txt CHANGES.txt
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%{oasis_docdir_html}
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
