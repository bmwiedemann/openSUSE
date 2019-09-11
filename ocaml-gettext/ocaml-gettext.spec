#
# spec file for package ocaml-gettext
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


%global __ocaml_requires_opts -i Asttypes -i Parsetree
%global __ocaml_provides_opts -i Pr_gettext

Name:           ocaml-gettext
Version:        0.3.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml library for i18n
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/gildor478/ocaml-gettext
Source0:        http://forge.ocamlcore.org/frs/download.php/1433/ocaml-gettext-%{version}.tar.gz
Patch0:         ocaml-gettext-unix.patch
Patch1:         ocaml-gettext-0.3.5-use-ocamlopt-g.patch
BuildRequires:  autoconf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-camomile-data
BuildRequires:  ocaml-camomile-devel >= 0.8.1
BuildRequires:  ocaml-fileutils-devel >= 0.4.4-4
BuildRequires:  ocaml-findlib-devel >= 1.3.3-3
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# ocaml-gettext program needs camomile data files
Requires:       ocaml-camomile-data

%description
Ocaml-gettext provides support for internationalization of Ocaml
programs.

Constraints :

* provides a pure Ocaml implementation,
* the API should be as close as possible to GNU gettext,
* provides a way to automatically extract translatable
  strings from Ocaml source code.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        stub
Summary:        Parts of %{name} which depend on Camomile
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    stub
The %{name}-stub package contains the parts of %{name} which
depend on Camomile.

%package        stub-devel
Summary:        Development files for %{name}-stub
Group:          Development/Languages/OCaml
Requires:       %{name}-stub = %{version}

%description    stub-devel
The %{name}-stub-devel package contains libraries and
signature files for developing applications that use
%{name}-stub.

%package        camomile
Summary:        Parts of %{name} which depend on Camomile
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    camomile
The %{name}-camomile package contains the parts of %{name} which
depend on Camomile.

%package        camomile-devel
Summary:        Development files for %{name}-camomile
Group:          Development/Languages/OCaml
Requires:       %{name}-camomile-devel = %{version}

%description    camomile-devel
The %{name}-camomile-devel package contains libraries and
signature files for developing applications that use
%{name}-camomile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%define _stylesheet_path "%{_datadir}/xml/docbook/stylesheet/nwalsh/current"

%build
# Parallel builds don't work.
unset MAKEFLAGS
CFLAGS="%{optflags}" \
./configure \
  --libdir=%{_libdir} \
  --enable-test \
  --with-docbook-stylesheet=%{_stylesheet_path}
make all

%check
export LD_LIBRARY_PATH=$PWD/_build/lib/gettext-stub
pushd test
../_build/bin/test
popd

%install
# make install in the package is screwed up completely.  Install
# by hand instead.
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p %{buildroot}%{_bindir}

# Remove *.o files - these shouldn't be distributed.
find _build -name '*.o' -exec rm {} \;

ocamlfind install gettext _build/lib/gettext/*
ocamlfind install gettext-stub _build/lib/gettext-stub/*
ocamlfind install gettext-camomile _build/lib/gettext-camomile/*
install -m 0755 _build/bin/ocaml-gettext %{buildroot}%{_bindir}/
install -m 0755 _build/bin/ocaml-xgettext %{buildroot}%{_bindir}/
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}-stub.conf <<_EOF_
%{_libdir}/ocaml/stublibs
_EOF_
#

%post   -n %{name}-stub -p /sbin/ldconfig

%postun -n %{name}-stub -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/ocaml-gettext
%{_bindir}/ocaml-xgettext
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext

%files devel
%defattr(-,root,root,-)
%doc README CHANGELOG TODO
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/gettext/*.a
%{_libdir}/ocaml/gettext/*.cmx
%{_libdir}/ocaml/gettext/*.cmxa
%endif
%{_libdir}/ocaml/gettext/*.cma
%{_libdir}/ocaml/gettext/*.cmi
%{_libdir}/ocaml/gettext/*.cmo
%{_libdir}/ocaml/gettext/*.ml
%{_libdir}/ocaml/gettext/*.mli
%{_libdir}/ocaml/gettext/META

%files stub
%defattr(-,root,root,-)
%doc COPYING
/etc/ld.so.conf.d/*.conf
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext-stub
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files stub-devel
%defattr(-,root,root,-)
%doc README
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext-stub
%{_libdir}/ocaml/gettext-stub/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/gettext-stub/*.cmx
%{_libdir}/ocaml/gettext-stub/*.cmxa
%endif
%{_libdir}/ocaml/gettext-stub/*.cma
%{_libdir}/ocaml/gettext-stub/*.cmi
%{_libdir}/ocaml/gettext-stub/*.ml
%{_libdir}/ocaml/gettext-stub/META

%files camomile
%defattr(-,root,root,-)
%doc COPYING
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext-camomile

%files camomile-devel
%defattr(-,root,root,-)
%doc README
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/gettext-camomile
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/gettext-camomile/*.a
%{_libdir}/ocaml/gettext-camomile/*.cmx
%{_libdir}/ocaml/gettext-camomile/*.cmxa
%endif
%{_libdir}/ocaml/gettext-camomile/*.cma
%{_libdir}/ocaml/gettext-camomile/*.cmi
%{_libdir}/ocaml/gettext-camomile/*.mli
%{_libdir}/ocaml/gettext-camomile/META

%changelog
