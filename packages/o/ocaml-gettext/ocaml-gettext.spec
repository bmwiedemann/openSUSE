#
# spec file for package ocaml-gettext
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with ocaml_gettext_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_gettext_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-gettext
Name:           %pkg%nsuffix
Version:        0.4.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml library for i18n
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/gettext
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20220222
%if 1
BuildRequires:  ocamlfind(camomile)
BuildRequires:  ocamlfind(compiler-libs.common)
BuildRequires:  ocamlfind(cppo)
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(fileutils)
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(fileutils)
BuildRequires:  ocamlfind(gettext)
BuildRequires:  ocamlfind(oUnit)
BuildRequires:  ocamlfind(str)
%endif

# ocaml-gettext program needs camomile data files
Requires:       ocaml-camomile-data
#
Obsoletes:      ocaml-gettext-camomile < %version-%release
Obsoletes:      ocaml-gettext-stub < %version-%release
Obsoletes:      ocaml-gettext-stub-debuginfo < %version-%release
Obsoletes:      ocaml-gettext-stub-devel < %version-%release
Provides:       ocaml-gettext-camomile = %version-%release
Provides:       ocaml-gettext-stub = %version-%release
Provides:       ocaml-gettext-stub-debuginfo = %version-%release
Provides:       ocaml-gettext-stub-devel = %version-%release

%description
Ocaml-gettext provides support for internationalization of Ocaml
programs.

Constraints :

* provides a pure Ocaml implementation,
* the API should be as close as possible to GNU gettext,
* provides a way to automatically extract translatable
  strings from Ocaml source code.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
Obsoletes:      ocaml-gettext-camomile-devel < %version-%release
Provides:       ocaml-gettext-camomile-devel = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='gettext,gettext-camomile,gettext-stub'
%ocaml_dune_setup
%if "%build_flavor" == ""
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == ""
%ocaml_dune_install
%ocaml_create_file_list
grep -m1 '%%dir' %name.files.devel | tee %name.files.stub-devel
%endif

%if "%build_flavor" == "testsuite"
%check
%ocaml_dune_test
%endif

%if "%build_flavor" == ""
%files -f %name.files
%_bindir/*
%_mandir/*/*

%files devel -f %name.files.devel

%endif

%changelog
