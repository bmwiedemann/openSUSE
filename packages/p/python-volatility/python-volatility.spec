#
# spec file for package python-volatility
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


Name:           python-volatility
Version:        2.6.1
Release:        0
Summary:        Volatile memory artifact extraction utility framework
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
Url:            http://www.volatilityfoundation.org/
Source:         https://github.com/volatilityfoundation/volatility/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-devel
Requires:       python-distorm3
Requires:       python-pycryptodome
Requires:       python-yara
#used in script vol_genprofile for generation of linux profile
Requires:       libdwarf-tools
Obsoletes:      volatility <= 2.4
Provides:       volatility = %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Volatility Framework is a collection of tools, implemented in
Python for the extraction of digital artifacts from volatile memory
(RAM) samples. The extraction techniques are performed independent of
the system being investigated but offer visibilty into the runtime
state of the system.

%prep
%setup -q -n volatility-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
# this entire install section is setup to mirror what fedora does in its spec file
python setup.py install --root=%{buildroot} --prefix=%{_prefix}
mkdir -p %{buildroot}/%{python_sitelib}/volatility/plugins/contrib
mv %{buildroot}/usr/contrib/plugins/* %{buildroot}/%{python_sitelib}/volatility/plugins/contrib
rm %{buildroot}/usr/contrib/__init__.py
mkdir -p %{buildroot}/%{_datadir}/python-volatility
mv %{buildroot}/usr/contrib/library_example %{buildroot}/%{_datadir}/python-volatility
mkdir -p %{buildroot}/%{_docdir}/python-volatility
mv %{buildroot}/%{_prefix}/tools %{buildroot}/%{_docdir}/python-volatility
mv %{buildroot}/%{_docdir}/python-volatility/tools/vtype_diff.py %{buildroot}/%{_bindir}/

# these are in the fedora spec file, but it is not clear why
#touch %%{buildroot}/%%{python_sitelib}/volatility/plugins/contrib/__init__.py
#touch %%{buildroot}/%%{python_sitelib}/volatility/plugins/contrib/malware/__init__.py
%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS.txt CHANGELOG.txt CREDITS.txt LEGAL.txt LICENSE.txt README.txt
%{python_sitelib}/volatility
%{python_sitelib}/volatility-%{version}-py2.7.egg-info
%{_bindir}/vol.py
%{_bindir}/vtype_diff.py
%{_datadir}/python-volatility
%{_docdir}/python-volatility

%changelog
