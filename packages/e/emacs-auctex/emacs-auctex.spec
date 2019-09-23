#
# spec file for package emacs-auctex
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           emacs-auctex
BuildRequires:  emacs-x11
BuildRequires:  ghostscript_any
BuildRequires:  texlive
BuildRequires:  texlive-latex
Obsoletes:      ge_auc
Provides:       auc-tex
Provides:       auctex
Provides:       ge_auc
Requires:       emacs
Requires:       texlive-latex
Requires:       texlive-tools
%if %suse_version > 1220
BuildRequires:  makeinfo
BuildRequires:  texinfo
BuildRequires:  texlive-collection-latexextra
BuildRequires:  texlive-tex
BuildRequires:  texlive-texinfo
%endif
Version:        12.1
Release:        0
Summary:        AUC TeX: An Emacs Extension
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
Source:         http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.gz
Url:            http://www.gnu.org/software/auctex
# Allows to select printer instance
# PATCH-FEATURE-UPSTREAM dvips.patch
Patch0:         dvips.patch
Patch10:        utf8-names-3b1ffcd8.patch
Patch11:        utf8-names-a8ea1273.patch
Patch12:        utf8-names-fix-boo1135326.patch
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

%prep
%setup -n auctex-%{version}
%patch0
%patch10
%patch11
%patch12

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
    find , -name '*.elc' | xargs -r rm -f
    make %{?_smp_mflags}
    make -C doc clean
    make -C doc %{?_smp_mflags}
    make -C doc extradist
    rm -rf /tmp/auctex

%install
    export LC_CTYPE=ISO-8859-1
    mkdir -p %{buildroot}%{_sitedir}/site-start.d
    make install DESTDIR=%{buildroot}
    rm -rf %{buildroot}%{_aucdir}/auto
    pushd %{buildroot}%{_aucdir}/
	emacs --no-site -batch -L %{buildroot}%{_sitedir}/auctex 		\
	    --eval '(setq TeX-lisp-directory "%{buildroot}%{_aucdir}")'		\
	    --eval '(setq TeX-auto-global "%{buildroot}%{_aucdir}/auto")'	\
	    -l %{buildroot}%{_sitedir}/tex-site.el -f TeX-auto-generate-global
    popd
    touch %{buildroot}%{_aucdir}/auto/.nosearch
    find %{buildroot}%{_aucdir}/auto/ -name '*.elc' | xargs -r rm -f
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
%{_aucdir}/auto/*.el
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
