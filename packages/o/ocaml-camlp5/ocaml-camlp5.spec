#
# spec file for package ocaml-camlp5
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


%global __ocaml_requires_opts -i Asttypes -i Parsetree -i Pa_extend
%global __ocaml_provides_opts -i Dynlink -i Dynlinkaux -i Pa_extend
Name:           ocaml-camlp5
Version:        7.07
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Preprocessor-Pretty-Printer for Objective Caml
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
URL:            https://camlp5.github.io/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros >= 4.02.1

%description
Camlp5 is a preprocessor-pretty-printer of OCaml, parsing a source file and printing some result on standard output.

%package devel
Summary:        Development files for ocaml-camlp5
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Camlp5 is a preprocessor-pretty-printer of OCaml, parsing a source file and printing some result on standard output.

This package contains the development files.

%prep
%setup -q

%build
./configure \
	--mandir %{_mandir}
make %{?_smp_mflags} out
make %{?_smp_mflags} world
%if 0%{?ocaml_native_compiler}
make %{?_smp_mflags} world.opt
%endif

%install
%make_install
cp -Lavit %{buildroot}%{_libdir}/ocaml/camlp5 etc/META

%files
%license LICENSE
%doc CHANGES DEVEL MODE README UPGRADING
%{_bindir}/camlp5
%{_bindir}/camlp5o
%{_bindir}/camlp5r
%{_bindir}/camlp5sch
%{_bindir}/mkcamlp5
%{_bindir}/ocpp5
%if 0%{?ocaml_native_compiler}
%{_bindir}/camlp5o.opt
%{_bindir}/camlp5r.opt
%{_bindir}/mkcamlp5.opt
%endif
%{_mandir}/man1/camlp5.1%{ext_man}
%{_mandir}/man1/camlp5o.1%{ext_man}
%{_mandir}/man1/camlp5r.1%{ext_man}
%{_mandir}/man1/camlp5sch.1%{ext_man}
%{_mandir}/man1/mkcamlp5.1%{ext_man}
%{_mandir}/man1/ocpp5.1%{ext_man}
%if 0%{?ocaml_native_compiler}
%{_mandir}/man1/camlp5o.opt.1%{ext_man}
%{_mandir}/man1/camlp5r.opt.1%{ext_man}
%{_mandir}/man1/mkcamlp5.opt.1%{ext_man}
%endif

%files devel
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/camlp5
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/camlp5/*.a
%{_libdir}/ocaml/camlp5/*.cmx
%{_libdir}/ocaml/camlp5/*.cmxa
%{_libdir}/ocaml/camlp5/*.o
%endif
%{_libdir}/ocaml/camlp5/*.cma
%{_libdir}/ocaml/camlp5/*.cmi
%{_libdir}/ocaml/camlp5/*.cmo
%{_libdir}/ocaml/camlp5/*.mli
%{_libdir}/ocaml/camlp5/*.sml
%{_libdir}/ocaml/camlp5/META

%changelog
