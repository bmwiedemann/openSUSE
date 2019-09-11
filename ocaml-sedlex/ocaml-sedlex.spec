#
# spec file for package ocaml-sedlex
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


Name:           ocaml-sedlex
Version:        1.99.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Unicode-friendly lexer generator
License:        MIT
Group:          Development/Languages/OCaml

URL:            https://github.com/alainfrisch/sedlex
Source0:        https://github.com/alainfrisch/sedlex/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# https://github.com/ocaml-community/sedlex/issues/64#issuecomment-433198249
Patch0:         ppx_tools_versioned-521.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-gen-devel
BuildRequires:  ocaml-migrate-parsetree-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ppx_tools_versioned-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-rpm-macros

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n sedlex-%{version}
%patch0 -p1

%build
make %{?_smp_mflags}

%if 0%{?ocaml_native_compiler}
make %{?_smp_mflags} opt
%endif

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR

# don't use make_install macro since it passes INSTALL,
# which is used differently in the Makefile
%if 0%{?ocaml_native_compiler}
make install
%else
make install_byteonly
%endif

%files
%defattr(-,root,root,-)
%doc README.md CHANGES
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%{_libdir}/ocaml/*/ppx_sedlex
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/ppx_sedlex.opt
%endif

%files devel
%defattr(-,root,root,-)
%doc README.md CHANGES
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/META

%changelog
