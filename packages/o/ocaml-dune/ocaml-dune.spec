#
# spec file for package ocaml-dune
#
# Copyright (c) 2021 SUSE LLC
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

%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == ""
%define nsuffix %{nil}
%else
%define nsuffix -%{build_flavor}
%endif

%define     pkg ocaml-dune
Name:           %{pkg}%{nsuffix}
Version:        2.8.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        A composable build system for OCaml
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/dune
Source0:        %{pkg}-%{version}.tar.xz
Requires:       ocamlfind(compiler-libs)
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
%if "%{build_flavor}" == ""
BuildRequires:  ocamlfind(compiler-libs)
%description
A composable build system for OCaml
%endif
%if "%{build_flavor}" == "configurator"
BuildRequires:  ocaml-dune = %{version}
BuildRequires:  ocamlfind(csexp)
BuildRequires:  ocamlfind(result)
%description
dune-configurator is a small library that helps writing OCaml scripts that
test features available on the system, in order to generate config.h
files for instance.
Among other things, dune-configurator allows one to:
- test if a C program compiles
- query pkg-config
- import #define from OCaml header files
- generate config.h file
%endif

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{pkg}-%{version}

%build
%if "%{build_flavor}" == ""
mv -vb src/dune_rules/setup.defaults.ml src/dune_rules/setup.ml
ocaml configure.ml '--libdir=%{ocaml_standard_library}' '--mandir=%{_mandir}'
ocaml bootstrap.ml
rm -rfv        '%{_tmppath}/%{name}-%{release}'
mkdir -vm 0700 '%{_tmppath}/%{name}-%{release}'
mkdir -vm 0700 '%{_tmppath}/%{name}-%{release}/bin'
test -x "$PWD/dune.exe"
ln -vs "$_"    '%{_tmppath}/%{name}-%{release}/bin/dune'
export    "PATH=%{_tmppath}/%{name}-%{release}/bin:$PATH"
dune_release_pkgs='dune,dune-action-plugin,dune-build-info,dune-glob,dune-private-libs'
%endif
#
%if "%{build_flavor}" == "configurator"
dune_release_pkgs='dune-configurator'
%endif
#
%ocaml_dune_setup
%ocaml_dune_build

%install
export    "PATH=%{_tmppath}/%{name}-%{release}/bin:$PATH"
%ocaml_dune_install
%ocaml_create_file_list
rm -rfv        '%{_tmppath}/%{name}-%{release}'

%files -f %{name}.files
%defattr(-,root,root,-)
%if "%{build_flavor}" == ""
%doc CHANGES.md README.md
%doc doc/*.rst
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/emacs
%endif

%files devel -f %{name}.files.devel
%defattr(-,root,root,-)

%changelog
