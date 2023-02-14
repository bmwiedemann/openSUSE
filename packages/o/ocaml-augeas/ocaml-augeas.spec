#
# spec file for package ocaml-augeas
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


Name:           ocaml-augeas
Version:        0.6
Release:        0
Summary:        OCaml bindings for Augeas configuration API
License:        GPL-2.0-or-later
URL:            http://people.redhat.com/~rjones/augeas/files/
Source0:        http://people.redhat.com/~rjones/augeas/files/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.sig
Source2:        ocaml-augeas.rpmlintrc

Patch1:         caml_named_value-returns-const-value-pointer-in-OCam.patch

BuildRequires:  make
BuildRequires:  ocaml >= 3.09.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  augeas-devel >= 0.1.0
BuildRequires:  chrpath 

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


%files
%doc COPYING.LIB
%{_libdir}/ocaml/augeas
%exclude %{_libdir}/ocaml/augeas/*.a
%exclude %{_libdir}/ocaml/augeas/*.cmxa
%exclude %{_libdir}/ocaml/augeas/*.cmx
%exclude %{_libdir}/ocaml/augeas/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc html
%{_libdir}/ocaml/augeas/*.a
%{_libdir}/ocaml/augeas/*.cmxa
%{_libdir}/ocaml/augeas/*.cmx
%{_libdir}/ocaml/augeas/*.mli


%changelog
