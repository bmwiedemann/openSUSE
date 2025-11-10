#
# spec file for package python-pyghmi
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


Name:           python-pyghmi
Version:        1.6.6
Release:        0
Summary:        General Hardware Management Initiative (IPMI and others)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/pyghmi
Source0:        https://files.pythonhosted.org/packages/source/p/pyghmi/pyghmi-%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 2.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
Requires:       python-cryptography >= 2.1
Requires:       python-python-dateutil >= 2.8.1
Requires:       python-six
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-pyghmi < %{version}
%else
Conflicts:      python3-pyghmi < %{version}
%endif
%python_subpackages

%description
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%package -n python-pyghmi-doc
Summary:        General Hardware Management Initiative (IPMI and others) -- Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-pyghmi-doc
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%prep
%autosetup -p1 -n pyghmi-%{version}

%build
%pyproject_wheel
PYTHONPATH=. PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/pyghmicons
%python_clone -a %{buildroot}%{_bindir}/pyghmiutil
%python_clone -a %{buildroot}%{_bindir}/virshbmc
%python_clone -a %{buildroot}%{_bindir}/fakebmc

%pre
%python_libalternatives_reset_alternative pyghmicons
%python_libalternatives_reset_alternative pyghmiutil
%python_libalternatives_reset_alternative fakebmc
%python_libalternatives_reset_alternative virshbmc

%post
%python_install_alternative pyghmicons
%python_install_alternative pyghmiutil
%python_install_alternative fakebmc
%python_install_alternative virshbmc

%postun
%python_uninstall_alternative pyghmicons
%python_uninstall_alternative pyghmiutil
%python_uninstall_alternative fakebmc
%python_uninstall_alternative virshbmc

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyghmicons
%python_alternative %{_bindir}/pyghmiutil
%python_alternative %{_bindir}/virshbmc
%python_alternative %{_bindir}/fakebmc
%{python_sitelib}/pyghmi
%{python_sitelib}/pyghmi-%{version}.dist-info

%files -n python-pyghmi-doc
%doc doc/build/html
%license LICENSE

%changelog
