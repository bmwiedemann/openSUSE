#
# spec file for package gnucash-docs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gnucash-docs
Version:        3.10
Release:        0
Summary:        Documentation Module for GnuCash
License:        GFDL-1.1-only AND GPL-2.0-or-later
Group:          Productivity/Office/Finance
URL:            https://www.gnucash.org/
Source:         https://sourceforge.net/projects/gnucash/files/gnucash%20(stable)/%{version}/gnucash-docs-%{version}.tar.gz
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
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang gnucash-guide %{?no_lang_C}
%find_lang gnucash-help %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files -f gnucash-guide.lang -f gnucash-help.lang
%license COPYING
%doc AUTHORS COPYING-DOCS HACKING NEWS README
# Own dirs so we do not have to depend on libgnome
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/help
%dir %{_datadir}/gnome/help/gnucash-guide
%doc %{_datadir}/gnome/help/gnucash-guide/C/
%dir %{_datadir}/gnome/help/gnucash-help
%doc %{_datadir}/gnome/help/gnucash-help/C/

%changelog
