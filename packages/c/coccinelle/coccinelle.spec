#
# spec file for package coccinelle
#
# Copyright (c) 2026 SUSE LLC
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


%bcond_with coccinelle_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == ""
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif
%if "%build_flavor" == "doc"
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix -doc
%endif
%if "%build_flavor" == "testsuite"
%if %{without coccinelle_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%endif

%define     pkg coccinelle
%global _buildshell /bin/bash
Name:           %pkg%nsuffix
Version:        1.3.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Semantic patch utility
License:        GPL-2.0-only
URL:            http://coccinelle.lip6.fr/
Source0:        %pkg-%version.tar.xz
Source1:        %pkg.rpmlintrc
%if "%build_flavor" == ""
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(menhir)
BuildRequires:  ocamlfind(parmap)
BuildRequires:  ocamlfind(pcre2)
BuildRequires:  ocamlfind(pyml)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  pkgconfig(python3)
Requires:       findutils
Requires:       grep
Requires:       which
%description
Coccinelle is a program matching and transformation engine which
provides the language SmPL (Semantic Patch Language) for specifying
desired matches and transformations in C code. [It does not recognize
C++.]

Coccinelle performs collateral evolutions in software. Such
evolutions comprise the changes that are needed in client code in
response to evolutions in library APIs, and may include modifications
such as renaming a function, adding a function argument whose value
is somehow context-dependent, and reorganizing a data structure.
Beyond collateral evolutions, Coccinelle is used for finding and
fixing bugs in systems code.
%endif

%if "%build_flavor" == "doc"
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hevea
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(parmap)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  tex(8r.enc)
BuildRequires:  tex(alltt.sty)
BuildRequires:  tex(amsmath.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(boxedminipage.sty)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(endnotes.sty)
BuildRequires:  tex(epsfig.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(graphics.sty)
BuildRequires:  tex(graphicx.sty)
BuildRequires:  tex(hyperref.sty)
BuildRequires:  tex(ifgeo10.tfm)
BuildRequires:  tex(ifsym.sty)
BuildRequires:  tex(ifthen.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(listings.sty)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(pcrr8t.tfm)
BuildRequires:  tex(phvr8t.tfm)
BuildRequires:  tex(ptmr8t.tfm)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(times.sty)
BuildRequires:  tex(url.sty)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  tex(xspace.sty)
BuildRequires:  tex(xy.sty)
BuildRequires:  tex(babel-english.tex)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  texlive-latex
BuildRequires:  texlive-metafont
BuildRequires:  texlive-mfware
%description
Coccinelle is a program matching and transformation engine which
provides the language SmPL (Semantic Patch Language) for specifying
desired matches and transformations in C code.
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  %pkg = %version
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
%description
%endif

%prep
%setup -q -n %pkg-%version

%build
%if "%build_flavor" == ""
echo '%version' > version
autoreconf -fi
%configure \
	--enable-pcre-syntax \
	--with-python=$(realpath %__python3) \
	%nil
# Compiling the generated parser requires an extraordinary amount of stack
%if 0%{?qemu_user_space_build}
export QEMU_STACK_SIZE=$((32768*1024))
%else
ulimit -s 32768
%endif
%make_build -j1 VERBOSE=yes
%endif
%if "%build_flavor" == "doc"
echo '%version' > version
autoreconf -fi
%configure \
	--disable-pcre-syntax \
	--disable-python \
	%nil
pushd docs/manual
%make_build -j1 VERBOSE=yes pdf
popd
pushd tools/spgen/documentation
%make_build -j1 VERBOSE=yes docs
popd
%endif

%install
%if "%build_flavor" == ""
%make_install
# no GUI
rm -rfv %buildroot%_datadir/metainfo
mkdir -vp %buildroot%_bindir
cp -p tools/pycocci %buildroot%_bindir/pycocci
chmod -c 755 $_
mkdir -vp %buildroot%_datadir/vim/site
mv -vt $_ editors/vim/{ftdetect,syntax}
# OCaml libraries will have unsatisfied dependencies, unless everything is installed
mv {commons,globals,parsing_*}/*.{cmi,cmx} %buildroot%_libdir/%name/ocaml
# Python library have been named after directories in the site-packages hierarchy
mkdir -p "%buildroot/%python3_sitelib"
mv "%buildroot/%_libdir/%name/python/coccilib" "%buildroot/%python3_sitelib"
%fdupes %buildroot/%_prefix
%?python3_fix_shebang
%endif
%if "%build_flavor" == "doc"
mkdir -vp %buildroot%_defaultdocdir/%pkg
pushd docs/manual
mv -vt %buildroot%_defaultdocdir/%pkg *.pdf
popd
pushd tools/spgen/documentation
mv documentation.pdf spgen.pdf
mv -vt %buildroot%_defaultdocdir/%pkg *.pdf
popd
%endif

%if "%build_flavor" == "testsuite"
%check
spatch --ctestall
# bug#1192695
tee bug1192695.c <<'_EOC_'
#include <stdio.h>
int main(int argc, char *argv[]){return 0;}
_EOC_
tee bug1192695.cocci <<'_EOC_'
@initialize:ocaml@
@@

let ok_function p =
    not (List.mem (List.hd p).current_element ["kmem_getpages";"kmem_freepages"])

// convert the type in selected functions
@@
position p : script:ocaml() { ok_function p };
@@

- struct page@p
+ struct slab
_EOC_
spatch --sp-file bug1192695.cocci --include-headers --no-includes --smpl-spacing bug1192695.c
%endif

%if "%build_flavor" == ""
%files
%doc changes.txt copyright.txt
%license license.txt
%_bindir/*
%_datadir/bash-completion
%_datadir/vim
%_libdir/%name
%_mandir/*/*
%python3_sitelib/coccilib
%endif

%if "%build_flavor" == "doc"
%files
%doc %_defaultdocdir/%pkg
%endif

%changelog
