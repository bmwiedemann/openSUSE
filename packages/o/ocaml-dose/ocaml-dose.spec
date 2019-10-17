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


Name:            ocaml-dose
Version:         5.0.1
Release:         0
%{?ocaml_preserve_bytecode}
Summary:         An OCaml dependency toolkit
License:         LGPL-3.0+
Group:           Development/Languages/OCaml
Url:             https://github.com/IRILL/dose3
Source0:         %{name}-%{version}.tar.xz
Patch0:          %{name}.patch
BuildRequires:   ocaml
BuildRequires:   ocaml-cppo
BuildRequires:   ocaml-findlib
BuildRequires:   ocaml-ocamlbuild
BuildRequires:   ocaml-rpm-macros >= 20191009
BuildRequires:   ocamlfind(ocamlgraph)
BuildRequires:   ocamlfind(cudf)
BuildRequires:   ocamlfind(re)

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
%autosetup -p1

%build
# Fix name of these manpages
mv doc/manpages/{debcoinstall,deb-coinstall}.pod
mv doc/manpages/{strongdeps,strong-deps}.pod

%configure
make

%install
%make_install

# Edit links that points to buildroot
ln -sf distcheck %{buildroot}%{_bindir}/debcheck
ln -sf distcheck %{buildroot}%{_bindir}/eclipsecheck
ln -sf distcheck %{buildroot}%{_bindir}/rpmcheck

# Install man pages
install -d %{buildroot}%{_mandir}/man{1,5,8}
for section in {1,5,8} ; do
  install -m0644 doc/manpages/*.${section} %{buildroot}%{_mandir}/man${section}
done

%ocaml_create_file_list

%check
make testlib

%files -f %{name}.files
%doc CHANGES CREDITS README.architecture
%{_bindir}/*
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man5/*.5%{ext_man}
%{_mandir}/man8/*.8%{ext_man}

%files devel -f %{name}.files.devel

%changelog
