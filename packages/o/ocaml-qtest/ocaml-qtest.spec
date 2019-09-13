#
# spec file for package ocaml-qtest
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


Name:           ocaml-qtest
Version:        2.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Inline (Unit) Tests for OCaml
License:        GPL-3.0-or-later
Group:          Development/Languages/OCaml

URL:            https://github.com/vincent-hugot/qtest
Source0:        https://github.com/vincent-hugot/qtest/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  help2man
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  opam-installer

%description
qtest extracts inline unit tests written using a special syntax in
comments. Those tests are then run using the oUnit framework and the
qcheck library. The possibilities range from trivial tests
to sophisticated random generation of test cases.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n qtest-%{version}

%build
dune build @install --profile=release

%install
dune install --destdir="%{buildroot}" --verbose

# These files will be installed using the doc and license directives
rm %{buildroot}/usr/doc/qtest/{LICENSE,README.adoc}

# generate manpage
mkdir -p %{buildroot}/%{_mandir}/man1/
help2man %{buildroot}/%{_bindir}/qtest \
    --output %{buildroot}/%{_mandir}/man1/qtest.1 \
    --name "Inline (Unit) Tests for OCaml" \
    --version-string %{version} \
    --no-info

%files
%defattr(-,root,root,-)
%doc README.adoc HOWTO.adoc
%license LICENSE
%{_bindir}/qtest
%{_mandir}/man1/qtest.1*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%dir %{_libdir}/ocaml/*/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc README.adoc HOWTO.adoc
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%dir %{_libdir}/ocaml/*/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*/*.a
%{_libdir}/ocaml/*/*/*.cmx
%{_libdir}/ocaml/*/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*/*.cma
%{_libdir}/ocaml/*/*/*.cmi
%{_libdir}/ocaml/*/*/*.cmt
%{_libdir}/ocaml/*/*/*.ml
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/dune-package

%changelog
