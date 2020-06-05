#
# spec file for package python-mox3
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
%global skip_python2 1
Name:           python-mox3
Version:        1.0.0
Release:        0
Summary:        An unofficial port of the Google mox framework to Python 3
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/openstack/mox3
Source0:        https://files.pythonhosted.org/packages/source/m/mox3/mox3-%{version}.tar.gz
BuildRequires:  %{python_module fixtures >= 3.0.0}
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module setuptools >= 16.0}
BuildRequires:  fdupes
BuildRequires:  openstack-macros
BuildRequires:  python-rpm-macros
Requires:       python-fixtures >= 3.0.0
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
# SECTION documentation requirements
BuildRequires:  python3-Sphinx >= 1.6.5
BuildRequires:  python3-openstackdocstheme >= 1.18.1
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module python-subunit >= 1.0.0}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module stestr >= 2.0.0}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testtools >= 2.2.0}
# /SECTION
%python_subpackages

%description
Mox3 is an unofficial port of the Google mox framework to Python 3. It
was meant to be as compatible with mox as possible, but small
enhancements have been made. The library was tested on Python version
3.2, 2.7 and 2.6.

%package     -n python-mox3-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description -n python-mox3-doc
Mox3 is an unofficial port of the Google mox framework to Python 3. It
was meant to be as compatible with mox as possible, but small
enhancements have been made. The library was tested on Python version
3.2, 2.7 and 2.6.

This package contains documentation in HTML format.

%prep
%autosetup -n mox3-%{version}
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%python_build

# generate html docs
%sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/mox3/tests

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r doc/build/html %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_docdir}/%{name}/html

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license COPYING.txt
%doc README.rst
%{python_sitelib}/mox3
%{python_sitelib}/mox3-*.egg-info

%files -n python-mox3-doc
%license COPYING.txt
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/html/

%changelog
