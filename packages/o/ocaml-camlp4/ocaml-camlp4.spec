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
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocaml(ocaml_base_version) = 4.05
Conflicts:      ocaml < 4.05.0
Requires:       ocaml-runtime = 4.05.0

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
%autosetup -p1

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
%make_install
d="%{buildroot}$(ocamlc -where)/camlp4"
tee "${d}/META" <<_META_
# Specifications for the "camlp4" preprocessor:
requires = ""
version = "%{name} %{version}"
description = "Base for Camlp4 syntax extensions"
directory = "+camlp4"

# For the toploop:
requires(byte,toploop) = "dynlink"
archive(byte,toploop,camlp4o) = "camlp4o.cma"
archive(byte,toploop,camlp4r) = "camlp4r.cma"

# For the preprocessor itself:
archive(syntax,preprocessor,camlp4o) = "-parser o -parser op -printer p"
archive(syntax,preprocessor,camlp4r) = "-parser r -parser rp -printer p"
preprocessor = "camlp4"

package "lib" (
  requires = "camlp4 dynlink"
  version = "%{name} %{version}"
  description = "Camlp4 library"
  archive(byte) = "camlp4lib.cma"
  archive(byte,toploop) = ""  # already contained in camlp4*.cma
  archive(native) = "camlp4lib.cmxa"
)

package "gramlib" (
  requires = "camlp4.lib"
  version = "%{name} %{version}"
  description = "Compatibilty name for camlp4.lib"
)

# dont use camlp4.lib and camlp4.fulllib together'
package "fulllib" (
  requires = "camlp4 dynlink"
  version = "%{name} %{version}"
  description = "Camlp4 library"
  error(pkg_camlp4.lib) = "camlp4.lib and camlp4.fulllib are incompatible"
  archive(byte) = "camlp4fulllib.cma"
  archive(byte,toploop) = ""  # already contained in camlp4*.cma
  archive(native) = "camlp4fulllib.cmxa"
)

package "quotations" (
  version = "%{name} %{version}"
  description = "Syntax extension: Quotations to create AST nodes"
  requires = "camlp4.quotations.r"  # backward compat
  archive(syntax,preprocessor) = "-ignore foo"
  package "o" (
    requires = "camlp4"
    version = "%{name} %{version}"
    description = "Syntax extension: Quotations to create AST nodes (original syntax)"
    archive(syntax,preprocessor) = "-parser Camlp4QuotationCommon -parser Camlp4OCamlOriginalQuotationExpander"
    archive(syntax,toploop) = "Camlp4Parsers/Camlp4QuotationCommon.cmo Camlp4Parsers/Camlp4OCamlOriginalQuotationExpander.cmo"
  )
  package "r" (
    requires = "camlp4"
    version = "%{name} %{version}"
    description = "Syntax extension: Quotations to create AST nodes (revised syntax)"
    archive(syntax,preprocessor) = "-parser Camlp4QuotationCommon -parser Camlp4OCamlRevisedQuotationExpander"
    archive(syntax,toploop) = "Camlp4Parsers/Camlp4QuotationCommon.cmo Camlp4Parsers/Camlp4OCamlRevisedQuotationExpander.cmo"
  )
)

package "extend" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax extension: EXTEND the camlp4 grammar"
  archive(syntax,preprocessor) = "-parser Camlp4GrammarParser"
  archive(syntax,toploop) = "Camlp4Parsers/Camlp4GrammarParser.cmo"
)

package "listcomprehension" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax extension for list comprehensions"
  archive(syntax,preprocessor) = "-parser Camlp4ListComprehension"
  archive(syntax,toploop) = "Camlp4Parsers/Camlp4ListComprehension.cmo"
)

package "macro" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax extension: Conditional compilation"
  archive(syntax,preprocessor) = "-parser Camlp4MacroParser"
  archive(syntax,toploop) = "Camlp4Parsers/Camlp4MacroParser.cmo"
)

package "mapgenerator" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Traverse data structure (map style)"
  archive(syntax,preprocessor) = "-filter Camlp4MapGenerator"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4MapGenerator.cmo"
)

package "foldgenerator" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Traverse data structure (fold style)"
  archive(syntax,preprocessor) = "-filter Camlp4FoldGenerator"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4FoldGenerator.cmo"
)

package "metagenerator" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Generate AST generator for data structure"
  archive(syntax,preprocessor) = "-filter Camlp4MetaGenerator"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4MetaGenerator.cmo"
)

package "locationstripper" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Remove location info from AST"
  archive(syntax,preprocessor) = "-filter Camlp4LocationStripper"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4LocationStripper.cmo"
)

package "tracer" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Trace execution"
  archive(syntax,preprocessor) = "-filter Camlp4Tracer"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4Tracer.cmo"
)

package "exceptiontracer" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Trace exception execution"
  archive(syntax,preprocessor) = "-filter Camlp4ExceptionTracer"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4ExceptionTracer.cmo"
)

package "profiler" (
  requires = "camlp4"
  version = "%{name} %{version}"
  description = "Syntax filter: Count events during execution"
  archive(syntax,preprocessor) = "-filter Camlp4Profiler"
  archive(syntax,toploop) = "Camlp4Filters/Camlp4Profiler.cmo"
  archive(byte) = "camlp4prof.cmo"
  archive(native) = "camlp4prof.cmx"
)
_META_

%files
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
%{_bindir}/camlp4*
%{_bindir}/mkcamlp4
%dir %{_libdir}/ocaml/camlp4
%{_libdir}/ocaml/camlp4/META
%if 0%{?ocaml_native_compiler}
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
