#
# spec file for package python-pypi-search
#
# Copyright (c) 2021 SUSE LLC
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
Name:             python-pypi-search
Version:          1.2.1
Release:          0
Summary:          Get Information on Python Packages From PyPI
License:          MIT
URL:              https://github.com/asadmoosvi/pypi-search
Source:           https://files.pythonhosted.org/packages/source/p/pypi-search/pypi-search-%{version}.tar.gz
BuildRequires:    python-rpm-macros
BuildRequires:    %{python_module setuptools}
# SECTION test requirements
BuildRequires:    %{python_module beautifulsoup4 >= 4.9.2}
BuildRequires:    %{python_module html2text >= 2020.1.16}
BuildRequires:    %{python_module requests >= 2.22.0}
# /SECTION
BuildRequires:    fdupes
Requires:         python-beautifulsoup4 >= 4.9.2
Requires:         python-html2text >= 2020.1.16
Requires:         python-requests >= 2.22.0
BuildArch:        noarch
Requires(post):   update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Get Information on Python Packages From PyPI

%prep
%setup -q -n pypi-search-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pypisearch
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pypisearch

%postun
%python_uninstall_alternative pypisearch

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pypisearch
%{python_sitelib}/pypi_search*

%changelog
