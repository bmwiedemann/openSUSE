#
# spec file for package ocaml-migrate-parsetree
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


Name:           ocaml-migrate-parsetree
Version:        1.4.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Library for conversion between different OCaml parsetrees versions
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml

URL:            https://github.com/ocaml-ppx/ocaml-migrate-parsetree
Source0:        https://github.com/ocaml-ppx/ocaml-migrate-parsetree/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ppx_derivers-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  opam-installer

%description
This library converts between parsetrees of different OCaml versions.
For each version, there is a snapshot of the parsetree and conversion
functions to the next and/or previous version.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
%make_install INSTALL_ARGS='--destdir=%{buildroot}'

# These files will be installed using doc and license directives.
rm -r %{buildroot}/usr/doc

%files
%defattr(-,root,root,-)
%doc README.md MANUAL.md CHANGES.md LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%dir %{_libdir}/ocaml/*/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%dir %{_libdir}/ocaml/*/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*/*.cmxa
%endif
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/META

%changelog
