#
# spec file for package coq
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012-2018 Peter Trommler, peter.trommler at ohm-hochschule.de
# Copyright (c) 2023 Aaron Puchert <aaronpuchert@alice-dsl.net>
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


%bcond_without ide

Name:           coq
Version:        8.16.1
Release:        0
Summary:        Proof Assistant based on the Calculus of Inductive Constructions
License:        LGPL-2.1-only
Group:          Productivity/Scientific/Math
URL:            https://coq.inria.fr/
Source:         https://github.com/coq/coq/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        fr.inria.coq.coqide.desktop
Source2:        fr.inria.coq.coqide.metainfo.xml
Source3:        coq.xml
Source50:       coq-refman-%{version}.tar.xz
Source51:       coq-stdlib-%{version}.tar.xz
Source100:      %{name}-rpmlintrc
BuildRequires:  desktop-file-utils
BuildRequires:  make >= 3.81
BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-camlp5-devel >= 5.08
BuildRequires:  ocaml-dune >= 2.5.1
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(zarith)
%if %{with ide}
BuildRequires:  update-desktop-files
BuildRequires:  ocamlfind(lablgtk3-sourceview3)
%endif
Requires:       ocamlfind

%description
Proof assistant which allows to handle calculus assertions, check mechanically
proofs of these assertions, helps to find formal proofs and extracts a certified
program from the constructive proof of its formal specification.

This package contains shared files and the command line interface.
For a graphical interface install %{name}-ide.

%package ide
Summary:        IDE for The Coq Proof Assistant
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}

%description ide
The Coq Integrated Development Interface is a graphical interface for the Coq proof assistant.

%package devel
Summary:        Development files for coq
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       ocaml >= 4.09.0

%description devel
This package contains development files for Coq.

%package doc
Summary:        Documentation for coq
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
HTML reference manual for Coq and full documentation of the standard library.

%prep
%setup -q -a 50 -a 51

%build
export CFLAGS='%{optflags}'
# TODO: Add -with-doc yes
./configure                \
   -prefix %{_prefix}      \
   -libdir %{_libdir}/coq  \
   -mandir %{_mandir}      \
   -datadir %{_datadir}/%{name} \
   -docdir %{_docdir}/%{name} \
   -configdir %{_sysconfdir}/xdg/%{name} \
%if %{with ide}
   -coqide opt \
%else
   -coqide no \
%endif
   -native-compiler yes \
   -natdynlink yes \
   -browser "xdg-open %s"

make %{?_smp_mflags} world

%install
make DESTDIR=%{buildroot} install

# For some reason, some of the files are installed into /usr/lib.
%if "%{_libdir}" != "%{_prefix}/lib"
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}
%endif

%if %{with ide}
%suse_update_desktop_file -i %{SOURCE1}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/fr.inria.coq.coqide.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo/fr.inria.coq.coqide.metainfo.xml
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/coq.xml
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
ln -s %{_datadir}/coq/coq.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/coq.png
%else
rm %{buildroot}%{_bindir}/coqidetop{.byte,.opt}
%endif

