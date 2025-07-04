#
# spec file for package ocaml-augeas
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ocaml-augeas
Version:        0.7
Release:        0
Summary:        OCaml bindings for Augeas configuration API
License:        LGPL-2.1-or-later
URL:            https://download.libguestfs.org/ocaml-augeas/
Source0:        https://download.libguestfs.org/ocaml-augeas/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.sig
Source2:        ocaml-augeas.rpmlintrc

BuildRequires:  augeas-devel >= 0.1.0
BuildRequires:  chrpath
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros

%description
Augeas is a unified system for editing arbitrary configuration
files. This provides complete OCaml bindings for Augeas.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}

%configure
make all
make doc

%check
make check

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

ocamlfind install augeas META *.mli *.cmx *.cma *.cmxa *.a augeas.cmi *.so

chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

%ocaml_create_file_list

%files -f %name.files
%license COPYING.LIB

%files devel -f %name.files.devel
%doc html

%changelog
