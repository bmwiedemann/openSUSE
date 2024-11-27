#
# spec file for package gnome-doc-utils
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


Name:           gnome-doc-utils
Version:        0.20.10
Release:        0
Summary:        A Collection of Documentation Utilities for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-doc-utils/0.20/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-doc-utils-fig-path.patch bgo#682776 dimstar@opensuse.org -- Fix linking of figs in subfolders.
Patch0:         gnome-doc-utils-fig-path.patch
# PATCH-FIX-UPSTREAM gnome-doc-utils-port-python3.patch -- Port to python3
Patch1:         gnome-doc-utils-port-python3.patch

BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
%if %suse_version > 1500
BuildRequires:  python3-libxml2
BuildRequires:  python3-setuptools
%else
BuildRequires:  python3-libxml2-python
%endif
# needed for xmllint
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
Requires:       libxslt
%if %suse_version > 1500
Requires:       python3-libxml2
%else
Requires:       python3-libxml2-python
%endif
BuildArch:      noarch

%description
The gnome-doc-utils package is a collection of documentation
utilities for the GNOME project. It contains utilities for building
documentation and auxiliary files in a source tree. It also contains
the DocBook XSLT stylesheets that were once distributed with Yelp.

%package -n xml2po
Summary:        Tool to extract translatable content from XML documents
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
%if %suse_version > 1500
BuildRequires:  python3-libxml2
%else
BuildRequires:  python3-libxml2-python
%endif

%description -n xml2po
xml2po is a Python program which extracts translatable content from
free-form XML documents and outputs gettext compatible POT files.

%package devel
Summary:        A Collection of Documentation Utilities for GNOME
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# For the validation with xsltproc to use a local DTD
Requires:       docbook_4
Requires:       xml2po-devel

%description devel
The gnome-doc-utils package is a collection of documentation
utilities for the GNOME project. It contains utilities for building
documentation and auxiliary files in a source tree. It also contains
the DocBook XSLT stylesheets that were once distributed with Yelp.

%package -n xml2po-devel
Summary:        Pkgconfig file for xml2po
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Requires:       xml2po = %{version}

%description -n xml2po-devel
xml2po is a Python program which extracts translatable content from
free-form XML documents and outputs gettext compatible POT files.

%lang_package

%prep
%autosetup -p1

%build
export LANG=C.UTF-8
%configure \
	--disable-scrollkeeper \
	%{nil}
%make_build pkgconfigdir=%{_datadir}/pkgconfig

%install
%make_install pkgconfigdir=%{_datadir}/pkgconfig
%find_lang %{name} %{?no_lang_C}
%find_lang gnome-doc-make %{?no_lang_C} %{name}.lang
%find_lang gnome-doc-xslt %{?no_lang_C} %{name}.lang
%fdupes %{buildroot}/%{_prefix}
%python3_fix_shebang

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/gnome-doc-make/
%doc %{_datadir}/gnome/help/gnome-doc-make/C/
%dir %{_datadir}/gnome/help/gnome-doc-xslt/
%doc %{_datadir}/gnome/help/gnome-doc-xslt/C/
%{_bindir}/gnome-doc-tool
%dir %{_datadir}/gnome-doc-utils
%{_datadir}/gnome-doc-utils/icons
%{_datadir}/gnome-doc-utils/watermarks
%{_datadir}/xml/gnome
%{_datadir}/xml/mallard

%files -n xml2po
%license xml2po/COPYING
%doc xml2po/AUTHORS xml2po/ChangeLog xml2po/NEWS xml2po/README
%{_bindir}/xml2po
%{python3_sitelib}/xml2po
%{_mandir}/man?/xml2po*%{ext_man}

%files devel
%{_bindir}/gnome-doc-prepare
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gnome-doc-utils.m4
%{_datadir}/pkgconfig/gnome-doc-utils.pc
%{_datadir}/gnome-doc-utils/gnome-doc-utils.make
%{_datadir}/gnome-doc-utils/templates
%{_datadir}/gnome-doc-utils/template*.*

%files -n xml2po-devel
%{_datadir}/pkgconfig/xml2po.pc

%files lang -f %{name}.lang

%changelog
