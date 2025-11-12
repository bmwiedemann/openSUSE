#
# spec file for package ocaml-pcre2
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%bcond_with ocaml_pcre2_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_pcre2_testsuite}
ExclusiveArch:  do-not-build
%else
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-pcre2
Name:           %pkg%nsuffix
Version:        8.0.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Bindings to the Perl Compatibility Regular Expressions library (version 2)
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://opam.ocaml.org/packages/pcre2
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version)
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(pcre2)
%endif
%description
pcre2-ocaml offers library functions for string pattern matching and
substitution, similar to the functionality offered by the Perl language.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version
Requires:       pkgconfig(libpcre2-8)

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q -n %pkg-%version

%build
dune_release_pkgs='pcre2'
%ocaml_dune_setup
%if "%build_flavor" == ""
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == ""
%ocaml_dune_install
%ocaml_create_file_list
%endif

%if "%build_flavor" == "testsuite"
%check
%ocaml_dune_test
%endif

%if "%build_flavor" == ""
%files -f %name.files
%defattr(-,root,root,-)

%files devel -f %name.files.devel
%defattr(-,root,root,-)
%doc README.md

%endif

%changelog
