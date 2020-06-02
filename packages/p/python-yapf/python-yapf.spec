#
# spec file for package python-yapf
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
Name:           python-yapf
Version:        0.30.0
Release:        0
Summary:        A formatter for Python code
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/yapf
Source:         https://files.pythonhosted.org/packages/source/y/yapf/yapf-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Recommends:     python-futures
%endif
%python_subpackages

%description
YAPF is based off clang-format and reformats it to the closest
formatting that conforms to the style guide, even if the original
code did not violate the style guide.

This is in contrast to other formatters like autopep8 and pep8ify
which are made to only remove lint errors from code, which has some
limitations, like, code that conforms to the PEP 8 guidelines may not
be reformatted.

%prep
%setup -q -n yapf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/yapf
%python_expand rm -r %{buildroot}%{$python_sitelib}/yapftests

%check
%pytest --capture=no

%post
%python_install_alternative yapf

%postun
%python_uninstall_alternative yapf

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG
%python_alternative %{_bindir}/yapf
%{python_sitelib}/yapf/
%{python_sitelib}/yapf-%{version}-py*.egg-info/

%changelog
