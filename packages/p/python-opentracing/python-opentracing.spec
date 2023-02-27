#
# spec file for package python-opentracing
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-opentracing
Version:        2.4.0
Release:        0
Summary:        OpenTracing API for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/opentracing/opentracing-python
Source:         https://files.pythonhosted.org/packages/source/o/opentracing/opentracing-%{version}.tar.gz
# https://github.com/opentracing/opentracing-python/issues/156
Patch0:         python-opentracing-no-mock.patch
Patch1:         pr_159.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-gevent
Suggests:       python-tornado
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tornado}
# /SECTION
%python_subpackages

%description
OpenTracing API for Python.
See documentation at http://opentracing.io

%prep
%setup -q -n opentracing-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/opentracing
%{python_sitelib}/opentracing-%{version}*-info

%changelog
