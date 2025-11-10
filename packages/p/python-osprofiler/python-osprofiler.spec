#
# spec file for package python-osprofiler
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


Name:           python-osprofiler
Version:        4.3.0
Release:        0
Summary:        OpenStack Profiler Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/osprofiler
Source0:        https://files.pythonhosted.org/packages/source/o/osprofiler/osprofiler-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.2}
BuildRequires:  %{python_module WebOb >= 1.7.1}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module opentelemetry-exporter-otlp}
BuildRequires:  %{python_module oslo.concurrency >= 3.26.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.log}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-WebOb >= 1.7.1
Requires:       python-importlib-metadata
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.log
Requires:       python-oslo.utils >= 3.33.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-osprofiler < %{version}
%else
Conflicts:      python3-osprofiler < %{version}
%endif
%python_subpackages

%description
OSProfiler provides a tiny but powerful library that is used by
most (soon to be all) OpenStack projects and their python clients. It
provides functionality to be able to generate 1 trace per request, that goes
through all involved services. This trace can then be extracted and used
to build a tree of calls which can be quite handy for a variety of
reasons (for example in isolating cross-project performance issues).

%package -n python-osprofiler-doc
Summary:        Documentation for OSProfiler
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-osprofiler-doc
Documentation for OSProfiler.

%prep
%autosetup -p1 -n osprofiler-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/osprofiler

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%pre
%python_libalternatives_reset_alternative osprofiler

%post
%python_install_alternative osprofiler

%postun
%python_uninstall_alternative osprofiler

%check
# otherwise causes import error
rm osprofiler/tests/unit/drivers/test_jaeger.py
rm -rf osprofiler/tests/functional
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/osprofiler
%{python_sitelib}/osprofiler
%{python_sitelib}/osprofiler-%{version}.dist-info

%files -n python-osprofiler-doc
%license LICENSE
%doc doc/build/html

%changelog
