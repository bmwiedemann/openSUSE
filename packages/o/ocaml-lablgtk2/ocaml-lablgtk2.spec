#
# spec file for package ocaml-lablgtk2
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


Version:        2.18.5
Release:        0
%{?ocaml_preserve_bytecode}
%global __ocaml_requires_opts -i GtkSourceView_types -i GtkSourceView2_types
Name:           ocaml-lablgtk2
Source0:        lablgtk-%{version}.tar.gz
BuildRequires:  gtk2-devel
BuildRequires:  gtksourceview2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  librsvg-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgl-devel
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRequires:  xorg-x11
BuildRequires:  zlib-devel
Requires:       ocaml
Provides:       lablgtk2 = %{version}
Obsoletes:      lablgtk2 < %{version}
Provides:       ocaml-lablgtk = %{version}
Obsoletes:      ocaml-lablgtk < %{version}
Url:            http://lablgtk.forge.ocamlcore.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        An Objective Caml Interface to gtk2+
License:        LGPL-2.1+
Group:          Development/Languages/OCaml

%description
LablGTK2 uses the rich type system of Objective Caml 3 to provide a
strongly typed, yet very comfortable, object-oriented interface to
GTK2+. Objective Caml threads are supported, including for the top
level, which allows the interactive use of the library.



Authors:
--------
    Jacques Garrigue <garrigue@kurims.kyoto-u.ac.jp>
    Benjamin Monate  <monate@lix.polytechnique.fr>
    Olivier Andrieu  <oandrieu@nerim.net>
    Jun Furuse       <Jun.Furuse@inria.fr>
    Hubert Fauque    <hubert.fauque@wanadoo.fr>
    Koji Kagawa      <kagawa@eng.kagawa-u.ac.jp>

%package devel
Summary:        An Objective Caml interface to gtk2+
Group:          Development/Languages/OCaml
Provides:       lablgtk2-devel = %{version}
Obsoletes:      lablgtk2-devel < %{version}
Provides:       ocaml-lablgtk-devel = %{version}
Obsoletes:      ocaml-lablgtk-devel < %{version}
Provides:       lablgtk2:/usr/lib/ocaml/lablgtk2/glib.cmi
Requires:       %{name} = %{version}
Requires:       gtk2-devel
Requires:       gtksourceview2-devel
Requires:       libgnomecanvas-devel

%description devel
LablGTK2 uses the rich type system of Objective Caml 3 to provide a
strongly typed, yet very comfortable, object-oriented interface to
GTK2+. Objective Caml threads are supported, including for the top
level, which allows for interactive use of the library.



Authors:
--------
    Jacques Garrigue <garrigue@kurims.kyoto-u.ac.jp>
    Benjamin Monate  <monate@lix.polytechnique.fr>
    Olivier Andrieu  <oandrieu@nerim.net>
    Jun Furuse       <Jun.Furuse@inria.fr>
    Hubert Fauque    <hubert.fauque@wanadoo.fr>
    Koji Kagawa      <kagawa@eng.kagawa-u.ac.jp>

%prep
%setup -q -n lablgtk-%{version}
find -name ".cvsignore" -print -delete
# fix README file executable permissions
chmod a-x README

%build
export CFLAGS="$RPM_OPT_FLAGS"
make configure 
%configure --with-gnomecanvas
make world
%if 0%{?ocaml_native_compiler}
make opt
pushd src
make lablgtk.cmxa
make lablrsvg.cmxa
make gtkInit.cmx
popd
%endif

%install
%makeinstall
# Remove ld.conf (part of main OCaml dist).
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/ld.conf
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/lablgtk2
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc CHANGES COPYING README examples
/etc/ld.so.conf.d/*.conf
%{_bindir}/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.so

%files devel
%defattr(-, root, root)
%doc examples
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.o
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmo
%{_libdir}/ocaml/*/*.h
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/propcc
%{_libdir}/ocaml/*/varcc

%changelog
