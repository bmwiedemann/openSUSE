#
# spec file for package python-manuel
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013-2018 LISA GmbH, Bingen, Germany.
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


%{?sle15allpythons}
Name:           python-manuel
Version:        1.13.0
Release:        0
Summary:        Python module to build tested documentation
License:        Apache-2.0
URL:            https://pypi.org/project/manuel/
# SourceRepository: https://github.com/benji-york/manuel
Source:         https://files.pythonhosted.org/packages/source/m/manuel/manuel-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?suse_version} >= 1600
# SECTION Documentation requirements:
BuildRequires:  python3-Sphinx
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinxcontrib-copybutton
# /SECTION
%endif
# SECTION Testing requirements:
BuildRequires:  %{python_module zope.testing}
# /SECTION
%python_subpackages

%description
Manuel lets the user build tested documentation.

Documentation, a full list of included plug-ins, and examples are available
with the -doc package and at http://packages.python.org/manuel/.

%package        doc
Summary:        Build tested documentation

%description    doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n manuel-%{version}

%build
%pyproject_wheel
%if 0%{?suse_version} >= 1600
sphinx-build -c sphinx/ -a src/manuel docs/
rm docs/.buildinfo
%endif

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if 0%{?suse_version} >= 1600
%{python_expand #
mkdir -p %{buildroot}%{_docdir}/%{$python_prefix}-manuel-doc
cp -r docs/* %{buildroot}%{_docdir}/%{$python_prefix}-manuel-doc
%fdupes %{buildroot}%{_docdir}/%{$python_prefix}-manuel-doc
}
%endif

%check
%pytest src/manuel/tests.py

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst COPYRIGHT.rst PKG-INFO README.rst
%{python_sitelib}/manuel
%{python_sitelib}/manuel-%{version}.dist-info

%if 0%{?suse_version} >= 1600
%files %{python_files doc}
%doc %{_docdir}/%{python_prefix}-manuel-doc
%endif

%changelog
