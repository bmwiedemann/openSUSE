#
# spec file for package ocaml-pcre
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Andrew Psaltis <ampsaltis at gmail.com>
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


Name:           ocaml-pcre
Version:        7.2.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Perl compatibility regular expressions (PCRE) for OCaml
License:        LGPL-2.0
Group:          Development/Languages/OCaml

Url:            http://mmottl.github.io/pcre-ocaml/
# https://github.com/mmottl/pcre-ocaml/releases/download/v%{version}/pcre-ocaml-%{version}.tar.gz
Source0:        pcre-ocaml-%{version}.tar.xz
Patch0:         ocaml-pcre-warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gawk
BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  pkg-config
BuildRequires:  ocamlfind(bytes)
BuildRequires:  pkgconfig(libpcre)

%description
Perl compatibile regular expressions (PCRE) for OCaml.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       pcre-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pcre-ocaml-%{version}
%patch0 -p1

%build
sed -i~ "
s@\(.*\)\(CCOpt:\)\(.*\)\$@\1\2 %{optflags} -fPIC `pkg-config --cflags libpcre`@
s@\(.*\)\(CCLib:\)\(.*\)\$@\1\2 `pkg-config --libs libpcre`@
" _oasis
if diff -u _oasis~ _oasis
then
  exit 1
fi
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/pcre
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING.txt README.md
/etc/ld.so.conf.d/*.conf
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.so

%files devel
%defattr(-,root,root,-)
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
