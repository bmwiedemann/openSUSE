#
# spec file for package python-filetype
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
Name:           python-filetype
Version:        1.2.0
Release:        0
Summary:        Infer file type and MIME type of any file/buffer. No external dependencies
License:        MIT
URL:            https://github.com/h2non/filetype.py
Source:         https://files.pythonhosted.org/packages/source/f/filetype/filetype-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Small and dependency free `Python`_ package to infer file type and MIME
type checking the `magic numbers`_ signature of a file or buffer.

This is a Python port from `filetype`_ Go package.

%prep
%setup -q -n filetype-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/filetype
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%post
%python_install_alternative filetype

%postun
%python_uninstall_alternative filetype

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/filetype
%{python_sitelib}/filetype-%{version}.dist-info
%python_alternative %{_bindir}/filetype

%changelog
