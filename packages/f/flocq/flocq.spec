#
# spec file for package flocq
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2020 Peter Trommler <ptrommler@icloud.com>
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


Name:           flocq
Version:        4.2.2
Release:        0
Summary:        Formalization of floating point numbers for Coq
Group:          Productivity/Scientific/Math
License:        LGPL-3.0-or-later
URL:            https://flocq.gitlabpages.inria.fr/
#Git-Clone:     https://gitlab.inria.fr/flocq/flocq.git
Source0:        https://flocq.gitlabpages.inria.fr/releases/%{name}-%{version}.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  gcc-c++
BuildRequires:  ocaml-rpm-macros
%if %{suse_version} >= 1600
BuildRequires:  coq-devel >= 8.15
BuildRequires:  (rocq-stdlib-devel if rocq-devel)
%else
BuildRequires:  coq-devel >= 8.15
%endif
BuildRequires:  ocamlfind(findlib)
# The binary format works only with the Coq version it was built with.
Requires:       coq = %{pkg_version coq}
%if %{pkg_vcmp coq >= 9.0}
Requires:       rocq-stdlib = %{pkg_version rocq-stdlib}
%endif
Suggests:       %{name}-doc = %{version}

%description
Flocq (Floats for Coq) is a floating-point formalization for the Coq
system.  It provides a comprehensive library of theorems on a
multi-radix multi-precision arithmetic.  It also supports efficient
numerical computations inside Coq.

%package devel
Summary:        Development files for Flocq
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       coq-devel = %{pkg_version coq}
%if %{pkg_vcmp coq >= 9.0}
Requires:       rocq-stdlib-devel = %{pkg_version rocq-stdlib-devel}
%endif

%description devel
This package contains development files for Flocq.

%package doc
Summary:        Documentation for Flocq
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Requires:       coq-doc = %{pkg_version coq}
%if %{pkg_vcmp coq >= 9.0}
Requires:       rocq-stdlib-doc = %{pkg_version rocq-stdlib-devel}
%endif
BuildArch:      noarch

%description doc
This package contains the HTML documentation for flocq.

%prep
%setup -q

# Make the documentation point to coq-doc/rocq-stdlib-doc if possible.
grep -- "--coqlib_url https://rocq-prover.org/doc/V@COQVERSION@/corelib" Remakefile.in &&
%if %{pkg_vcmp coq >= 9.0}
sed -i "s|--coqlib_url https://rocq-prover.org/doc/V@COQVERSION@/corelib|--coqlib %{_libdir}/coq --coqlib_url %{_defaultdocdir}/rocq/corelib|" Remakefile.in
%else
%if %{pkg_vcmp coq >= 8.18}
sed -i "s|--coqlib_url https://rocq-prover.org/doc/V@COQVERSION@/corelib|--coqlib %{_libdir}/coq --coqlib_url %{_defaultdocdir}/coq/stdlib|" Remakefile.in
%else
sed -i "s|--coqlib_url https://rocq-prover.org/doc/V@COQVERSION@/corelib|--coqlib %{_libdir}/coq-core --coqlib_url %{_defaultdocdir}/coq/stdlib|" Remakefile.in
%endif
%endif

grep -- "--external https://rocq-prover.org/doc/V@COQVERSION@/stdlib" Remakefile.in &&
%if %{pkg_vcmp coq >= 9.0}
sed -i "s|--external https://rocq-prover.org/doc/V@COQVERSION@/stdlib|--external %{_defaultdocdir}/rocq/stdlib|" Remakefile.in
%else
sed -i "\#--external https://rocq-prover.org/doc/V@COQVERSION@/stdlib#d" Remakefile.in
%endif

%build
# This is not autotools-compatible, so we don't use the macro.
%if %{pkg_vcmp coq >= 9.0}
COQC="%{_bindir}/rocq compile" COQDOC="%{_bindir}/rocq doc" \
%endif
./configure
./remake %{?_smp_mflags} all doc

%install
DESTDIR=%{buildroot} ./remake install

# Build lists of runtime and devel files by ending.
# Compiled theories and shared objects are needed at runtime.
find %{buildroot}%{_libdir}/coq/user-contrib/Flocq -type d | sed "s|%{buildroot}|%%dir |g" >dir.list
find %{buildroot}%{_libdir}/coq/user-contrib/Flocq -name '*.cmxs' \
                -or -name '*.so' \
                -or -name '*.vo' | sed "s|%{buildroot}||g" >runtime.list

# Object files, static libraries and import definitions are only needed for development.
# For now, we also put the standard library Coq sources here, since the runtime
# package contains the HTML documentation for the standard library.
find %{buildroot}%{_libdir}/coq/user-contrib/Flocq -name '*.a' \
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

%files -f dir.list -f runtime.list
%doc README.md NEWS.md
%license AUTHORS COPYING

%files devel -f dir.list -f devel.list

%files doc
%doc html

%changelog
