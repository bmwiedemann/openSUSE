#
# spec file for package itstool
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


Name:           itstool
Version:        2.0.6
Release:        0
Summary:        Tool to translate XML documents using PO files
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://itstool.org
Source:         http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2

BuildRequires:  python3-base
%if 0%{?sle_version}
BuildRequires:  python3-libxml2-python
Requires:       python3-libxml2-python
%else
BuildRequires:  python3-libxml2
Requires:       python3-libxml2
%endif
BuildArch:      noarch

%description
ITS Tool extracts messages from XML files and outputs PO template files, then
merges translations from MO files to create translated XML files. It determines
what to translate and how to chunk it into messages using the W3C
Internationalization Tag Set (ITS).

%prep
%setup -q

%build
sed -i -e "/^echo.*import/s/python/python3/" configure
export PYTHON=%{_bindir}/python3
%configure
make %{?_smp_mflags}

%install
%make_install PYTHON=%{_bindir}/python3

%files
%license COPYING
%doc ChangeLog NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/itstool.1%{?ext_man}

%changelog
