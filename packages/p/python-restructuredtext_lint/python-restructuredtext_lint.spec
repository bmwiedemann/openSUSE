#
# spec file for package python-restructuredtext_lint
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
Name:           python-restructuredtext_lint
Version:        1.3.0
Release:        0
Summary:        Linter for reStructuredText
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/twolfson/restructuredtext-lint
Source:         https://files.pythonhosted.org/packages/source/r/restructuredtext_lint/restructuredtext_lint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.11
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils >= 0.11}
# /SECTION
%python_subpackages

%description
Linter for reStructuredText.

This was created out of frustration with PyPI; it sucks finding out
your reST is invalid **after** uploading it. It is being developed
in junction with a Sublime Text linter.

%prep
%setup -q -n restructuredtext_lint-%{version}
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rst-lint
%python_clone -a %{buildroot}%{_bindir}/restructuredtext-lint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m unittest discover
}

%post
%python_install_alternative rst-lint
%python_install_alternative restructuredtext-lint

%postun
%python_uninstall_alternative rst-lint
%python_uninstall_alternative restructuredtext-lint

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license UNLICENSE
%python_alternative %{_bindir}/restructuredtext-lint
%python_alternative %{_bindir}/rst-lint
%{python_sitelib}/*

%changelog
