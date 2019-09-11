#
# spec file for package ocaml-result
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   result
Name:           ocaml-result
Version:        1.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Compatibility OCaml Result module
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/janestreet/result
Source:         %{_name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Projects that want to use the new result type defined in OCaml >= 4.03 while
staying compatible with older version of OCaml should use the Result module
defined in this library.

%package devel
Summary:        Compatibility OCaml Result module -- Development files
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Projects that want to use the new result type defined in OCaml >= 4.03 while
staying compatible with older version of OCaml should use the Result module
defined in this library.

This package contains development files for %{name}.

%prep
%setup -q -n %{_name}-%{version}

%build
make result.ml
rm -fv setup.ml myocamlbuild.ml META* _* */_* 
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        %{_name}
Version:     0
Synopsis:    Result type
Authors:     Jane Street Group, LLC <opensource@janestreet.com>
License:     %{license}
LicenseFile: LICENSE
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library %{_name}
 Path: .
 Install: true
 Modules: Result

Document %{_name}
 Title:                API reference for %{_name}
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: %{_name}
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%{oasis_docdir_html}
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
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/META

%changelog
