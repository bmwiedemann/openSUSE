#
# spec file for package ocaml-camlp-streams
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


Name:           ocaml-camlp-streams
Version:        5.0.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stream and Genlex libraries for use with Camlp5
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/camlp-streams
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20230101

%description
The camlp-streams package provides two library modules:

Stream: imperative streams, with in-place update and memoization of the latest element produced.
Genlex: a small parameterized lexical analyzer producing streams of tokens from streams of characters.

The two modules are designed for use with Camlp5:

The stream patterns and stream expressions of Camlp5 consume and produce data of type 'a Stream.t.
The Genlex tokenizer can be used as a simple lexical analyzer for Camlp5-generated parsers.

The Stream module can also be used by hand-written recursive-descent parsers, but is not very convenient for this purpose.

The Stream and Genlex modules have been part of the OCaml standard library for a long time, and have been distributed as part of the core OCaml system. They will be removed from the OCaml standard library at some future point, but will be maintained and distributed separately in this camlp-streams package.


%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.


%prep
%setup -q

%build
dune_release_pkgs='camlp-streams'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %name.files
%defattr(-,root,root,-)

%files devel -f %name.files.devel
%defattr(-,root,root,-)

%changelog
