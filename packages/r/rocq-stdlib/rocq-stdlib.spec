#
# spec file for package rocq-stdlib
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global rocq_minver 9.0.0

Name:           rocq-stdlib
Version:        9.1.0
Release:        0
Summary:        Standard library for the Rocq prover
Group:          Productivity/Scientific/Math
License:        LGPL-2.1-only
URL:            https://rocq-prover.org/
Source:         https://github.com/rocq-prover/stdlib/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source50:       rocq-refman-stdlib-%{version}.tar.xz
Source51:       rocq-stdlib-doc-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  ocaml-rpm-macros
BuildRequires:  rocq >= %{rocq_minver}
BuildRequires:  rocq-devel >= %{rocq_minver}
# The binary format works only with the Rocq version it was built with.
Requires:       rocq = %{pkg_version rocq}
Provides:       coq:%{_libdir}/coq/theories/Logic/Classical.vo
Suggests:       %{name}-doc = %{version}

%description
The Rocq standard library consists of fundamental logic, number types like
natural numbers, integers, and floating point numbers, as well as containers
like lists, sets and relations.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Provides:       coq-devel:%{_libdir}/coq/theories/Logic/Classical.v

%description devel
This package contains development files for the Rocq standard library.

%package doc
Summary:        Documentation for the Rocq standard library
Group:          Documentation/HTML
License:        OPUBL-1.0
Requires:       %{name} = %{version}
Provides:       coq-doc:%{_docdir}/coq/stdlib/index.html
BuildArch:      noarch

%description doc
HTML reference manual for the Rocq standard library.

%prep
%setup -q -a 50 -a 51 -n stdlib-%{version}

%build
%{make_build} ROCQMAKEOPTIONS=%{?_smp_mflags}

%install
%{make_install}

# Remove unneeded empty *.vos files.
find %{buildroot}%{_libdir}/coq -empty -name '*.vos' -delete

# Build lists of runtime and devel files by ending.
# Compiled theories and shared objects are needed at runtime.
find %{buildroot}%{_libdir} -type d | sed "s|%{buildroot}|%%dir |g" >dir.list
sed -i '1d; /rocq-runtime\/tools/d' dir.list
find %{buildroot}%{_libdir} -name '*.cmxs' \
                -or -name '*.so' \
                -or -name '*.vo' | sed "s|%{buildroot}||g" >runtime.list

# Object files, static libraries and import definitions are only needed for development.
# For now, we also put the standard library Coq sources here, since the runtime
# package contains the HTML documentation for the standard library.
find %{buildroot}%{_libdir} -name '*.a' \
                -or -name '*.cma' \
                -or -name '*.cmi' \
                -or -name '*.cmt' \
                -or -name '*.cmti' \
                -or -name '*.cmx' \
                -or -name '*.cmxa' \
                -or -name '*.glob' \
                -or -name '*.ml' \
                -or -name '*.mli' \
                -or -name '*.o' \
                -or -name '*.v' | sed "s|%{buildroot}||g" >devel.list

# Until we can build it, we fetch the documentation from the official website:
# git clone --filter=tree:0 --sparse https://github.com/rocq-prover/doc.git
# pushd doc
# git sparse-checkout add V%{version}
# cd V%{version}
# tar --sort=name --owner=0 --group=0 --mtime="@${SOURCE_DATE_EPOCH}" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf ../../rocq-refman-stdlib-%{version}.tar.xz refman-stdlib
# tar --sort=name --owner=0 --group=0 --mtime="@${SOURCE_DATE_EPOCH}" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf ../../rocq-stdlib-doc-%{version}.tar.xz stdlib
# popd

# Slim down documentation pages, add some margin directly.
find stdlib/ -name '*.html' -exec sed -i '
s#https://rocq-prover\.org/css/stdlib\.css#%{_libdir}/rocq-runtime/tools/coqdoc/coqdoc.css#
/<meta [^h]/d
/<link .* href="https:\/\/rocq-prover\.org.*"/d
/<script defer="".* src=".*"><\/script>/d
/<style>/,/<\/style>/d
/<body/i<body style="margin:1em;"><!--
/<body/,/END STDLIB HEADER/d
/START STDLIB FOOTER/,/<\/body>/d
/<\/html>/i-->\n</body>
' {} +
mkdir -p %{buildroot}%{_docdir}/rocq
cp -r refman-stdlib stdlib %{buildroot}%{_docdir}/rocq
rm -r %{buildroot}%{_docdir}/rocq/refman-stdlib/{.buildinfo,.doctrees,_sources}

%fdupes %{buildroot}%{_docdir}/rocq

%files -f dir.list -f runtime.list
%license LICENSE

%files devel -f dir.list -f devel.list

%files doc
%dir %{_docdir}/rocq
%{_docdir}/rocq/refman-stdlib
%{_docdir}/rocq/stdlib

%changelog
