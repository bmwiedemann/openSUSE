#
# spec file for package python-oslo.concurrency
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


Name:           python-oslo.concurrency
Version:        7.2.0
Release:        0
Summary:        OpenStack oslo.concurrency library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.concurrency
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-concurrency/oslo_concurrency-%{version}.tar.gz
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fasteners >= 0.7.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-fasteners >= 0.7.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.concurrency < %{version}
%else
Conflicts:      python3-oslo.concurrency < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package -n python-oslo.concurrency-doc
Summary:        Documentation for OpenStack concurrency library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.concurrency-doc
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo_concurrency-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/lockutils-wrapper

%pre
%python_libalternatives_reset_alternative lockutils-wrapper

%post
%python_install_alternative lockutils-wrapper

%postun
%python_uninstall_alternative lockutils-wrapper

%check
env TEST_EVENTLET=0 %{openstack_stestr_run}
env TEST_EVENTLET=1 %{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%python_alternative %{_bindir}/lockutils-wrapper
%{python_sitelib}/oslo_concurrency
%{python_sitelib}/oslo_concurrency-%{version}.dist-info

%files -n python-oslo.concurrency-doc
%license LICENSE
%doc doc/build/html

%changelog
