#
# spec file for package python-nbsphinx-link
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-nbsphinx-link
Version:        1.2.0
Release:        0
Summary:        Sphinx extension for including notebook files outside sphinx source root
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vidartf/nbsphinx-link
Source:         https://files.pythonhosted.org/packages/source/n/nbsphinx-link/nbsphinx-link-%{version}.tar.gz
BuildRequires:  %{python_module nbsphinx}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python-nbsphinx
Provides:       python-jupyter_nbsphinx_link = %{version}
Obsoletes:      python-jupyter_nbsphinx_link <= %{version}
BuildArch:      noarch
%ifpython3
Provides:       jupyter-nbsphinx-link = %{version}
%endif
%python_subpackages

%description
A sphinx extension for including notebook files from outside the
sphinx source root.

Normally, Sphinx will only allow you to add files that are situated
inside the source directory, but you might want to include files from
another directory, for example a central 'examples' folder. For RST
files these can be linked with `include` directives inside another
RST file. For notebooks, there's nbsphinx-link!

%prep
%setup -q -n nbsphinx-link-%{version}
sed -i 's/\r$//' README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -c "import nbsphinx_link"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/nbsphinx_link-%{version}-py*.egg-info
%{python_sitelib}/nbsphinx_link/

%changelog
