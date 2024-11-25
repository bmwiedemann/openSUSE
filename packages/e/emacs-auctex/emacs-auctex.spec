#
# spec file for package emacs-auctex
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with     tex4auto
%define tlversion 2024
%if %{undefined ext_el}
%define ext_el  .gz
%endif

Name:           emacs-auctex
Obsoletes:      ge_auc
Provides:       auc-tex
Provides:       auctex
Provides:       ge_auc
Requires:       emacs
Requires:       texlive-latex
Requires:       texlive-tools
Requires:       emacs(ELPA)
Recommends:     texlive-preview
Supplements:    (texlive and emacs)
BuildRequires:  emacs-x11
BuildRequires:  makeinfo
BuildRequires:  texinfo
%if %{with tex4auto}
BuildRequires:  ghostscript_any
BuildRequires:  texlive >= %tlversion
BuildRequires:  texlive-collection-latexextra >= %tlversion
BuildRequires:  texlive-latex >= %tlversion
BuildRequires:  texlive-tex >= %tlversion
BuildRequires:  texlive-texinfo >= %tlversion
%endif
Version:        14.0.7
Release:        0
Summary:        AUC TeX: An Emacs Extension
License:        GPL-3.0-or-later
Group:          Productivity/Editors/Emacs
Source0:        https://elpa.gnu.org/packages/auctex-%{version}.tar
Source1:        https://elpa.gnu.org/packages/auctex-%{version}.tar.sig
Source2:        auctex.keyring
Source3:        auctex-%{version}-auto-TL-%{tlversion}.tar.xz
Source4:        emacs-auctex-rpmlintrc
URL:            https://www.gnu.org/software/auctex
# Allows to select printer instance
# PATCH-FEATURE-UPSTREAM dvips.patch
Patch0:         dvips.patch
BuildArch:      noarch

%description
These macros make it easier for you to write TeX documents with GNU
Emacs.	Documentation can be found under:

/usr/share/doc/packages/emacs-auctex/

and in the dvi files math-ref.dvi and tex-ref.dvi (reference cards) and
in the info file auctex in emacs info-mode.

%define _sitedir %{_datadir}/emacs/site-lisp/elpa
%define _aucdir  %{_sitedir}/auctex-%{version}
%define _smp_mflags -j1

%prep
%setup -n auctex-%{version}
%patch -P0

