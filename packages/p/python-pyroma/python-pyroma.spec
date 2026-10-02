#
# spec file for package python-pyroma
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-pyroma
Version:        5.0.1
Release:        0
Summary:        Test a Python project's adherence to packaging guidelines
License:        MIT
URL:            https://github.com/regebro/pyroma
Source:         https://files.pythonhosted.org/packages/source/p/pyroma/pyroma-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#regebro/pyroma#123
Patch0:         no-more-pkg-resources.patch
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module build >= 0.7}
BuildRequires:  %{python_module docutils >= 0.22}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module trove-classifiers >= 2022.6}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-build >= 0.7
Requires:       python-docutils >= 0.22
Requires:       python-packaging
Requires:       python-requests
Requires:       python-setuptools >= 42
Requires:       python-trove-classifiers >= 2022.6
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pyroma is a package that gives a rating of how well a Python project
complies with the best practices of the Python packaging ecosystem,
primarily PyPI, pip, Distribute, etc., as well as a list of issues
that could be improved.

It's written so that there are a library with methods to call from Python, as
well as a script, also called pyroma.

%prep
%autosetup -p1 -n pyroma-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyroma
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# Requires network
donttest="test_complete or test_distribute"
# Requires check-manifest, a full git checkout and probably a pony
donttest+=" or (RatingsTest and (test_custom_test or test_minimal or test_only_config))"
%pytest -k "not ($donttest)"

%post
%python_install_alternative pyroma

%postun
%python_uninstall_alternative pyroma

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGES.txt
%python_alternative %{_bindir}/pyroma
%{python_sitelib}/pyroma
%{python_sitelib}/pyroma-%{version}.dist-info

%changelog
