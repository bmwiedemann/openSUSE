#
# spec file for package ocaml-dune
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

%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == ""
%define nsuffix %nil
%else
%define nsuffix -%build_flavor
%endif

%define     pkg ocaml-dune
%global  _buildshell /bin/bash
Name:           %pkg%nsuffix
Version:        3.0.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        A composable build system for OCaml
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/dune
Source0:        %pkg-%version.tar.xz
Requires:       ocamlfind(compiler-libs)
BuildRequires:  ocaml-rpm-macros >= 20220222
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
%if "%build_flavor" == ""
BuildRequires:  ocaml-dune-bootstrap = %version
BuildRequires:  ocamlfind(csexp)
BuildRequires:  ocamlfind(pp)
BuildRequires:  ocamlfind(result)
Provides:       ocaml-dune-configurator == %version-%release
Obsoletes:      ocaml-dune-configurator <  %version-%release
%description
A composable build system for OCaml
%endif
%if "%build_flavor" == "bootstrap"
%description
This package provides a minimal dune binary in %ocaml_dune_bootstrap_directory
to build a few number of packages to bootstrap the full dune package.
%endif

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Provides:       ocaml-dune-configurator-devel == %version-%release
Obsoletes:      ocaml-dune-configurator-devel <  %version-%release
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q -n %pkg-%version

%build
mv -vb src/dune_rules/setup.defaults.ml src/dune_rules/setup.ml
ocaml configure.ml \
	'--etcdir=%_sysconfdir' \
	'--libdir=%ocaml_standard_library' \
	'--mandir=%_mandir' \
	%nil
#
%if "%build_flavor" == "bootstrap"
jobs="-j `/usr/bin/getconf _NPROCESSORS_ONLN`"
ocaml bootstrap.ml --verbose ${jobs}
./dune.exe build \
	dune.install \
	--release \
	--profile dune-bootstrap \
	--verbose \
	${jobs} \
	%nil
# leaving early
exit 0
%endif
#
%if "%build_flavor" == ""
pkgs=(
dune
dune-action-plugin
dune-build-info
dune-configurator
dune-glob
dune-private-libs
dune-rpc
dune-site
dyn
fiber
ordering
stdune
xdg
)
dune_release_pkgs="${pkgs[*]}"
dune_release_pkgs="${dune_release_pkgs// /,}"
#
export PATH="%ocaml_dune_bootstrap_directory:$PATH"
%ocaml_dune_setup
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == "bootstrap"
mkdir -vp %buildroot%ocaml_dune_bootstrap_directory
cp -avL dune.exe %buildroot%ocaml_dune_bootstrap_directory/dune
tee %name.files <<'_EOF_'
%ocaml_dune_bootstrap_directory
%%doc CHANGES.md
_EOF_
echo '%dir %ocaml_dune_bootstrap_directory' > %name.files.devel
%endif
#
%if "%build_flavor" == ""
export PATH="%ocaml_dune_bootstrap_directory:$PATH"
%ocaml_dune_install
%ocaml_create_file_list
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

%files devel -f %name.files.devel
%defattr(-,root,root,-)

%changelog
