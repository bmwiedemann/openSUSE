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
Version:        13.3
Release:        0
Summary:        AUC TeX: An Emacs Extension
License:        GPL-3.0-or-later
Group:          Productivity/Editors/Emacs
Source0:        https://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.gz.sig
Source2:        auctex.keyring
Source3:        auctex-%{version}-auto-TL-%{tlversion}.tar.xz
URL:            https://www.gnu.org/software/auctex
# Allows to select printer instance
# PATCH-FEATURE-UPSTREAM dvips.patch
Patch0:         dvips.patch
Patch1:         auctex-13.1-expand.patch
Patch3:         initial-reset.patch
Patch4:         dinbrief.patch
BuildArch:      noarch

%description
These macros make it easier for you to write TeX documents with GNU
Emacs.	Documentation can be found under:

/usr/share/doc/packages/emacs-auctex/

and in the dvi files math-ref.dvi and tex-ref.dvi (reference cards) and
in the info file auctex in emacs info-mode.

AuC TeX is integrated in XEmacs 19.15 and higher, so these packages may
not be installed concurrently.	Note that the binary formats of the
byte-compiled lisp files of the two emacs editors are incompatible, so
you cannot use this package for XEmacs.

%define _sitedir %{_datadir}/emacs/site-lisp
%define _aucdir  %{_sitedir}/auctex
%define _smp_mflags -j1

%prep
%setup -n auctex-%{version}
%patch -P0
%patch -P1
%patch -P3
%patch -P4

%build
    unset ${!LC_*}
    LANG=en_US.UTF-8
    export LANG
    rm -rf /tmp/auctex
    mkdir  /tmp/auctex
    mkdir -p /tmp/auctex/doc/preview
    mkdir -p /tmp/auctex/latex/preview
    %configure \
	--docdir=%{_defaultdocdir}/%name	\
	--with-emacs				\
	--with-lispdir=%{_sitedir}		\
	--with-auto-dir=%{_aucdir}/auto		\
	--with-texmf-dir=%{_datadir}/texmf	\
	--with-doc-dir=/tmp/auctex/doc/preview	\
	--with-tex-dir=/tmp/auctex/latex/preview
    find . -name '*.elc' | xargs -r rm -f
    %make_build
    %{__make} %{_make_output_sync} -C doc clean
    %{__make} %{_make_output_sync} -C doc %{?_smp_mflags}
    %{__make} %{_make_output_sync} -C doc extradist
    rm -rf /tmp/auctex

%install
    export LC_CTYPE=ISO-8859-1
    mkdir -p %{buildroot}%{_sitedir}/site-start.d
    %make_install DESTDIR=%{buildroot}
    pushd %{buildroot}%{_aucdir}/auto/
%if %{with tex4auto}
	pwd
	echo "Run the command TeX-auto-generate-global in mini buffer"
	ignore="$(sed -rn '/^\(defcustom TeX-ignore-file/,+1{ s@^\s+@@;s@(\\\\)(\)\$)@\1|lwarp\\.sty\\\\\2@p }' < ../tex.el)"
	emacs-gtk -batch -Q -L %{buildroot}%{_sitedir}/auctex 			\
	    --eval '(setq TeX-lisp-directory "%{buildroot}%{_aucdir}")'		\
	    --eval "(setq TeX-install-font-lock #'ignore)"			\
	    --eval "(setq TeX-ignore-file ${ignore})"				\
	    --eval '(setq TeX-auto-global "%{buildroot}%{_aucdir}/auto")'	\
	    -l %{buildroot}%{_sitedir}/tex-site.el -f TeX-auto-generate-global
	exit 1
%else
	TLVERSION=$(rpm -q --qf '%%{VERSION}' -f /etc/texmf)
	if test %{tlversion} -eq ${TLVERSION%%%%.*}
	then
	    tar --use-compress-program=xz -xf %{S:3}
	    touch %{buildroot}%{_aucdir}/auto/.nosearch
	else
	    echo Rerun with %%bcond_without tex4auto to generate new
	    echo auctex-%{version}-auto-TL-${TLVERSION%%%%.*}.tar.xz
	    exit 1
	fi
%endif
    popd
    cat <<-EOF > %{buildroot}%{_sitedir}/suse-start-auctex.el
	;;; suse-start-auctex.el
	;;
	;; This is used for starting up AUCTeX
	;; See (info "(auctex)Introduction") on how to disable AUCTeX.
	;;
	(load "auctex.el" nil t t)
	EOF
    cat <<-EOF > %{buildroot}%{_sitedir}/suse-start-preview-latex.el
	;;; suse-start-preview-latex.el
	;;
	;; This is used for starting up preview-latex of AUCTeX
	;; See (info "(auctex)Introduction") on how to disable AUCTeX.
	;;
	(load "preview-latex.el" nil t t)
	EOF
    for el in auctex.el preview-latex.el
    do
	test -e %{buildroot}%{_sitedir}/$el || continue
	mv %{buildroot}%{_sitedir}/$el %{buildroot}%{_sitedir}/site-start.d/
    done
    #
    # Preview is part of te_latex
    #
    rm -rf %{buildroot}/tmp/auctex
%define info_files auctex.info preview-latex.info

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
%doc README COPYING doc/*.pdf CHANGES
%dir %{_sitedir}/
%dir %{_aucdir}/
%dir %{_aucdir}/auto/
%dir %{_aucdir}/images/
%dir %{_aucdir}/style/
%doc %{_infodir}/*.info*.gz
%{_aucdir}/*.el
%{_aucdir}/*.elc
%{_aucdir}/auto/*.el%{ext_el}
%{_aucdir}/auto/*.elc
%{_aucdir}/auto/.nosearch
%{_aucdir}/images/*.xpm
%{_aucdir}/style/*.el
%{_aucdir}/style/*.elc
%{_aucdir}/auto/.nosearch
%{_aucdir}/style/.nosearch
%config %{_sitedir}/suse-start*.el
%config %{_sitedir}/tex-site.el
%config %{_sitedir}/site-start.d/auctex.el
%config %{_sitedir}/site-start.d/preview-latex.el

%changelog
