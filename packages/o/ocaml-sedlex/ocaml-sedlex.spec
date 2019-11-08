#
# spec file for package ocaml-sedlex
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


Name:           ocaml-sedlex
Version:        2.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Unicode-friendly lexer generator
License:        MIT
Group:          Development/Languages/OCaml

URL:            https://github.com/alainfrisch/sedlex
Source0:        https://github.com/alainfrisch/sedlex/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Use unicode data files from unicode-ucd
Patch0:         unicode-data.diff

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-gen-devel
BuildRequires:  ocaml-migrate-parsetree-devel
BuildRequires:  ocaml-ppx_tools_versioned-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-rpm-macros >= 20190930
BuildRequires:  unicode-ucd

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n sedlex-%{version}
%patch0 -p1

%build
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md CHANGES
%license LICENSE

%files devel -f %{name}.files.devel

%changelog
