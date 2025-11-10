#
# spec file for package python-debtcollector
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


Name:           python-debtcollector
Version:        3.0.0
Release:        0
Summary:        A collection of Python deprecation patterns and strategies
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/debtcollector/latest/
Source0:        https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-3.0.0.tar.gz
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wrapt >= 1.7.0}
BuildRequires:  openstack-macros
Requires:       python-importlib-metadata
Requires:       python-pbr
Requires:       python-wrapt >= 1.7.0
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-debtcollector < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

%package -n python-debtcollector-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-debtcollector-doc
A collection of Python deprecation patterns and strategies that help
you collect your technical debt in a non-destructive manner. The goal
of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand
into a larger set of patterns as time goes on. The desired output of
these patterns is to apply the warnings module to emit
DeprecationWarning or PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about
future deprecations.

This package contains documentation in HTML format.

%prep
%autosetup -p1 -n debtcollector-3.0.0

%build
%pyproject_wheel

# generate html doc
PBR_VERSION=3.0.0 %{sphinx_build} -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%pytest

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/debtcollector
%{python_sitelib}/debtcollector-%{version}.dist-info

%files -n python-debtcollector-doc
%license LICENSE
%doc doc/build/html

%changelog
