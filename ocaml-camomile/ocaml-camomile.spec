#
# spec file for package ocaml-camomile
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


Name:           ocaml-camomile
Version:        0.8.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Unicode library for OCaml
# Several files are MIT and UCD licensed, but the overall work is LGPLv2+
# and the LGPL/GPL supercedes compatible licenses.
# https://www.redhat.com/archives/fedora-legal-list/2008-March/msg00005.html
License:        LGPL-2.0+
Group:          Development/Languages/OCaml
Url:            https://github.com/yoriyuki/Camomile/wiki
Source0:        camomile-%{version}.tar.bz2
# Use ocamlopt -g option to enable debuginfo.
Patch1:         camomile-0.8.3-enable-debug.patch
Patch2:         ocaml-camomile.bytecode.patch
BuildRequires:  fdupes
BuildRequires:  ocaml >= 3.12.1-12
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        data
Summary:        Data files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.

%prep
%setup -q -n camomile-%{version}

%patch1 -p1
%patch2 -p1

%build
# Parallel builds don't work.
./configure --prefix=%{_prefix} --datadir=%{_datadir} --libdir=%{_libdir}
make do_byte
%if 0%{?ocaml_native_compiler}
make do_opt
%endif
make %{?_smp_mflags} dochtml
make %{?_smp_mflags} man

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs $OCAMLFIND_DESTDIR/camomile
mkdir -p %{buildroot}%{_bindir}
make install prefix=%{buildroot}%{_prefix} DATADIR=%{buildroot}%{_datadir}
%if 0%{?ocaml_native_compiler}
cp tools/camomilecharmap.opt %{buildroot}%{_bindir}/camomilecharmap
cp tools/camomilelocaledef.opt %{buildroot}%{_bindir}/camomilelocaledef
%endif
%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_bindir}/camomilecharmap
%{_bindir}/camomilelocaledef
%endif

%files devel
%defattr(-,root,root,-)
%doc README dochtml/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%files data
%defattr(-,root,root,-)
%doc README
%{_datadir}/camomile/

%changelog
