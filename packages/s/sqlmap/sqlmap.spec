#
# spec file for package sqlmap
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           sqlmap
Version:        1.6.12
Release:        0
Summary:        Automatic SQL injection and database takeover tool
License:        GPL-2.0-or-later
URL:            https://github.com/sqlmapproject/sqlmap
Source:         https://github.com/sqlmapproject/sqlmap/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix_shebang.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3
BuildArch:      noarch

%description

sqlmap is an open source penetration testing tool that automates the process of
detecting and exploiting SQL injection flaws and taking over of database
servers. It comes with a powerful detection engine, many niche features for the
ultimate penetration tester, and a broad range of switches including database
fingerprinting, over data fetching from the database, accessing the underlying
file system, and executing commands on the operating system via out-of-band
connections.

%prep
%setup -q -n sqlmap-%{version}
%patch0 -p1
find extra lib plugins tamper thirdparty -iname "*.py" -exec sed -i '1{/^#!/ d}' {} \;
find extra lib plugins tamper thirdparty -iname "*.pl" -exec sed -i '1{/^#!/ d}' {} \;
mv extra/icmpsh/icmpsh-m.c extra/icmpsh/icmpsh-m.c.txt
mv extra/icmpsh/icmpsh-s.c extra/icmpsh/icmpsh-s.c.txt
mv extra/runcmd/src/runcmd/runcmd.cpp extra/runcmd/src/runcmd/runcmd.cpp.txt
mv extra/runcmd/src/runcmd/stdafx.cpp extra/runcmd/src/runcmd/stdafx.cpp.txt
mv extra/runcmd/src/runcmd/stdafx.h extra/runcmd/src/runcmd/stdafx.h.txt
chmod ugo-x extra/shutils/duplicates.py
chmod ugo-x thirdparty/identywaf/identYwaf.py

%build

%install
mkdir -p %{buildroot}%{_datadir}/sqlmap
cp -a * %{buildroot}%{_datadir}/sqlmap

%python_expand %fdupes %{buildroot}%{_datadir}/sqlmap

%post
ln -s -f  %{_datadir}/sqlmap/sqlmap.py %{_bindir}
ln -s -f  %{_datadir}/sqlmap/sqlmapapi.py %{_bindir}

%postun
case "$1" in
  0) # last one out put out the lights
    rm -f %{_bindir}/sqlmap.py
    rm -f %{_bindir}/sqlmapapi.py
  ;;
esac

%files
%{_datadir}/sqlmap

%license %{_datadir}/sqlmap/LICENSE
%doc %{_datadir}/sqlmap/README.md

%changelog
