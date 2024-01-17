#
# spec file for package python-Flask-OpenTracing
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


%define skip_python2 1
Name:           python-Flask-OpenTracing
Version:        1.1.0
Release:        0
Summary:        OpenTracing support for Flask applications
License:        BSD-3-Clause
URL:            https://github.com/opentracing-contrib/python-flask
Source:         https://files.pythonhosted.org/packages/source/F/Flask-OpenTracing/Flask-OpenTracing-%{version}.tar.gz
# PATCH-FIX-UPSTREAM demock.patch gh#opentracing-contrib/python-flask#58 mcepl@suse.com
# Remove dependency on mock
Patch0:         demock.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-opentracing >= 2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module opentracing >= 2.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
OpenTracing support for Flask applications.

%prep
%autosetup -p1 -n Flask-OpenTracing-%{version}

# We don't need coverage
sed -i -e '/--cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# gh#opentracing-contrib/python-flask#57 for TestTracingStartSpanCallback
%pytest -k 'not (test_span_tags or TestTracingStartSpanCallback)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flask_opentracing
%{python_sitelib}/Flask_OpenTracing-%{version}*-info

%changelog
