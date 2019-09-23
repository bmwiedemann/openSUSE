#
# spec file for package ocaml-camlp4
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


Name:           ocaml-camlp4
Version:        4.05
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Pre-Processor-Pretty-Printer for Objective Caml
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml/camlp4
Source:         camlp4-%{version}-1.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros >= 4.05.0
BuildRequires:  ocaml(ocaml_base_version) = 4.05
Conflicts:      ocaml < 4.05.0
Requires:       ocaml-runtime >= 4.05.0

%description
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml, parsing a
source file and printing some result on standard output.

This package contains the runtime files.


%package devel
Summary:        Pre-Processor-Pretty-Printer for Objective Caml
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       ocaml(ocaml_base_version) = 4.05
Provides:       camlp4 = %{version}
Obsoletes:      camlp4 < %{version}

%description devel
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml, parsing a
source file and printing some result on standard output.

This package contains the development files.

%prep
%setup -q -n camlp4-%{version}-1

%build
./configure
make \
	%{?_smp_mflags} \
	byte
%if 0%{?ocaml_native_compiler}
make \
	%{?_smp_mflags} \
	native
%endif

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc LICENSE README.md
%dir %{_libdir}/ocaml/camlp4
%dir %{_libdir}/ocaml/camlp4/Camlp4Filters
%dir %{_libdir}/ocaml/camlp4/Camlp4Parsers
%dir %{_libdir}/ocaml/camlp4/Camlp4Printers
%dir %{_libdir}/ocaml/camlp4/Camlp4Top
%{_libdir}/ocaml/camlp4/*.cma
%{_libdir}/ocaml/camlp4/*.cmi
%{_libdir}/ocaml/camlp4/*.cmo
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmo
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmo
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmo
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmi
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmo

%files devel
%defattr(-,root,root)
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%if 0%{?ocaml_native_compiler}
%dir %{_libdir}/ocaml/camlp4
%{_libdir}/ocaml/camlp4/*.a
%{_libdir}/ocaml/camlp4/*.cmx
%{_libdir}/ocaml/camlp4/*.cmxa
%{_libdir}/ocaml/camlp4/*.o
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Filters/*.o
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Parsers/*.o
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Printers/*.o
%{_libdir}/ocaml/camlp4/Camlp4Top/*.cmx
%{_libdir}/ocaml/camlp4/Camlp4Top/*.o
%endif

%changelog
