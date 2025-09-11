#
# spec file for package python-pyvo
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


Name:           python-pyvo
Version:        1.7
Release:        0
Summary:        Astropy affiliated package for accessing Virtual Observatory data and services
License:        BSD-3-Clause
URL:            https://github.com/astropy/pyvo
Source:         https://files.pythonhosted.org/packages/source/p/pyvo/pyvo-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-astropy-header}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-remotedata}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
# /SECTION
BuildRequires:  fdupes
Requires:       python-astropy >= 4.1
Requires:       python-requests
Suggests:       python-pillow
Suggests:       python-sphinx-astropy
Suggests:       python-pytest-astropy
Suggests:       python-requests-mock
BuildArch:      noarch
%python_subpackages

%description
Astropy affiliated package for accessing Virtual Observatory data and services

%prep
%setup -q -n pyvo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Custom configuration to add current directory to sys.path when running tests
cat << EOF > pytest.ini
[pytest]
path = "."
EOF

%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pyvo
%{python_sitelib}/pyvo-%{version}.dist-info

%changelog
