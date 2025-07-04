#
# spec file for package python-ebcdic
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-ebcdic
Version:        1.1.1
Release:        0
Summary:        Additional EBCDIC codecs for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/roskakori/CodecMapper
Source:         https://github.com/roskakori/CodecMapper/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Additional EBCDIC codecs for Python.

%prep
%setup -q -n CodecMapper-%{version}/ebcdic
# do not use venv python
sed -i -e 's:"${basedir}/venv/bin/python":"${PYTHON}":' ../build.xml

%build
# first generate the py files
pushd ..
%python_expand ant ebcdic -DPYTHON="$python"
popd
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/ebcdic
%{python_sitelib}/ebcdic-%{version}.dist-info

%changelog
