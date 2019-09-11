#
# spec file for package gnome-doc-utils
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


Name:           gnome-doc-utils
Version:        0.20.10
Release:        0
Summary:        A Collection of Documentation Utilities for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source:         http://download.gnome.org/sources/gnome-doc-utils/0.20/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-doc-utils-fig-path.patch bgo#682776 dimstar@opensuse.org -- Fix linking of figs in subfolders.
Patch0:         gnome-doc-utils-fig-path.patch
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libxml2-python
# needed for xmllint
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
Requires:       libxslt
Recommends:     %{name}-lang
BuildArch:      noarch

%description
The gnome-doc-utils package is a collection of documentation utilities
for the GNOME project. Notably, it contains utilities for building
documentation and all auxiliary files in your source tree. It also
contains the DocBook XSLT stylesheets that were once distributed with
Yelp.

%package -n xml2po
Summary:        Tool to extract translatable content from XML documents
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Requires:       libxml2-python

%description -n xml2po
xml2po is a simple Python program which extracts translatable
content from free-form XML documents and outputs gettext compatible
POT files.

%package devel
Summary:        A Collection of Documentation Utilities for GNOME
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
# For the validation with xsltproc to use a local DTD
Requires:       docbook_4
Requires:       xml2po-devel

%description devel
The gnome-doc-utils package is a collection of documentation utilities
for the GNOME project. Notably, it contains utilities for building
documentation and all auxiliary files in your source tree. It also
contains the DocBook XSLT stylesheets that were once distributed with
Yelp.

%package -n xml2po-devel
Summary:        Tool to extract translatable content from XML documents
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Requires:       xml2po = %{version}

%description -n xml2po-devel
xml2po is a simple Python program which extracts translatable
content from free-form XML documents and outputs gettext compatible
POT files.

%lang_package

%prep
%setup -q
%patch0 -p1
translation-update-upstream

%build
%configure\
	--disable-scrollkeeper
make %{?_smp_mflags} pkgconfigdir=%{_datadir}/pkgconfig

%install
%make_install pkgconfigdir=%{_datadir}/pkgconfig
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
%find_lang %{name} %{?no_lang_C}
%find_lang gnome-doc-make %{?no_lang_C} %{name}.lang
%find_lang gnome-doc-xslt %{?no_lang_C} %{name}.lang
%fdupes %{buildroot}

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
%{python_sitelib}/xml2po
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
