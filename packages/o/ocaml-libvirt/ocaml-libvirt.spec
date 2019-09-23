#
# spec file for package ocaml-libvirt
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


Name:           ocaml-libvirt
Version:        0.6.1.4.20160205.8853f5a
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml binding for libvirt
License:        LGPL-2.0+
Group:          Development/Languages/OCaml
Url:            http://libvirt.org/ocaml/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  perl
BuildRequires:  pkgconfig(libvirt)
Requires:       libvirt-client >= 0.9.10-3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OCaml binding for libvirt.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
sed '
s|@PACKAGE_NAME@|libvirt|
s|@PACKAGE_VERSION@|%{version}|
' libvirt/libvirt_version.ml.in > libvirt/libvirt_version.ml
#
tee config.h <<'_EOF_'
_EOF_
#
libvirt_version="`pkg-config --modversion libvirt`"
libvirt_cflags="`pkg-config --cflags libvirt`"
libvirt_libs="`pkg-config --libs libvirt`"
# contains CFLAGS ...
case "${libvirt_version}" in
  1.1.*) libvirt_libs="-lvirt" ;;
  1.2.5) libvirt_libs="-lvirt" ;;
esac
#
pushd libvirt
mv -v libvirt_c.c libvirt_c.c.txt
perl -w generator.pl
diff -u libvirt_c.c.txt libvirt_c.c || :
popd
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        libvirt
Version:     0
Synopsis:    binding for libvirt
Authors:     Richard W.M. Jones
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library mllibvirt
 Path: libvirt
 Install: true
 Modules: Libvirt, Libvirt_version
 FindlibName: libvirt
 BuildDepends: unix
 CSources: libvirt_c.c
 CCOpt: %{optflags} -I$PWD -I$PWD/libvirt -Werror -D_GNU_SOURCE ${libvirt_cflags}
 CCLib: ${libvirt_libs}

Document libvirt
 Title:                API reference for libvirt
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: libvirt

Executable "%{name}-domain_events"
 Install: true
 Path: examples
 MainIs: domain_events.ml
 CompiledObject: best
 BuildDepends: libvirt

Executable "%{name}-get_cpu_stats"
 Install: true
 Path: examples
 MainIs: get_cpu_stats.ml
 CompiledObject: best
 BuildDepends: libvirt

Executable "%{name}-list_domains"
 Install: true
 Path: examples
 MainIs: list_domains.ml
 CompiledObject: best
 BuildDepends: libvirt

Executable "%{name}-node_info"
 Install: true
 Path: examples
 MainIs: node_info.ml
 CompiledObject: best
 BuildDepends: libvirt
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/libvirt
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README
/etc/ld.so.conf.d/*.conf
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.so

%files devel
%defattr(-,root,root,-)
%doc COPYING.LIB README
%{oasis_docdir_html}
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
