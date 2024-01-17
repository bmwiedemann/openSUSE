#
# spec file for package ocaml-calendar
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_with ocaml_calendar_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_calendar_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-calendar
Name:           %pkg%nsuffix
Version:        3.0.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective Caml library for managing dates and times
License:        LGPL-2.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/calendar
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
%if 1
BuildRequires:  ocamlfind(re)
BuildRequires:  ocamlfind(unix)
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(calendar)
BuildRequires:  ocamlfind(alcotest)
%endif

%description
Objective Caml library for managing dates and times.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='calendar'
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
dune_test_tolerate_fail='dune_test_tolerate_fail'
%ocaml_dune_test
%endif

%if "%build_flavor" == ""
%files -f %name.files

%files devel -f %name.files.devel

%endif

%changelog
