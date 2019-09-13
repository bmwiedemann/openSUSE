#
# spec file for package psgml
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           psgml
BuildRequires:  emacs-nox
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
BuildRequires:  unzip
%define tdtd tdtd.zip
Requires:       emacs_program
Summary:        Emacs Add-On to edit SGML/XML documents
License:        GPL-2.0+ and SUSE-Public-Domain
Group:          Productivity/Editors/Emacs
Version:        1.4.1
Release:        0
Source:         https://marmalade-repo.org/packages/psgml-%{version}.tar
Source1:        http://home.sprynet.com/sprynet/dmeggins/psgml-dsssl.el
Source2:        http://logimac.mathematik.uni-freiburg.de/mixed/psgml-ja.tgz
Source3:        http://www.menteith.com/tdtd/data/tdtd.zip
Source4:        http://www.iro.umontreal.ca/~pinard/xxml/xxml.tar.gz
Source5:        http://www.megginson.com/Software/psgml-xpointer.el
Source6:        %{name}-README.openSUSE
Source7:        ke-docbook.el
Source8:        suse-start-psgml.el
Source9:        psgml-html.el
Patch:          psgml-compile-addons.diff
Patch2:         psgml-1.2.5-key.diff
Patch3:         psgml-xpointer.el.diff
Patch4:         psgml-1.3.1-texi-category.diff
Patch5:         psgml-xxml-namespace-face.diff
Patch6:         tdtd-dtd-patch
Patch7:         xxml-indentation.diff
Patch8:         flavour.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://sourceforge.net/projects/psgml/
PreReq:         %install_info_prereq

%description
'psgml' supports you while editing SGML/XML documents.	It respects the
context of the used DTD (Document Type Definition) and offers the valid
elements and attributes.

Included are several helper tools: tdtd, xxml, psgml-xpointer.

For more info see README.openSUSE.

Compiled for GNU Emacs (XEmacs has its own version!).



Authors:
--------
    James Clark <jjc@clark.com>
    Lennart Staflin <lenst@lysator.liu.se>
    David Megginson <dmeggins@sprynet.com>
    Matthias Clasen <mclasen@sun2.mathematik.uni-freiburg.de>
    François Pinard <pinard@iro.umontreal.ca>
    etc.

%prep
%setup -q
%patch -p1
cp -p %{SOURCE1} .
# xxml
mkdir xxml
tar vxz -C xxml -f %{SOURCE4}
%patch -P 5 -p0
%patch7 -p1
cp xxml/xxml.el .
for f in README THANKS; do
  cp xxml/$f $f.xxml
done
cp -p %{SOURCE5} .
%patch -P 2 -p1 -P 3 -p1 -P 4 -p1
%setup -q -T -D -a 2
mv psgml-jade/psgml-jade.el .
unzip -o -a %{SOURCE3}
# Add write permissions so that we can patch it
chmod u+w tutorial.txt
cp -p %{SOURCE6} README.openSUSE
cp -p %{SOURCE7} .
cp -p %{SOURCE8} .
cp -p %{S:9} .
%patch -p 1 -P 6
%patch8

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir}
make # emacs
echo "(add-to-list (quote load-path) (getenv \"PWD\"))" > load-psgml.el
emacs --batch -Q -l load-psgml.el \
      -l ./tdtd-font.el \
      -f batch-byte-compile tdtd-font.el tdtd.el
emacs --batch -Q -l load-psgml.el -f batch-byte-compile xxml.el
emacs --batch -Q -l load-psgml.el -l ./xxml.el \
      -f batch-byte-compile ke-docbook.el
emacs --batch -Q -l load-psgml.el -f batch-byte-compile psgml-xpointer.el
emacs --batch -Q -l load-psgml.el -l tempo -f batch-byte-compile psgml-html.el
makeinfo psgml.texi
makeinfo psgml-api.texi

%install
[ -z $RPM_BUILD_ROOT ] || rm -fr $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml \
                 $RPM_BUILD_ROOT%{_infodir}
# to avoid timestamp problems, install .el files first.
install -p -m644 *.el $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml
rm -f $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/suse-start*
make install prefix="$RPM_BUILD_ROOT%{_prefix}" \
             lispdir="$RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml" \
             infodir="$RPM_BUILD_ROOT%{_infodir}"
make install-info prefix="$RPM_BUILD_ROOT%{_prefix}" \
                  lispdir="$RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml" \
                  infodir="$RPM_BUILD_ROOT%{_infodir}"
#install -p -m644 suse-start-psgml.el \
#    $RPM_BUILD_ROOT%%{_prefix}/share/emacs/site-lisp/suse-start-psgml.el
install -p -m644 iso88591.map \
    $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/iso88591.map
install -p -m644 tdtd-font.el tdtd-font.elc \
                 tdtd-font-maker.el \
                 tdtd.el tdtd.elc \
                 $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/
install -p -m644 xxml.el xxml.elc \
    $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/
install -p -m644 ke-docbook.el ke-docbook.elc \
    $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/
install -p -m644 psgml-xpointer.el psgml-xpointer.elc \
    $RPM_BUILD_ROOT%{_prefix}/share/emacs/site-lisp/psgml/
pushd $RPM_BUILD_ROOT%{_infodir}/
  gzip -9f psgml-api.info psgml.info
popd
ln -f tutorial.txt tdtd-tutorial.txt
ln -f readme.txt tdtd-readme.txt
ln -f dot_emacs tdtd.dot.emacs

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/psgml-api.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/psgml-api.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.psgml README.openSUSE
%doc README.xxml THANKS.xxml
%doc suse-start-psgml.el
%doc psgml-jade
%doc tdtd-readme.txt tdtd-tutorial.txt tdtd.dot.emacs
# %config %%{_prefix}/share/emacs/site-lisp/suse-start-psgml.el
%{_prefix}/share/emacs/site-lisp/psgml
%doc %{_infodir}/psgml-api.info*
%doc %{_infodir}/psgml.info*

%changelog
