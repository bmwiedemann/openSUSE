#
# spec file for package ocaml-curses
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-curses
Version:        1.0.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml bindings for ncurses
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            http://savannah.nongnu.org/projects/ocaml-tmk/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  pkg-config

%description
OCaml bindings for ncurses.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       ncurses-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='curses'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
dune_test_tolerate_fail='dune_test_tolerate_fail'
%ocaml_dune_test

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
