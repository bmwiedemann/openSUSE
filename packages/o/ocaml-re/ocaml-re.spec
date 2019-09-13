#
# spec file for package ocaml-re
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ocaml-re
Version:        1.7.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Pure OCaml regular expressions
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml/ocaml-re
Source:         https://github.com/ocaml/ocaml-re/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pure OCaml regular expressions, with support for Perl and POSIX-style strings.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

%build
dune build @install -p re

%install
mkdir -p %{buildroot}%{_libdir}/ocaml

# do not use jbuilder install, which depends on opam-installer,
# which is built from the opam package that depends on re.
cp -rL _build/install/default/lib/* %{buildroot}%{_libdir}/ocaml

%files
%defattr(-,root,root)
%doc README.md CHANGES.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%dir %{_libdir}/ocaml/*/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc README.md CHANGES.md
%license LICENSE.md
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
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
