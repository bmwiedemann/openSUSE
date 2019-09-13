#
# spec file for package python-ZEO
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
%define         oldpython python
Name:           python-ZEO
Version:        5.2.1
Release:        0
Summary:        Client-Server storage implementation for ZODB
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/ZEO
Source:         https://files.pythonhosted.org/packages/source/Z/ZEO/ZEO-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module ZConfig}
BuildRequires:  %{python_module ZODB >= 5.5.1}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module random2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module transaction >= 2.0.3}
BuildRequires:  %{python_module zc.lockfile}
BuildRequires:  %{python_module zdaemon}
BuildRequires:  %{python_module zodbpickle >= 0.6.0}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
BuildRequires:  python-trollius
Requires:       python-ZConfig
Requires:       python-ZODB >= 5.5.1
Requires:       python-persistent >= 4.1.0
Requires:       python-six
Requires:       python-transaction >= 2.0.3
Requires:       python-zc.lockfile
Requires:       python-zdaemon
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       %{oldpython}-trollius
%endif
%python_subpackages

%description
ZEO provides a client-server storage implementation for ZODB.

%package     -n %{name}-doc
Summary:        Client-Server storage implementation for ZODB
Group:          Development/Languages/Python
Provides:       %{python_module ZEO-doc = %{version}}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n ZEO-%{version}
# delete backup files
find . -name "*~" -print -delete
# remove unwanted shebang
find src -name "*.py" | xargs sed -i '1 { /^#!/ d }'
rm -rf src/ZEO.egg-info
# do not hardcode version
sed -i -e 's:msgpack < 0.6:msgpack:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/runzeo
%python_clone -a %{buildroot}%{_bindir}/zeoctl
%python_clone -a %{buildroot}%{_bindir}/zeopack
%python_clone -a %{buildroot}%{_bindir}/zeo-nagios

%check
%python_exec setup.py test

%post
%python_install_alternative runzeo zeoctl zeopack zeo-nagios

%postun
%python_uninstall_alternative runzeo

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%python_alternative %{_bindir}/runzeo
%python_alternative %{_bindir}/zeoctl
%python_alternative %{_bindir}/zeopack
%python_alternative %{_bindir}/zeo-nagios
%{python_sitelib}/ZEO
%{python_sitelib}/ZEO-%{version}-py%{python_version}.egg-info

%changelog
