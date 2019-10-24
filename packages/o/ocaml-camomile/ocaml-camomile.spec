#
# spec file for package ocaml-camomile
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ocaml-camomile
Version:        1.0.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Unicode library for OCaml
# Several files are MIT and UCD licensed, but the overall work is LGPLv2+
# and the LGPL/GPL supercedes compatible licenses.
# https://www.redhat.com/archives/fedora-legal-list/2008-March/msg00005.html
License:        LGPL-2.0+
Group:          Development/Languages/OCaml
Url:            https://github.com/yoriyuki/Camomile/wiki
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(str)

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        data
Summary:        Data files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test || : make check failed

%files -f %{name}.files

%files devel -f %{name}.files.devel

%files data
%{_datadir}/camomile/

%changelog
