#
# spec file for package itstool
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.0.7
Release:        0
Summary:        Tool to translate XML documents using PO files
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            http://itstool.org
Source:         http://files.itstool.org/itstool/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM 32c7d07664dc37765100285d1202d488cd6a27e8.patch -- Fix insufficiently quoted regular expressions
Patch:          https://github.com/itstool/itstool/commit/32c7d07664dc37765100285d1202d488cd6a27e8.patch
# PATCH-FIX-UPSTREAM itstool-2.0.7-lxml.patch -- port to lxml boo#1259023
Patch2:         itstool-2.0.7-lxml.patch
# for itstool-2.0.7-lxml.patch
BuildRequires:  autoconf
BuildRequires:  automake
#
BuildRequires:  python3-base
BuildRequires:  python3-lxml
Requires:       python3-lxml
BuildArch:      noarch

%description
ITS Tool extracts messages from XML files and outputs PO template files, then
merges translations from MO files to create translated XML files. It determines
what to translate and how to chunk it into messages using the W3C
Internationalization Tag Set (ITS).

%prep
%autosetup -p1

%build
# for itstool-2.0.7-lxml.patch
autoreconf -fiv
export PYTHON=$(realpath %{_bindir}/python3)
%configure
%make_build

%install
%make_install PYTHON=$(realpath %{_bindir}/python3)

%files
%license COPYING
%doc ChangeLog NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/itstool.1%{?ext_man}

%changelog
