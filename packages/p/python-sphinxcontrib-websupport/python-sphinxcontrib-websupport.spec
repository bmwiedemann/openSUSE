#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-sphinxcontrib-websupport%{psuffix}
Version:        1.2.4
Release:        0
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinxcontrib-websupport
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-websupport/sphinxcontrib-websupport-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-docutils
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module Whoosh}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sphinxcontrib-websupport >= %{version}}
%endif
%if 0%{?suse_version} >= 1000 || 0%{?fedora_version} >= 24
Recommends:     python-Sphinx
Suggests:       python-SQLAlchemy
Suggests:       python-Whoosh
Suggests:       python-xapian
%endif
%python_subpackages

%description
sphinxcontrib-webuspport provides a Python API to integrate Sphinx
documentation into your Web application.

%prep
%autosetup -p1 -n sphinxcontrib-websupport-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%dir %{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib/websupport
%{python_sitelib}/sphinxcontrib_websupport-%{version}*-nspkg.pth
%{python_sitelib}/sphinxcontrib_websupport-%{version}*-info
%endif

%changelog
