#
# spec file for package waf
#
# Copyright (c) 2023 SUSE LLC
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


Name:           waf
Version:        2.0.25
Release:        0
Summary:        The Waf build system
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://waf.io
Source:         https://gitlab.com/ita1024/waf/-/archive/waf-%{version}/waf-waf-%{version}.tar.bz2
BuildRequires:  python3-base
BuildArch:      noarch

%description
Waf is a Python-based framework for configuring, compiling and installing applications.

%prep
%setup -q -n waf-waf-%{version}
find ./waflib -iname \*py -print -exec sed -i -e '1{ s/#!.*/#!foo/ }' '{}' \;

%build
python3 ./waf-light configure build
# Unpack waflib
python3 -c "import zipfile; z = zipfile.ZipFile('./zip/waflib.zip'); z.extractall(path='./zip/')"

cat <<EOF > ./waf.wrapper
#!/usr/bin/python3
import os, sys;
cwd = os.getcwd()
wafdir = "%{_datadir}/waf/"
sys.path.insert(0, wafdir)

if __name__ == '__main__':
	from waflib import Scripting
	Scripting.waf_entry_point(cwd, "%{version}", wafdir)
EOF

%install
install -m 755 -D waf.wrapper %{buildroot}%{_bindir}/waf
install -m 755 -d %{buildroot}%{_datadir}/waf/
cp -pR ./zip/waflib %{buildroot}%{_datadir}/waf/

%check
export PYTHONPATH=%{buildroot}/%{_datadir}/waf/
%{buildroot}/%{_bindir}/waf -h

%files
%doc README.md
%{_bindir}/waf
%{_datadir}/waf

%changelog
