#
# spec file for package opam
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           opam
Version:        2.0.3
Release:        0
Summary:        Source-based package manager for OCaml
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          System/Packages
URL:            https://opam.ocaml.org/
Source:         https://github.com/ocaml/opam/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  curl
BuildRequires:  gcc-c++
BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune
BuildRequires:  ocamlfind
BuildRequires:  ocaml(Ocamlbuild)
BuildRequires:  ocaml(Odoc)
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(cppo)
BuildRequires:  ocamlfind(cudf)
BuildRequires:  ocamlfind(dose3)
BuildRequires:  ocamlfind(extlib)
BuildRequires:  ocamlfind(ocamlgraph)
BuildRequires:  ocamlfind(opam-file-format)
BuildRequires:  ocamlfind(re)

Requires:       %{name}-installer%{?_isa} = %{version}-%{release}

Requires:       bubblewrap
Requires:       mccs

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

%description installer
Handles (un)installation of package files following instructions from
OPAM *.install files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make all man

%install
%make_install LIBINSTALL_DIR=%{buildroot}%{_libdir}/ocaml
# Prevent installation of doc files in wrong directory
rm -r %{buildroot}%{_prefix}/doc

%files
%doc AUTHORS CHANGES CONTRIBUTING.md README.md
%license LICENSE
%{_bindir}/opam
%{_mandir}/man1/*.1%{?ext_man}

%files installer
%license LICENSE
%{_bindir}/opam-installer
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/opam-installer/
%{_libdir}/ocaml/opam-installer/opam
%{_libdir}/ocaml/opam-installer/META
%{_libdir}/ocaml/opam-installer/dune-package

%changelog
