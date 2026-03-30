#
# spec file for package python-zope.dottedname
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


Name:           python-zope.dottedname
Version:        7.1
Release:        0
Summary:        Resolver for Python dotted names
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.dottedname
Source:         https://files.pythonhosted.org/packages/source/z/zope.dottedname/zope_dottedname-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 78.1.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Resolver for Python dotted names.

%prep
%autosetup -p1 -n zope_dottedname-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%dir %{python_sitelib}/zope
%{python_sitelib}/zope/dottedname
%{python_sitelib}/zope[._]dottedname-%{version}.dist-info

%changelog
