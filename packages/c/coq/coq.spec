#
# spec file for package coq
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2012-2018 Peter Trommler, peter.trommler at ohm-hochschule.de
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


# Project has been renamed, but unclear how to rename in OBS.
%global _name rocq

%bcond_without ide

%global dune_packages rocq-runtime,rocq-core
%if %{with ide}
%global dune_packages %{dune_packages},rocqide,coqide-server
%endif

Name:           coq
Version:        9.1.1
Release:        0
Summary:        Proof Assistant based on the Calculus of Inductive Constructions
License:        LGPL-2.1-only
Group:          Productivity/Scientific/Math
URL:            https://rocq-prover.org/
Source:         https://github.com/rocq-prover/rocq/archive/V%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source1:        org.rocq-prover.rocqide.desktop
Source2:        org.rocq-prover.rocqide.metainfo.xml
Source3:        %{_name}.xml
Source50:       %{_name}-refman-%{version}.tar.xz
Source51:       %{_name}-corelib-doc-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  make >= 3.81
BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-camlp5-devel >= 5.08
BuildRequires:  ocaml-dune >= 3.8.3
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(zarith)
%if %{with ide}
BuildRequires:  update-desktop-files
BuildRequires:  ocamlfind(lablgtk3-sourceview3)
%endif
Requires:       ocamlfind

%description
Empty dummy package.

%package -n %{_name}
Summary:        Proof Assistant based on the Calculus of Inductive Constructions
Group:          Productivity/Scientific/Math
Provides:       coq = %{version}-%{release}
Obsoletes:      coq < 9.0.0

%description -n %{_name}
Proof assistant which allows to handle calculus assertions, check mechanically
proofs of these assertions, helps to find formal proofs and extracts a certified
program from the constructive proof of its formal specification.

This package contains shared files and the command line interface.
For a graphical interface install %{_name}-ide.

%package -n %{_name}-ide
Summary:        IDE for The Coq Proof Assistant
Group:          Productivity/Scientific/Math
Requires:       %{_name} = %{version}
Provides:       coq-ide = %{version}-%{release}
Obsoletes:      coq-ide < 9.0.0

%description -n %{_name}-ide
The Coq Integrated Development Interface is a graphical interface for the Coq proof assistant.

%package -n %{_name}-devel
Summary:        Development files for coq
Group:          Development/Libraries/Other
Requires:       %{_name} = %{version}
Requires:       ocaml >= 4.09.0
Provides:       coq-devel = %{version}-%{release}
Obsoletes:      coq-devel < 9.0.0

%description -n %{_name}-devel
This package contains development files for Coq.

%package -n %{_name}-doc
Summary:        Documentation for coq
Group:          Documentation/HTML
License:        OPUBL-1.0
Requires:       %{_name} = %{version}
Provides:       coq-doc = %{version}-%{release}
Obsoletes:      coq-doc < 9.0.0
BuildArch:      noarch

%description -n %{_name}-doc
HTML reference manual for Coq.

%prep
%setup -q -a 50 -a 51 -n %{_name}-%{version}

%build
%if 0%{?qemu_user_space_build}
# The OCaml compiler sometimes needs a bit more stack than the usual limit.
# While ocaml-rpm-macros increases the limit, this doesn't affect a QEMU build.
# We add a wrapper script to PATH. This doesn't affect the processes started by
# Dune, but coqc itself uses the compiler from PATH.
mkdir bin
echo "#!/bin/bash
exec /usr/bin/qemu-%{_host_cpu} -s $((64*1024*1024)) /usr/bin/ocamlopt.opt \"\$@\"" >bin/ocamlopt.opt
chmod +x bin/ocamlopt.opt
export PATH=$PWD/bin:$PATH
%endif

export CFLAGS='%{optflags}'
./configure                \
   -prefix %{_prefix}      \
   -libdir %{_libdir}/coq  \
   -mandir %{_mandir}      \
   -datadir %{_datadir}/%{_name} \
   -docdir %{_docdir}/%{_name} \
   -configdir %{_sysconfdir}/xdg/%{_name} \
   -native-compiler yes \
   -natdynlink yes \
   -browser "xdg-open %s"
make %{?_smp_mflags} dunestrap

