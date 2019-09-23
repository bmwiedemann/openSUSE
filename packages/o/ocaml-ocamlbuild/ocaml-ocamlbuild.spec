#
# spec file for package ocaml-ocamlbuild
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


Name:           ocaml-ocamlbuild
Version:        0.11.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Generic build tool for building OCaml library and programs
License:        LGPL-2.0
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml/ocamlbuild
Source:         %{name}-%{version}.tar.xz
Conflicts:      ocaml < 4.03.0
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRequires:  ocaml-runtime
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OCamlbuild is a generic build tool, that has built-in rules for
building OCaml library and programs.

OCamlbuild was distributed as part of the OCaml distribution for
OCaml versions between 3.10.0 and 4.02.3. Starting from OCaml
4.03, it is now released separately.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ocamlbuild-%{version}

%build
tee %{name}.sh <<'_EOF_'
set -x
exec \
make \
PREFIX=%{_prefix} \
%if 0%{?ocaml_native_compiler}
OCAML_NATIVE_TOOLS=true \
OCAML_NATIVE=true \
%else
OCAML_NATIVE_TOOLS=false \
OCAML_NATIVE=false \
%endif
"$@"
_EOF_
sh %{name}.sh -f configure.make
sh %{name}.sh configure
sh %{name}.sh %{?_smp_mflags}

%install
sh %{name}.sh \
install \
DESTDIR=%{buildroot} %{?_smp_mflags}
find %{buildroot} -ls

%files
%defattr(-,root,root)
%doc Changes  LICENSE
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmo
%{_mandir}/man*/*

%files devel
%defattr(-,root,root,-)
%doc LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.o
%endif
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
