#
# spec file for package python-Markdown
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-Markdown
Version:        3.3.3
Release:        0
Summary:        Python implementation of Markdown
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://python-markdown.github.io/
Source:         https://files.pythonhosted.org/packages/source/M/Markdown/Markdown-%{version}.tar.gz
Patch0:         markdown-3.0-python37.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of John Gruber's [Markdown][].
It is almost completely compliant with the reference implementation,
though there are a few known issues. See [Features][] for information
on what exactly is supported and what is not. Additional features are
supported by the [Available Extensions][].

%prep
%setup -q -n Markdown-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/markdown_py

%check
%python_exec -m unittest discover

%post
%python_install_alternative markdown_py

%postun
%python_uninstall_alternative markdown_py

%files %{python_files}
%license LICENSE.md
%doc README.md docs/*
%python_alternative %{_bindir}/markdown_py
%{python_sitelib}/Markdown-%{version}-py%{python_version}.egg-info
%{python_sitelib}/markdown

%changelog
