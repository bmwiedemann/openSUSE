#
# spec file for package ocaml-dune
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ocaml-dune
Version:        2.4.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        A composable build system for OCaml
License:        MIT
Group:          Development/Languages/OCaml
Url:            https://opam.ocaml.org/packages/dune
Source:         %{name}-%{version}.tar.xz
Requires:       ocamlfind(compiler-libs)
BuildRequires:  ocaml(ocaml_base_version) >= 4.07
BuildRequires:  ocamlfind(compiler-libs)
BuildRequires:  ocaml-rpm-macros >= 20200220

%description
A composable build system for OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
ocaml configure.ml '--libdir=%{ocaml_standard_library}' '--mandir=%{_mandir}'
ocaml bootstrap.ml
rm -rfv        '%{_tmppath}/%{name}-%{release}'
mkdir -vm 0700 '%{_tmppath}/%{name}-%{release}'
mkdir -vm 0700 '%{_tmppath}/%{name}-%{release}/bin'
test -x "$PWD/dune.exe"
ln -vs "$_"    '%{_tmppath}/%{name}-%{release}/bin/dune'
export    "PATH=%{_tmppath}/%{name}-%{release}/bin:$PATH"
dune_release_pkgs='dune,dune-action-plugin,dune-build-info,dune-configurator,dune-glob,dune-private-libs'
%ocaml_dune_setup
%ocaml_dune_build

%install
export    "PATH=%{_tmppath}/%{name}-%{release}/bin:$PATH"
%ocaml_dune_install
%ocaml_create_file_list
rm -rfv        '%{_tmppath}/%{name}-%{release}'

%files -f %{name}.files
%doc CHANGES.md README.md
%doc doc/*.rst
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/emacs

%files devel -f %{name}.files.devel

%changelog