# Sometimes we get identical x and x.opt files, replace by symlink x -> x.opt.
for bin in %{buildroot}%{_bindir}/*.opt
do
    if [ -f ${bin%.opt} ] && diff $bin ${bin%.opt}
    then
        rm ${bin%.opt}
        ln -s ${bin#%{buildroot}} ${bin%.opt}
    fi
done

# Fix executable bit and shebangs, preferring python3.
# (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
chmod -x %{buildroot}%{_libdir}/coq-core/tools/TimeFileMaker.py
sed -i '1s|^#!/usr/bin/env *|#!/usr/bin/|;1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
    %{buildroot}%{_libdir}/coq-core/tools/make-{one-time-file,both-{time,single-timing}-files}.py

# Remove installed LICENSE, we put it elsewhere.
rm %{buildroot}%{_docdir}/%{name}/coq{-core,ide,ide-server}/LICENSE

# Remove superfluous man page.
rm %{buildroot}%{_mandir}/man1/coqtop.byte.1

# Remove unneeded empty *.vos files.
find %{buildroot}%{_libdir}/coq -empty -name '*.vos' -delete

# Build lists of runtime and devel files by ending.
# Compiled theories and shared objects are needed at runtime.
find %{buildroot}%{_libdir} -type d | sed "s|%{buildroot}|%%dir |g" >dir.list
sed -i '1d; /coq-core\/tools/d' dir.list
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
# svn export https://github.com/coq/doc/trunk/V%{version}/refman
# svn export https://github.com/coq/doc/trunk/V%{version}/stdlib
# tar --sort=name --owner=0 --group=0 --mtime="@$(stat -c %%Y refman/index.html)" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf coq-refman-%{version}.tar.xz refman
# tar --sort=name --owner=0 --group=0 --mtime="@$(stat -c %%Y stdlib/index.html)" \
#     --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
#     -cJf coq-stdlib-%{version}.tar.xz stdlib

# Drop some CSS files and headers in stdlib documentation, add some margin directly.
find stdlib/ -name '*.html' -exec sed -i '
s#//coq.inria.fr/sites/all/themes/coq/coqdoc.css#%{_libdir}/coq-core/tools/coqdoc/coqdoc.css#
/<link type="text\/css" rel="stylesheet" media="all" href="\/\/coq.inria.fr\/.*.css" \/>/d
/<div id="container">/s/>/ style="margin:1em;">/
/^  <div id="headertop">$/,/^  <\/div>$/d
/^  <div id="header">$/,/^  <\/div>$/d
' {} +
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r refman stdlib %{buildroot}%{_docdir}/%{name}
rm -r %{buildroot}%{_docdir}/%{name}/refman/{.buildinfo,.doctrees,_sources}

%files -f dir.list -f runtime.list
%license LICENSE CREDITS

%{_bindir}/coq-tex
%{_bindir}/coq_makefile
%{_bindir}/coqc
%{_bindir}/coqc.byte
%{_bindir}/coqchk
%{_bindir}/coqdep
%{_bindir}/coqdoc
%{_bindir}/coqnative
%{_bindir}/coqpp
%{_bindir}/coqproofworker.opt
%{_bindir}/coqqueryworker.opt
%{_bindir}/coqtacticworker.opt
%{_bindir}/coqtop
%{_bindir}/coqtop.byte
%{_bindir}/coqtop.opt
%{_bindir}/coqwc
%{_bindir}/coqworkmgr
%{_bindir}/csdpcert
%{_bindir}/ocamllibdep
%{_bindir}/votour

%{_libdir}/coq-core/tools
%exclude %{_libdir}/coq-core/tools/CoqMakefile.in

%{_mandir}/man1/coq-tex.1%{ext_man}
%{_mandir}/man1/coq_makefile.1%{ext_man}
%{_mandir}/man1/coqc.1%{ext_man}
%{_mandir}/man1/coqchk.1%{ext_man}
%{_mandir}/man1/coqdep.1%{ext_man}
%{_mandir}/man1/coqdoc.1%{ext_man}
%{_mandir}/man1/coqnative.1%{ext_man}
%{_mandir}/man1/coqtop.1%{ext_man}
%{_mandir}/man1/coqtop.opt.1%{ext_man}
%{_mandir}/man1/coqwc.1%{ext_man}

%dir %{_datadir}/texmf
%dir %{_datadir}/texmf/tex
%dir %{_datadir}/texmf/tex/latex
%dir %{_datadir}/texmf/tex/latex/misc
%{_datadir}/texmf/tex/latex/misc/coqdoc.sty

%dir %{_docdir}/%{name}
%{_docdir}/%{name}/coq-core

%if %{with ide}
%files ide
%{_bindir}/coqide
%{_bindir}/coqidetop.byte
%{_bindir}/coqidetop.opt
%{_mandir}/man1/coqide.1%{ext_man}
%{_datadir}/%{name}
%{_datadir}/applications/fr.inria.coq.coqide.desktop
%{_datadir}/icons/hicolor/256x256/apps/coq.png
%{_datadir}/metainfo/fr.inria.coq.coqide.metainfo.xml
%{_datadir}/mime/packages/coq.xml
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/coqide
%{_docdir}/%{name}/coqide-server
%endif

%files devel -f dir.list -f devel.list
%{_libdir}/coq-core/revision
%{_libdir}/{coq,coq-core,coq-stdlib,coqide,coqide-server}/{META,dune-package,opam}
%{_libdir}/coq-core/tools/CoqMakefile.in

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/refman
%{_docdir}/%{name}/stdlib

%changelog
