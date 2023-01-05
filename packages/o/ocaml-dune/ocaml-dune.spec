#
# spec file for package ocaml-dune
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

%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == ""
%define nsuffix %nil
%else
%define nsuffix -%build_flavor
%endif

%define     pkg ocaml-dune
%global  _buildshell /bin/bash
Name:           %pkg%nsuffix
Version:        3.5.0
Release:        0
%{?ocaml_preserve_bytecode}
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/dune
Source0:        %pkg-%version.tar.xz
Requires:       ocamlfind(compiler-libs)
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
%if "%build_flavor" == ""
Provides:       %name-bootstrap = %version-%release
Provides:       %name-bootstrap-devel = %version-%release
Obsoletes:      %name-bootstrap < %version-%release
Obsoletes:      %name-bootstrap-devel < %version-%release
Summary:        A composable build system for OCaml
%description
This package provides the dune binary and the documentation.
%endif
%if "%build_flavor" == "devel"
Summary:        Various libraries
Group:          Development/Languages/OCaml
BuildRequires:  ocaml-dune = %version
BuildRequires:  ocamlfind(csexp)
BuildRequires:  ocamlfind(pp)
BuildRequires:  ocamlfind(result)
Provides:       ocaml-dune-configurator == %version-%release
Obsoletes:      ocaml-dune-configurator <  %version-%release
Provides:       ocaml-dune-configurator-devel == %version-%release
Obsoletes:      ocaml-dune-configurator-devel <  %version-%release

%description
This package provides various libraries:
chrome-trace
dune-action-plugin
dune-build-info
dune-configurator
dune-glob
dune-private-libs
dune-rpc
dune-site
dyn
fiber
ocamlc-loc
ordering
stdune
xdg
%endif

%prep
%setup -q -n %pkg-%version

%build
mv -vb src/dune_rules/setup.defaults.ml src/dune_rules/setup.ml
ocaml configure.ml \
	'--bindir=%_bindir' \
	'--datadir=%_datadir' \
	'--etcdir=%_sysconfdir' \
	'--libdir=%ocaml_standard_library' \
	'--libexecdir=%_libexecdir' \
	'--mandir=%_mandir' \
	'--sbindir=%_sbindir' \
	%nil
#
%if "%build_flavor" == ""
dune_release_pkgs='dune'
%ocaml_dune_setup
jobs="-j `/usr/bin/getconf _NPROCESSORS_ONLN`"
ocaml bootstrap.ml --verbose ${jobs}
./dune.exe build \
	dune.install \
	--release \
	--profile dune-bootstrap \
	--verbose \
	${jobs} \
	%nil
mkdir .bin
ln -s ../dune.exe .bin/dune
%endif
#
%if "%build_flavor" == "devel"
pkgs=(
chrome-trace
dune-action-plugin
dune-build-info
dune-configurator
dune-glob
dune-private-libs
dune-rpc
dune-site
dyn
fiber
ocamlc-loc
ordering
stdune
xdg
)
dune_release_pkgs="${pkgs[*]}"
dune_release_pkgs="${dune_release_pkgs// /,}"
#
%ocaml_dune_setup
%ocaml_dune_build
%endif

%install
# use the just built dune
PATH="$PWD/.bin:$PATH"
%ocaml_dune_install
%if "%build_flavor" == "devel"
# the META file removed below belongs to this package, to provide dune.configurator
mkdir -vp %buildroot%ocaml_standard_library/dune
tee %buildroot%ocaml_standard_library/dune/META <<_EOM_
package "configurator" (
  directory = "configurator"
  version = "%version"
  requires = "dune-configurator"
)
_EOM_
%endif
%if "%build_flavor" == ""
# the installed META file provides and requires 'dune-configurator'
rm -rfv %buildroot%ocaml_standard_library
%endif
#
%ocaml_create_file_list
#
%if "%build_flavor" == "devel"
# package everything, including the cmxs files
tee -a %name.files < %name.files.devel
%endif

%files -f %name.files
%defattr(-,root,root,-)
%if "%build_flavor" == ""
%doc CHANGES.md README.md
%doc doc/*.rst
%_bindir/*
%_mandir/*/*
%_datadir/emacs
%endif


%changelog
