#
# spec file for package ocaml-pcre
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011 Andrew Psaltis <ampsaltis at gmail.com>
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


Name:           ocaml-pcre
Version:        7.5.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Perl compatibility regular expressions (PCRE) for OCaml
License:        LGPL-2.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/pcre
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20220222
BuildRequires:  pkg-config
BuildRequires:  ocaml(ocaml_base_version) >= 4.12
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  pkgconfig(libpcre)

%description
Perl compatibile regular expressions (PCRE) for OCaml.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
Requires:       pcre-devel

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='pcre'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel
%doc README.md

%changelog
