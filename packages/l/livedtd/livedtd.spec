#
# spec file for package livedtd
#
# Copyright (c) 2025 SUSE LLC
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


Name:           livedtd
URL:            http://www.sagehill.net/livedtd/
Group:          Productivity/Publishing/XML
License:        BSD-3-Clause
Summary:        DTD Visualizing Tool
Version:        2007.1.15
Release:        0
Source0:        http://www.sagehill.net/livedtd/downloads/%{name}.tar.gz
Patch0:         livedtd-catalog.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The package comes with a Perl script (livedtd.pl) that converts an SGML
or XML DTD (Document Type Definition) into an HTML document.  The HTML
document is exactly the same text as the DTD but with "live" links that
let you navigate through the DTD.



Authors:
--------
    Robert Stayton <bobs@sagehill.net>

%prep
%setup -q -c -n %{name}
%patch -P 0 -p 1 -b .catalog

%install
if [ -n $RPM_BUILD_ROOT ]; then
  rm -fr $RPM_BUILD_ROOT
  install -d $RPM_BUILD_ROOT
fi
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
  $RPM_BUILD_ROOT%{_bindir}
cp -a OASIS $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 *.pl $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-, root, root)
%doc README
%{_bindir}/*
%{_datadir}/%{name}

%changelog
