#
# spec file for package emacs-color-theme
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           emacs-color-theme
Version:        6.6.0
Release:        0
Summary:        Color themes for emacs
License:        GPL-2.0+
Group:          Productivity/Text/Editors
URL:            http://www.nongnu.org/color-theme/
Source0:        http://download.savannah.gnu.org/releases/color-theme/color-theme-6.6.0.tar.gz
Patch1:         make.patch
BuildRequires:  emacs-nox
BuildRequires:  makeinfo
Requires:       emacs
BuildArch:      noarch

%define _sitedir %{_datadir}/emacs/site-lisp
%define _lispdir %{_sitedir}/color-theme

%description 
Emacs Color Themes is an add-on package for GNU Emacs.
It provides several different color themes to skin your Emacs greatly
improving the editing experience. 

%prep
%setup -n color-theme-%{version}
%patch -p1 -P 1

%build
make %{?_smp_mflags}
make autoloads %{?_smp_mflags}

%install
install -pm 755 -d %{buildroot}%{_lispdir}
install -pm 644 *.el %{buildroot}%{_lispdir}/
install -pm 644 *.elc %{buildroot}%{_lispdir}/
install -pm 755 -d %{buildroot}%{_lispdir}/themes
install -pm 644 themes/*.el %{buildroot}%{_lispdir}/themes/
install -pm 644 themes/*.elc %{buildroot}%{_lispdir}/themes/

%files 
%doc README AUTHORS COPYING HACKING
%{_lispdir}/
%{_lispdir}/themes/

%changelog

