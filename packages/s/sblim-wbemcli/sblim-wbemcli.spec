#
# spec file for package sblim-wbemcli
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sblim-wbemcli
%if 0%{?suse_version} > 1010
BuildRequires:  binutils-devel
%else
# SLE_10
BuildRequires:  binutils
%endif
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
Version:        1.6.3
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://sblim.wiki.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-wbemcli-allow-tls.patch
Summary:        SBLIM WBEM Command Line Interface
License:        EPL-1.0
Group:          System/Management

%description
WBEM Command Line Interface is a standalone, command line WBEM client.
It is especially suited for basic systems management tasks as it can be
used in scripts.



Authors:
--------
    SBLIM Project <http://www-124.ibm.com/sblim/>

%prep
%setup -q
%patch0 -p1

sed -i 's|wbemcli/samples|wbemcli/examples|' man/wbemcli.1.pre.in
sed -i 's|wbemcli/samples|wbemcli/examples|' man/wbemcli.1

%build
%configure
make %{?jobs:-j %jobs}

%install
%makeinstall
mv "samples" "examples"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README* NEWS examples/ *py
%{_bindir}/wbem*
%{_mandir}/man1/wbemcli.1.gz

%changelog