%build
    unset ${!LC_*}
    LANG=en_US.UTF-8
    export LANG
    EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION=t
    export EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION
    emacs -batch -Q -l package -L ${PWD} \
        --eval "(setq package-user-dir \"/nonexistent\")" \
        --eval "(add-to-list 'package-directory-list \"${PWD}\")" \
         -f package-initialize -f batch-byte-compile *.el style/*.el
    mkdir ${PWD}/auto
%if %{with tex4auto}
    ignore="$(sed -rn '/^\(defcustom TeX-ignore-file/,+1{ s@^\s+@@;s@(\\\\)(\)\$)@\1|lwarp\\.sty\\\\\2@p }' < tex.el)"
    emacs -batch -Q -L ${PWD} \
	--eval "(setq TeX-lisp-directory \"${PWD}\")" \
	--eval "(setq TeX-install-font-lock #'ignore)" \
	--eval "(setq TeX-ignore-file ${ignore})" \
	--eval "(setq TeX-auto-global \"${PWD}/auto\")" \
	-l tex-site -l tex -l latex -l plain-tex -f TeX-auto-generate-global
%else
    TLVERSION=$(rpm -q --qf '%%{VERSION}' -f /etc/texmf)
    if test %{tlversion} -eq ${TLVERSION%%%%.*}
    then
	tar --use-compress-program=xz -xf %{S:3} -C ${PWD}/auto/
    else
	echo Rerun with %%bcond_without tex4auto to generate new
	echo auctex-%{version}-auto-TL-${TLVERSION%%%%.*}.tar.xz
	exit 1
    fi
%endif
    # Otherwise, e.g. the auto/url.el masks out the url/url.el from emacs lisp collections
    for dir in style auto
    do
        test -e ${dir}/.nosearch && continue
        echo ';; AUCTeX style/ and auto/ directories should not appear in load path.' > ${dir}/.nosearch
    done

    # This is part of the (recommended) texlive-preview
    rm -rvf latex/

    unset HOME
    emacs -batch -Q -l package \
	--eval '(setq package-user-dir "/nonexistent")' \
	--eval "(package-generate-autoloads \"auctex\" \"$(cwd)\")"

    pushd doc
%global info_files auctex.info preview-latex.info
        rm -vf *.info *.pdf
	texi2pdf -E auctex.texi
        pdftex tex-ref.tex
	makeinfo -I . auctex.texi
	makeinfo -I . preview-latex.texi
    popd

%install
    unset ${!LC_*}
    LANG=en_US.UTF-8
    export LANG
    EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION=t
    export EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION

unelc ()
{
    local elc=$1
    local elz=${elc%%.elc}.el.gz
    rm -vf $elc
    if test -n "$elz" -a -e "$elz" ; then
	gunzip "$elz"
    fi
}

    mkdir -p %{buildroot}%{_sitedir}/auctex-%{version}
    tar cpf - *.el *.elc auto/ style/ images/ | \
    tar xpf - -C %{buildroot}%{_sitedir}/auctex-%{version}/

    pushd doc
	install -m 644 -D -t %{buildroot}%{_infodir} preview-latex.info
	install -m 644 -D -t %{buildroot}%{_infodir} auctex.info*
    popd

    pushd %{buildroot}%{_sitedir}/auctex-%{version}
	find -name '*.el' -exec gzip -n -f9 '{}' \+
	unelc auctex-autoloads.elc
	unelc auctex-pkg.elc
	unelc auctex.elc
	unelc tex-site.elc
	unelc font-latex.elc
	# Workaround for old stuff in ~/.gnu-emacs which is about loading "auctex/font-latex"
	# in after-init-hook for existing AUCTeX version
	mkdir auctex
	pushd auctex
	    ln -sf ../font-latex.el .
	    echo ';; AUCTeX style/ and auto/ directories should not appear in load path.' > .nosearch
	popd
    popd

%triggerin -- emacs-nox
EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION=t
export EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION
if test -e %{_aucdir}/font-latex.el
then
  owd=$(pwd)
  cd %{_aucdir} || exit 0
  emacs -batch -Q --eval '(setq load-path (cons "." load-path)
    byte-compile-warnings nil
    TeX-lisp-directory "%{_aucdir}"
    TeX-auto-global "%{_aucdir}/auto")' -f batch-byte-compile font-latex.el > /dev/null 2>&1
  cd auctex
  ln -sf ../font-latex.elc .
  cd $owd
fi

%triggerin -- emacs-x11
EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION=t
export EMACS_INHIBIT_AUTOMATIC_NATIVE_COMPILATION
if test -e %{_aucdir}/font-latex.el
then
  owd=$(pwd)
  cd %{_aucdir} || exit 0
  emacs -batch -Q --eval '(setq load-path (cons "." load-path)
    byte-compile-warnings nil
    TeX-lisp-directory "%{_aucdir}"
    TeX-auto-global "%{_aucdir}/auto")' -f batch-byte-compile font-latex.el > /dev/null 2>&1
  cd auctex
  ln -sf ../font-latex.elc .
  cd $owd
fi

%post
for f in %info_files; do
 %install_info --info-dir=%{_infodir} %{_infodir}/$f.gz
done

%postun
for f in %info_files; do
  %install_info_delete --info-dir=%{_infodir} %{_infodir}/$f.gz
done

%files
%defattr(-, root, root)
%license COPYING
%doc README doc/*.pdf ChangeLog
%dir %{_sitedir}/
%dir %{_aucdir}/
%dir %{_aucdir}/auctex/
%dir %{_aucdir}/auto/
%dir %{_aucdir}/images/
%dir %{_aucdir}/style/
%doc %{_infodir}/*.info*.gz
%{_aucdir}/*.el
%{_aucdir}/*.el%{ext_el}
%ghost %verify(not mode) %{_aucdir}/font-latex.elc
%{_aucdir}/*.elc
%{_aucdir}/auctex/font-latex.el
%ghost %verify(not mode) %{_aucdir}/auctex/font-latex.elc
%{_aucdir}/auctex/.nosearch
%{_aucdir}/auto/*.el%{ext_el}
%{_aucdir}/auto/*.elc
%{_aucdir}/auto/.nosearch
%{_aucdir}/images/*.xbm
%{_aucdir}/images/*.xpm
%{_aucdir}/style/*.el%{ext_el}
%{_aucdir}/style/*.elc
%{_aucdir}/style/.nosearch

%changelog
