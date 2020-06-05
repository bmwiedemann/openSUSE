#
# spec file for package python-bandit
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Tests require python-hacking, which isn't compatible with pycodestyle
%bcond_without  builddocs
# dependencies are no longer py2 compatible
%define skip_python2 1
Name:           python-bandit
Version:        1.6.2
Release:        0
Summary:        Security oriented static analyser for Python code
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/bandit
Source:         https://files.pythonhosted.org/packages/source/b/bandit/bandit-%{version}.tar.gz
Patch0:         remove-non-test-deps.patch
BuildRequires:  %{python_module GitPython >= 1.0.1}
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module beautifulsoup4 >= 4.6.0}
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module pbr >= 1.8}
BuildRequires:  %{python_module python-subunit >= 0.0.18}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module stestr >= 1.0.0}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 2.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# doc requirements
%if %{with builddocs}
BuildRequires:  %{python_module Sphinx >= 1.2.1}
BuildRequires:  %{python_module oslotest >= 3.2.0}
BuildRequires:  %{python_module reno >= 1.8.0}
%endif
Requires:       python-GitPython >= 1.0.1
Requires:       python-PyYAML >= 3.13
Requires:       python-six >= 1.10.0
Requires:       python-stestr >= 1.0.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
Bandit is a tool designed to find common security issues in Python code. To do
this Bandit processes each file, builds an AST from it, and runs appropriate
plugins against the AST nodes. Once Bandit has finished scanning all the files
it generates a report.

%prep
%setup -q -n bandit-%{version}
%patch0 -p1
sed -i '/^#!/d' bandit/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/bandit
%python_clone -a %{buildroot}%{_bindir}/bandit-config-generator
%python_clone -a %{buildroot}%{_bindir}/bandit-baseline

%check
# Copy executables to py2/3 build areas, to be used for testing
%{python_expand mkdir build/bin
for filepath in %{buildroot}/%{_bindir}/bandit*-%{$python_bin_suffix}; do
  filename=$(basename $filepath)
  unsuffixed=${filename/-%{$python_bin_suffix}/}
  cp $filepath build/bin/$unsuffixed
done
}
%{python_expand export PATH="$(pwd)/build/bin:$PATH"
$python setup.py test
}

%post
%{python_install_alternative bandit bandit-config-generator bandit-baseline }

%postun
%python_uninstall_alternative bandit

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%python_alternative %{_bindir}/bandit
%python_alternative %{_bindir}/bandit-config-generator
%python_alternative %{_bindir}/bandit-baseline
%{python_sitelib}/*

%changelog
