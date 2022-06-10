#
# spec file for package volatility3
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
%define skip_python2 1

%if 0%{?suse_version} > 1540
# For reashons unknown to me, this spec file only works if only one python version is targetted.
# Choosing python38 as I have tested it the most.
# opensuse releases 15.4 and before only target one python version so don't need this define.
%define pythons python38
%endif

Name:           volatility3
Version:        2.0.1
Release:        0
Summary:        Volatile memory artifact extraction utility framework
#License:        BSD-2-Clause-Patent and CC-PDDC
License:        BSD-2-Clause-Patent
Group:          Development/Libraries/Python
URL:            http://www.volatilityfoundation.org/
Source:         v%{version}.tar.gz
#Patch0:         python-volality-2.6.1_fixbuild.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
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

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%python_subpackages

%description
The Volatility Framework is a collection of tools, implemented in
Python for the extraction of digital artifacts from volatile memory
(RAM) samples. The extraction techniques are performed independent of
the system being investigated but offer visibilty into the runtime
state of the system.

%prep
%setup -q -n %{name}-%{version}
sed -i 's/\r//' doc/make.bat

%build
env CFLAGS="%{optflags}" python3 setup.py build

%install
# this entire install section is setup to mirror what fedora does in its spec file
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
%fdupes %{buildroot}

%files %{python_files}
%defattr(-,root,root)
%license LICENSE.txt
%doc doc README.md
%{python3_sitelib}/volatility*
/usr/bin/vol
/usr/bin/volshell

%changelog
