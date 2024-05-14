#
# spec file for package volatility3
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


Name:           volatility3
Version:        2.5.2
Release:        0
Summary:        Volatile memory artifact extraction utility framework
#License:        BSD-2-Clause-Patent and CC-PDDC
License:        BSD-2-Clause-Patent
Group:          Development/Libraries/Python
URL:            https://www.volatilityfoundation.org/
Source:         https://github.com/volatilityfoundation/volatility3/archive/refs/tags/v%{version}.tar.gz#/volatility3-%{version}.tar.gz
# https://github.com/volatilityfoundation/volatility3/archive/refs/tags/v2.4.1.tar.gz
#Patch0:         python-volality-2.6.1_fixbuild.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  pkgconfig(python3)
Requires:       capstone >= 3.0.0
Requires:       python3-distorm3
Requires:       python3-pefile >= 2017.8.1
Requires:       python3-pycryptodome
Requires:       python3-yara >= 3.8.0
#used in script vol_genprofile for generation of linux profile
#Requires:       libdwarf-tools
# this package previously cmade the RPM volatility3, now it is python38-volatility3 (etc)
Obsoletes:      volatility3 < %{version}
Provides:       volatility3 = %{version}
# volatility was a python 2 release, provides 10.0.0 to ensure all future python 2 releases are obsolete
Obsoletes:      volatility <= 2.4
Provides:       volatility = 10.0.0
# python-volatility was a python 2 release, provides 10.0.0 to ensure all future python 2 release are obsolete
Obsoletes:      python-volatility <= 2.6.1
Provides:       python-volatility = 10.0.0
# python38-volatility was the previous release, which was using %%python_subpackage without much reason
Obsoletes:      python38-volatility <= %{version}
Provides:       python38-volatility = %{version}
BuildArch:      noarch

%description
The Volatility Framework is a collection of tools, implemented in
Python for the extraction of digital artifacts from volatile memory
(RAM) samples. The extraction techniques are performed independent of
the system being investigated but offer visibilty into the runtime
state of the system.

%prep
%setup -q
sed -i 's/\r//' doc/make.bat

%build
export CFLAGS="%{optflags}"
%python3_pyproject_wheel

%install
# this entire install section is setup to mirror what fedora does in its spec file
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
# Test require downloading Windows ISO image, not something we would like to do.

%files
%license LICENSE.txt
%doc doc README.md
%{python3_sitelib}/volatility3
%{python3_sitelib}/volatility3-%{version}*-info
%{_bindir}/vol
%{_bindir}/volshell

%changelog
