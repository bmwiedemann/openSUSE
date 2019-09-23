#
# spec file for package ocaml-ptmap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ocaml-ptmap
Version:        2.0.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Maps over integers implemented as Patricia trees
License:        LGPL-2.1-or-later WITH OCaml-linking-exception
Group:          Development/Languages/OCaml

URL:            https://github.com/backtracking/ptmap
Source0:        https://github.com/backtracking/ptmap/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# https://github.com/backtracking/ptmap/pull/9
Patch0:         https://github.com/backtracking/ptmap/commit/97849cd31363ac80306d714915d76dc5a06672cb.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-qtest
BuildRequires:  ocaml-rpm-macros

%description
OCaml implementation of an efficient maps over integers,
from a paper by Chris Okasaki.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ptmap-%{version}
%patch0 -p1


%build
obuild configure
obuild build
obuild build lib-ptmap
make doc


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
obuild install --destdir $OCAMLFIND_DESTDIR


%files
%defattr(-,root,root,-)
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc doc/*
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*/
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/META

%changelog

