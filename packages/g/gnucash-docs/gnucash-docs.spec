#
# spec file for package gnucash-docs
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gnucash-docs
Version:        4.13
Release:        9.1
Summary:        Documentation Module for GnuCash
License:        GFDL-1.1-only AND GPL-2.0-or-later
Group:          Productivity/Office/Finance
URL:            https://www.gnucash.org/
Source:         https://sourceforge.net/projects/gnucash/files/gnucash%20(stable)/%{version}/gnucash-docs-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  sgml-skel
BuildRequires:  xsltproc
BuildArch:      noarch
Recommends:     %{_bindir}/gnome-help

%description
GnuCash is a personal finance manager. A check-book like register GUI
allows you to enter and track bank accounts, stocks, income and even
currency trades. The interface is designed to be simple and easy to
use, but is backed with double-entry accounting principles to ensure
balanced books. This is the documentation module for GnuCash.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang gnucash-guide %{?no_lang_C}
%find_lang gnucash-help %{?no_lang_C}
%{__rm} -rf %{buildroot}%{_datadir}/gnucash-docs
%fdupes %{buildroot}%{_datadir}

%files -f gnucash-guide.lang -f gnucash-help.lang
%license COPYING
%doc AUTHORS COPYING-DOCS NEWS README
%doc %{_datadir}/help/C/gnucash-guide
%doc %{_datadir}/help/C/gnucash-help

%changelog
