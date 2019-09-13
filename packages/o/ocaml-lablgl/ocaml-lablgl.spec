#
# spec file for package ocaml-lablgl
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


Name:           ocaml-lablgl
Version:        1.05
Release:        0
%{?ocaml_preserve_bytecode}

Summary:        LablGL is an OpenGL interface for Objective Caml
License:        BSD-3-Clause
Group:          Development/Languages/OCaml

Url:            https://forge.ocamlcore.org/projects/lablgl/
Source0:        lablgl-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  Mesa-devel
BuildRequires:  freeglut-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  xorg-x11-proto-devel

%description
LablGL is is an Objective Caml interface to OpenGL. Support is
included for use inside LablTk, and LablGTK also includes specific
support for LablGL.  It can be used either with proprietary OpenGL
implementations (SGI, Digital Unix, Solaris...), with XFree86 GLX
extension, or with open-source Mesa.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       ocaml-labltk-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n lablgl-%{version}

cat > Makefile.config <<EOF
%if 0%{?ocaml_native_compiler}
CAMLC = ocamlc.opt
CAMLOPT = ocamlopt.opt
%else
CAMLC = ocamlc
CAMLOPT = ocamlc
%endif
BINDIR = %{_bindir}
XINCLUDES = -I%{_prefix}/X11R6/include
XLIBS = -lXext -lXmu -lX11
TKINCLUDES = -I%{_includedir}
GLINCLUDES =
GLLIBS = -lGL -lGLU
GLUTLIBS = -lglut -lXxf86vm
RANLIB = :
LIBDIR = %{_libdir}/ocaml
DLLDIR = %{_libdir}/ocaml/stublibs
INSTALLDIR = %{_libdir}/ocaml/lablGL
TOGLDIR=Togl
COPTS = $RPM_OPT_FLAGS
EOF

%build
make all
%if 0%{?ocaml_native_compiler}
make opt
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
make INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL \
    DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    install

# Make and install a META file.
cat <<EOM >META
version="%{version}"
directory="+lablgl"
archive(byte) = "lablgl.cma"
archive(native) = "lablgl.cmxa"

package "togl" (
  requires = "labltk lablgl"
  archive(byte) = "togl.cma"
  archive(native) = "togl.cmxa"
)

package "glut" (
  requires = "lablgl"
  archive(byte) = "lablglut.cma"
  archive(native) = "lablglut.cmxa"
)
EOM
cp META $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd
#
mkdir -vp %{buildroot}/etc/ld.so.conf.d/
tee %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<_EOF_
%{_libdir}/ocaml/stublibs
_EOF_
#

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README
/etc/ld.so.conf.d/*.conf
%{_bindir}/lablgl
%{_bindir}/lablglut
%dir %{_libdir}/ocaml/lablGL
%{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(-,root,root,-)
%doc CHANGES COPYRIGHT README LablGlut/examples Togl/examples
%{_libdir}/ocaml/lablGL/META
%{_libdir}/ocaml/lablGL/*.a
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/lablGL/*.cmxa
%{_libdir}/ocaml/lablGL/*.cmx
%endif
%{_libdir}/ocaml/lablGL/*.cma
%{_libdir}/ocaml/lablGL/*.cmi
%{_libdir}/ocaml/lablGL/*.mli
%{_libdir}/ocaml/lablGL/build.ml

%changelog