dune_release_pkgs='%{dune_packages}'
%ocaml_dune_setup
%ocaml_dune_build

%install
%global ocaml_standard_library %{_libdir}
%ocaml_dune_install

%if %{with ide}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/org.rocq-prover.rocqide.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo/org.rocq-prover.rocqide.metainfo.xml
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/rocq.xml
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
ln -s %{_datadir}/coq/coq.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rocq.png
%endif

# Fix executable bit and shebangs, preferring python3.
# (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
chmod -x %{buildroot}%{_libdir}/rocq-runtime/tools/TimeFileMaker.py
sed -i '1s|^#!/usr/bin/env *|#!/usr/bin/|;1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
    %{buildroot}%{_libdir}/rocq-runtime/tools/make-{one-time-file,both-{time,single-timing}-files}.py

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
#     -cJf ../../coq-refman-%{version}.tar.xz refman
# tar --sort=name --owner=0 --group=0 --mtime="@${SOURCE_DATE_EPOCH}" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf ../../coq-corelib-doc-%{version}.tar.xz corelib
# popd

# Slim down documentation pages, add some margin directly.
find corelib/ -name '*.html' -exec sed -i '
s#https://rocq-prover\.org/css/stdlib\.css#%{_libdir}/rocq-runtime/tools/coqdoc/coqdoc.css#
/<meta [^h]/d
/<link .* href="https:\/\/rocq-prover\.org.*"/d
/<script defer="".* src=".*"><\/script>/d
/<style>/,/<\/style>/d
/<body/i<body style="margin:1em;"><!--
/<body/,/END CORELIB HEADER/d
/START CORELIB FOOTER/,/<\/body>/d
/<\/html>/i-->\n</body>
' {} +
mkdir -p %{buildroot}%{_docdir}/%{_name}
cp -r corelib refman %{buildroot}%{_docdir}/%{_name}
rm -r %{buildroot}%{_docdir}/%{_name}/refman/{.buildinfo,.doctrees,_sources}

%fdupes %{buildroot}%{_docdir}/%{_name}

%files -n %{_name} -f dir.list -f runtime.list
%license LICENSE CREDITS

%{_bindir}/rocq
%{_bindir}/rocq.byte
%{_bindir}/rocqchk
%{_bindir}/csdpcert
%{_bindir}/ocamllibdep
%{_bindir}/votour

%{_libdir}/rocq-runtime/rocqnative
%{_libdir}/rocq-runtime/rocqworker
%{_libdir}/rocq-runtime/rocqworker.byte
%{_libdir}/rocq-runtime/rocqworker_with_drop
%{_libdir}/rocq-runtime/tools
%exclude %{_libdir}/rocq-runtime/tools/CoqMakefile.in

%{_mandir}/man1/rocq.1%{ext_man}
%{_mandir}/man1/rocqchk.1%{ext_man}

%dir %{_datadir}/texmf
%dir %{_datadir}/texmf/tex
%dir %{_datadir}/texmf/tex/latex
%dir %{_datadir}/texmf/tex/latex/misc
%{_datadir}/texmf/tex/latex/misc/coqdoc.sty

%{_libdir}/{%{dune_packages}}/META

%if %{with ide}
%files -n %{_name}-ide
%{_bindir}/rocqide
%{_bindir}/coqidetop
%{_mandir}/man1/rocqide.1%{ext_man}
%{_datadir}/coq
%{_datadir}/applications/org.rocq-prover.rocqide.desktop
%{_datadir}/icons/hicolor/256x256/apps/rocq.png
%{_datadir}/metainfo/org.rocq-prover.rocqide.metainfo.xml
%{_datadir}/mime/packages/rocq.xml
%endif

%files -n %{_name}-devel -f dir.list -f devel.list
%{_libdir}/rocq-runtime/revision
%{_libdir}/rocq-runtime/dev/ml_toplevel
%{_libdir}/{%{dune_packages}}/{dune-package,opam}
%{_libdir}/rocq-runtime/tools/CoqMakefile.in

%files -n %{_name}-doc
%dir %{_docdir}/%{_name}
%{_docdir}/%{_name}/corelib
%{_docdir}/%{_name}/refman

%changelog
