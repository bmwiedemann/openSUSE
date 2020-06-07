#
# spec file for package coq
#
# Copyright (c) 2020 SUSE LLC
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


Name:           coq
Version:        8.11.2
Release:        0
Summary:        Proof Assistant based on the Calculus of Inductive Constructions
License:        LGPL-2.1-only
Group:          Productivity/Scientific/Math
URL:            https://coq.inria.fr/
Source:         https://github.com/coq/coq/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        coq.desktop
Source2:        coq.xml
Source100:      %{name}-rpmlintrc
BuildRequires:  desktop-file-utils
BuildRequires:  memory-constraints
# Required for standard coq:
BuildRequires:  make >= 3.81
BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-camlp5-devel >= 5.08
# TODO: Build docs when antlr4-python3-runtime becomes available.
#BuildRequires:  python3-Sphinx
#BuildRequires:  python3-pexpect
#BuildRequires:  antlr4-python3-runtime
#BuildRequires:  python3-beautifulsoup4
# Required for coq-ide:
BuildRequires:  update-desktop-files
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(lablgtk3)
BuildRequires:  ocamlfind(num)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)

%global __requires_exclude ocaml\\\((Interface|Sos_types|GtkSourceView2_types)\\\)

%description
Proof assistant which allows to handle calculus assertions, check mechanically
proofs of these assertions, helps to find formal proofs and extracts a certified
program from the constructive proof of its formal specification.

This package contains shared files and the command line interface.
For a graphical interface install %{name}-ide.

%package ide
Summary:        IDE for The Coq Proof Assistant
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}-%{release}

%description ide
The Coq Integrated Development Interface is a graphical interface for the Coq proof assistant.

%package devel
Summary:        Development files for coq
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml >= 4.05.0

%description devel
This package contains development files for Coq.

%prep
%setup -q

%build
export CFLAGS='%{optflags}'
./configure                \
   -bindir %{_bindir}      \
   -libdir %{_libdir}/coq  \
   -mandir %{_mandir}      \
   -datadir %{_datadir}/%{name} \
   -docdir %{_docdir}/%{name} \
   -configdir %{_sysconfdir}/xdg/%{name} \
   -coqdocdir %{_datadir}/texmf/tex/latex/misc \
   -native-compiler yes \
   -natdynlink yes \
   -browser "xdg-open %s"

%limit_build -m 800
make %{?_smp_mflags} world

%install
# Fixup dependencies before we install. Some are apparently not detected.
sed -i 's#^ide/ide_MLLIB_DEPENDENCIES:=.*$#& ide/configwin_types ide/protocol/richpp#' \
    .mllibfiles.d

make COQINSTALLPREFIX=%{buildroot} install

%suse_update_desktop_file -i %{SOURCE1}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/coq.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/mime/packages/coq.xml
install -D -m 644 ide/coq.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/coq.png

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
chmod -x %{buildroot}%{_libdir}/%{name}/tools/TimeFileMaker.py
sed -i '1s|^#!/usr/bin/env *|#!/usr/bin/|;1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
    %{buildroot}%{_libdir}/%{name}/tools/make-{one-time-file,both-{time,single-timing}-files}.py

# Remove superfluous man page.
rm %{buildroot}%{_mandir}/man1/coqtop.byte.1

# Remove unneeded empty *.vos files.
find %{buildroot}%{_libdir}/coq -empty -name '*.vos' -delete

# Build lists of runtime and devel files by ending.
# Compiled theories and shared objects are needed at runtime.
find %{buildroot}%{_libdir}/coq/{plugins,theories} -type d | \
    sed "s|%{buildroot}|%%dir |g" >runtime.list
find %{buildroot}%{_libdir}/coq -name '*.cmxs' \
                -or -name '*.so' \
                -or -name '*.vo' | sed "s|%{buildroot}||g" >>runtime.list

# Object files, static libraries and import definitions are only needed for development.
# For now, we also put the standard library Coq sources here, since the runtime
# package contains the HTML documentation for the standard library.
find %{buildroot}%{_libdir}/coq -type d | sed "s|%{buildroot}|%%dir |g" >devel.list
find %{buildroot}%{_libdir}/coq -name '*.a' \
                -or -name '*.cma' \
                -or -name '*.cmi' \
                -or -name '*.cmx' \
                -or -name '*.cmxa' \
                -or -name '*.glob' \
                -or -name '*.o' \
                -or -name '*.v' | sed "s|%{buildroot}||g" >>devel.list

%files -f runtime.list
%license LICENSE CREDITS
%doc README.md
%{_docdir}/%{name}/FAQ-CoqIde

%{_bindir}/coq-tex
%{_bindir}/coq_makefile
%{_bindir}/coqc
%{_bindir}/coqchk
%{_bindir}/coqdep
%{_bindir}/coqdoc
%{_bindir}/coqpp
%{_bindir}/coqproofworker.opt
%{_bindir}/coqqueryworker.opt
%{_bindir}/coqtacticworker.opt
%{_bindir}/coqtop
%{_bindir}/coqtop.opt
%{_bindir}/coqwc
%{_bindir}/coqworkmgr
%{_bindir}/votour

%dir %{_libdir}/coq
%{_libdir}/coq/META
%{_libdir}/coq/revision
%dir %{_libdir}/coq/kernel
%dir %{_libdir}/coq/kernel/byterun
%{_libdir}/coq/plugins/micromega/csdpcert
%{_libdir}/coq/tools
%exclude %{_libdir}/coq/tools/CoqMakefile.in
%dir %{_libdir}/coq/user-contrib

%{_mandir}/man1/coq-tex.1%{ext_man}
%{_mandir}/man1/coq_makefile.1%{ext_man}
%{_mandir}/man1/coqc.1%{ext_man}
%{_mandir}/man1/coqchk.1%{ext_man}
%{_mandir}/man1/coqdep.1%{ext_man}
%{_mandir}/man1/coqdoc.1%{ext_man}
%{_mandir}/man1/coqtop.1%{ext_man}
%{_mandir}/man1/coqtop.opt.1%{ext_man}
%{_mandir}/man1/coqwc.1%{ext_man}

%{_datadir}/%{name}
%dir %{_datadir}/texmf
%dir %{_datadir}/texmf/tex
%dir %{_datadir}/texmf/tex/latex
%dir %{_datadir}/texmf/tex/latex/misc
%{_datadir}/texmf/tex/latex/misc/coqdoc.sty

%files ide
%{_bindir}/coqide
%{_bindir}/coqidetop
%{_bindir}/coqidetop.opt
%{_mandir}/man1/coqide.1%{ext_man}
%{_datadir}/applications/coq.desktop
%{_datadir}/icons/hicolor/256x256/apps/coq.png
%{_datadir}/mime/packages/coq.xml

%files devel -f devel.list
%{_libdir}/coq/tools/CoqMakefile.in

%changelog
