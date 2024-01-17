#
# spec file for package xslide
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


Name:           xslide
Version:        0.2.2
Release:        0
Summary:        XSL Integrated Development Environment
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
Url:            http://www.menteith.com/xslide/
Source:         http://downloads.sf.net/xslide/xslide-%version.tar.gz
Source1:        xslide-README.openSUSE
Source10:       COPYING
Patch1:         suse-start-xslide.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  emacs-nox
Requires:       emacs_program
Requires:       psgml

%description
An Emacs mode to edit XSL files.

%prep
%setup -q
%patch1 -p 1
cp %{S:10} .
cp %{S:1} xslide-README.openSUSE

%build
make xslide

%install
install -dm0755 "%buildroot/usr/share/emacs/site-lisp/xslide" \
                 "%buildroot/%_infodir"
# to avoid timestamp problems, install .el files first.
install -p -m644 *.el "%buildroot/usr/share/emacs/site-lisp/xslide/"
# install -p -m644 suse-start-xslide.el \
#     "%buildroot/usr/share/emacs/site-lisp/suse-start-xslide.el"
install -p -m644 *.el *.elc \
    "%buildroot/usr/share/emacs/site-lisp/xslide"

%files
%defattr(-,root,root)
%doc xslide-README.openSUSE
%doc suse-start-xslide.el
%doc TODO README.TXT NEWS dot_emacs
%doc COPYING
%doc xslide-initial.xsl
# %config %_datadir/emacs/site-lisp/suse-start-xslide.el
%_datadir/emacs/site-lisp/xslide

%changelog
