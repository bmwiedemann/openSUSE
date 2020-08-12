#
# spec file for package volatility3
#
# Copyright (c) 2020 SUSE LLC
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


Name:           volatility3
Version:        1.0.0+beta.1
Release:        0
Summary:        Volatile memory artifact extraction utility framework
#License:        BSD-2-Clause-Patent and CC-PDDC
License:        BSD-2-Clause-Patent
Group:          Development/Libraries/Python
URL:            http://www.volatilityfoundation.org/
Source:         https://github.com/volatilityfoundation/volatility3/archive/v1.0.0-beta.1.tar.gz
#Patch0:         python-volality-2.6.1_fixbuild.patch
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3)
Requires:       python3-distorm3
Requires:       python3-pycryptodome
Requires:       python3-yara
#used in script vol_genprofile for generation of linux profile
#Requires:       libdwarf-tools

# volatility was a python 2 release, provides 10.0.0 to ensure all future python 2 releases are obsolete
Obsoletes:      volatility <= 2.4
Provides:       volatility = 10.0.0

# python-volatility was a python 2 release, provides 10.0.0 to ensure all future python 2 release are obsolete
Obsoletes:      python-volatility <= 2.6.1
Provides:       python-volatility = 10.0.0

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Volatility Framework is a collection of tools, implemented in
Python for the extraction of digital artifacts from volatile memory
(RAM) samples. The extraction techniques are performed independent of
the system being investigated but offer visibilty into the runtime
state of the system.

%prep
%setup -q -n volatility3-1.0.0-beta.1
sed -i 's/\r//' README.txt
sed -i 's/\r//' doc/make.bat

%build
env CFLAGS="%{optflags}" python3 setup.py build

%install
# this entire install section is setup to mirror what fedora does in its spec file
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
%fdupes %{buildroot}

%files
%defattr(-,root,root)
%license LICENSE.txt
%doc doc README.txt
%{python3_sitelib}/volatility
%{python3_sitelib}/volatility-1.0.0b1-py3.8.egg-info
%{python3_sitelib}/development
/usr/bin/vol
/usr/bin/volshell

%changelog
