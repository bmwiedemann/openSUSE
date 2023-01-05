#
# spec file for package opam
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


Name:           opam
Version:        2.1.4
Release:        0
Summary:        Source-based package manager for OCaml
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          System/Packages
URL:            https://opam.ocaml.org/
Source:         %name-%version.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(base64)
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(cudf)
BuildRequires:  ocamlfind(dose3)
BuildRequires:  ocamlfind(mccs)
BuildRequires:  ocamlfind(ocamlgraph)
BuildRequires:  ocamlfind(opam-file-format)
BuildRequires:  ocamlfind(re)
BuildRequires:  ocamlfind(unix)

Requires:       %name-installer%{?_isa} = %version-%release

Requires:       bubblewrap

# https://cygwin.com/ml/cygwin/2018-01/msg00079.html
Requires:       bzip2
Requires:       curl
Requires:       diffutils
Requires:       gzip
Requires:       patch
Requires:       tar
Requires:       unzip
Recommends:     gcc
Recommends:     make
Recommends:     m4
Recommends:     rsync
Recommends:     git
Recommends:     mercurial
Suggests:       ocaml

%description
OPAM is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and a
Git-friendly development workflow.

%package installer
Summary:        Standalone tool for opam install files
Group:          System/Packages
Requires:       %name = %version-%release

%description installer
Handles (un)installation of package files following instructions from
OPAM *.install files.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
# wipe bogus FETCH
grep -n FETCH configure.ac
sed -i~ '/FETCH/d;287,+7d' configure.ac
diff -u "$_"~ "$_" && exit 1
export DUNE=$(type -P dune)
export CPPO=$(type -P cppo)
export PATCH=$(type -P false)
export BUNZIP2=$(type -P false)
autoreconf -fi
%configure
dune_release_pkgs='opam-admin,opam-client,opam-core,opam-format,opam-installer,opam-repository,opam-solver,opam-state,opam'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%files -f %name.files
%_bindir/opam
%_bindir/opam-admin.top
%_mandir/man*/*

%files devel -f %name.files.devel

%files installer
%_bindir/opam-installer

%changelog
