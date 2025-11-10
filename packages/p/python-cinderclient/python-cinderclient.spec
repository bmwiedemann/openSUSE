#
# spec file for package python-cinderclient
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global pythons %{primary_python}
Name:           python-cinderclient
Version:        9.8.0
Release:        0
Summary:        Python API and CLI for OpenStack Cinder
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-cinderclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-cinderclient/python_cinderclient-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneauth1 >= 5.9.0}
BuildRequires:  %{python_module oslo.serialization}
BuildRequires:  %{python_module oslo.utils >= 4.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.25.1}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-keystoneauth1 >= 5.9.0
Requires:       python-oslo.i18n >= 5.0.1
Requires:       python-oslo.utils >= 4.8.0
Requires:       python-requests >= 2.25.1
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-cinderclient < %{version}
%endif
%python_subpackages

%description
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.

%package -n python-cinderclient-doc
Summary:        Documentation for OpenStack Cinder API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-cinderclient-doc
This is a client for the OpenStack Cinder API (Block Storage. There's a
Python API (the cinderclient module), and a command-line script (cinder).
Each implements 100% of the OpenStack Cinder API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_cinderclient-%{version}

%build
%pyproject_wheel

export PYTHONPATH=.
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

# man page
install -p -D -m 644 doc/build/man/cinder.1 %{buildroot}%{_mandir}/man1/cinder.1
# bash completion
install -p -D -m 644 tools/cinder.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%check
rm cinderclient/tests/unit/test_shell.py
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/cinderclient
%{python_sitelib}/python_cinderclient-%{version}.dist-info
%{_bindir}/cinder
%{_mandir}/man1/cinder.1*
%{_sysconfdir}/bash_completion.d/cinder.bash_completion

%files -n python-cinderclient-doc
%license LICENSE
%doc doc/build/html

%changelog
