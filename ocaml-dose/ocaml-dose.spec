#
# spec file for package ocaml-dose
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name    dose3
%define _version 5.0.1
Name:            ocaml-dose
Version:         3.5.0.1
Release:         0
%{?ocaml_preserve_bytecode}
Summary:         An OCaml dependency toolkit
License:         LGPL-3.0+
Group:           Development/Languages/OCaml
Url:             http://www.mancoosi.org/software/ 
Source:          http://gforge.inria.fr/frs/download.php/file/36063/%{_name}-%{_version}.tar.gz
BuildRequires:   ocaml
BuildRequires:   ocaml-cppo
BuildRequires:   ocaml-findlib
BuildRequires:   ocaml-ocamlbuild
BuildRequires:   ocaml-rpm-macros
BuildRequires:   ocamlfind(ocamlgraph)
BuildRequires:   ocamlfind(cudf)
BuildRequires:   ocamlfind(re)
BuildRoot:       %{_tmppath}/%{name}-%{version}-build

%description
Dose3 is a framework made of several OCaml libraries for managing distribution
packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems (monitoring
package evolutions, correct and complete dependency resolution, repository-wide
uninstallability checks).

%package devel
Summary:        An OCaml dependency toolkit -- Development files
Requires:       %{name} = %{version}

%description devel
This package contains development files for package %{name}.

%prep
%setup -q -n %{_name}-%{_version}
# Fix name of these manpages
mv doc/manpages/{debcoinstall,deb-coinstall}.pod
mv doc/manpages/{strongdeps,strong-deps}.pod

%build
%configure --with-ocamlgraph
make

%install
make DESTDIR=%{buildroot} install

# Edit links that points to buildroot
ln -sf %{_bindir}/distcheck %{buildroot}%{_bindir}/debcheck
ln -sf %{_bindir}/distcheck %{buildroot}%{_bindir}/eclipsecheck
ln -sf %{_bindir}/distcheck %{buildroot}%{_bindir}/rpmcheck

# Install man pages
install -d %{buildroot}%{_mandir}/man{1,5,8}
for section in {1,5,8} ; do
  install -m0644 doc/manpages/*.${section} %{buildroot}%{_mandir}/man${section}
done

%check
make testlib

%files
%defattr(-,root,root)
%doc CHANGES CREDITS README.architecture
%license COPYING Copyright
%{_bindir}/*
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man5/*.5%{ext_man}
%{_mandir}/man8/*.8%{ext_man}
%dir %{_libdir}/ocaml/%{_name}
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/%{_name}/*.cmxs
%endif

%files devel
%defattr(-,root,root)
%license COPYING Copyright
%{_libdir}/ocaml/%{_name}/META
%{_libdir}/ocaml/%{_name}/*.cma
%{_libdir}/ocaml/%{_name}/*.cmi
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/%{_name}/*.a
%{_libdir}/ocaml/%{_name}/*.cmxa
%endif

%changelog
