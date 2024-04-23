#
# spec file for package python-gunicorn
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-gunicorn%{psuffix}
Version:        22.0.0
Release:        0
Summary:        WSGI HTTP Server for UNIX
License:        MIT
Group:          Development/Languages/Python
URL:            https://gunicorn.org
Source:         https://files.pythonhosted.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-evenlet
Suggests:       python-gevent
Suggests:       python-gthread
Suggests:       python-setproctitle
Suggests:       python-tornado
BuildArch:      noarch
%if 0%{?sle_version} >= 150500
# Fixes the build on Leap
BuildRequires:  %{python_module Sphinx}
%else
BuildRequires:  python3-Sphinx
%endif
%if %{with test}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module gevent >= 1.4}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks.

%if 0%{?suse_version} > 1500
%package -n python-gunicorn-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module gunicorn-doc = %{version}}

%description -n python-gunicorn-doc
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks.

This package contains the documentation.
%endif

%prep
%setup -q -n gunicorn-%{version}
# remove version pinning for test requirements
sed -i 's/==.*//' requirements_test.txt
sed -i -e '/cover/d' requirements_test.txt
# do not check coverage
sed -i -e 's/--cov[^ ]*//' -e 's/--cov-report[^ ]*//' setup.cfg
%autopatch -p1

%if %{with test}
%check
%pytest

%else  # without test

%build
%pyproject_wheel
sphinx-build -b html -d docs/build/doctrees docs/source docs/build/html

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gunicorn
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gunicorn

%postun
%python_uninstall_alternative gunicorn

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/gunicorn
%{python_sitelib}/gunicorn
%{python_sitelib}/gunicorn-%{version}*-info

%if 0%{?suse_version} > 1500
%files -n python-gunicorn-doc
%license LICENSE
%endif
%doc README.rst NOTICE THANKS docs/build/html docs/source/news.rst
%endif

%changelog
