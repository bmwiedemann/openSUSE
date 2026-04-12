#
# spec file for package python-packageurl-python
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


Name:           python-packageurl-python
Version:        0.17.6
Release:        0
Summary:        A "purl" aka package URL parser and builder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/package-url/packageurl-python
Source:         https://files.pythonhosted.org/packages/source/p/packageurl_python/packageurl_python-%{version}.tar.gz
# git submodule "spec" which is not part of the pypi tarball
Source1:        https://github.com/package-url/purl-spec/archive/c398646bb2d642ccdd43bfbf5923cf650d69dc6a.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A "purl" aka. package URL parser and builder.

%prep
%setup -q -n packageurl_python-%{version} -a1
ln -s purl-spec-c398646bb2d642ccdd43bfbf5923cf650d69dc6a spec

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license mit.LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/packageurl
%{python_sitelib}/packageurl_python-%{version}.dist-info

%changelog
