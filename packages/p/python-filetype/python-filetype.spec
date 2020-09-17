#
# spec file for package python-filetype
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
Name:           python-filetype
Version:        1.0.7
Release:        0
Summary:        Infer file type and MIME type of any file/buffer. No external dependencies
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/h2non/filetype.py
Source:         https://files.pythonhosted.org/packages/source/f/filetype/filetype-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Small and dependency free `Python`_ package to infer file type and MIME
type checking the `magic numbers`_ signature of a file or buffer.

This is a Python port from `filetype`_ Go package.

%prep
%setup -q -n filetype-%{version}

%build
%python_build

%install
%python_install
# do not install examples in generic folder
%python_expand rm -r %{buildroot}%{$python_sitelib}/examples/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
