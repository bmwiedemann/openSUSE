#
# spec file for package python-watchdog
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-watchdog
Version:        0.9.0
Release:        0
Summary:        Filesystem events monitoring
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/gorakhargosh/watchdog
Source:         https://files.pythonhosted.org/packages/source/w/watchdog/watchdog-%{version}.tar.gz
Patch0:         add-missing-conftest.patch
BuildRequires:  %{python_module pathtools}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout >= 0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-PyYAML
Requires:       python-argh
Requires:       python-pathtools
BuildArch:      noarch
%ifpython2
Requires:       python-Brownie
%endif
%python_subpackages

%description
Python API and shell utilities to monitor file system events.

%package doc
Summary:        Documentation and examples for %{name}
Group:          Documentation/HTML

%description doc
This package contains documentation and examples for %{name}.

%prep
%setup -q -n watchdog-%{version}
%patch0 -p1
chmod -x README.rst
# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'

%build
%python_build
cd docs && make html && rm -r build/html/.buildinfo build/html/objects.inv # Build HTML docs

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version}

%files %{python_files}
%license COPYING LICENSE
%doc AUTHORS changelog.rst MANIFEST.in README.rst
%python3_only %{_bindir}/watchmedo
%{python_sitelib}/watchdog
%{python_sitelib}/watchdog-%{version}-py%{python_version}.egg-info

%files %{python_files doc}
%doc docs/build/html

%changelog
