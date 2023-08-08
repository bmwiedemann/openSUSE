#
# spec file for package python-sphinxcontrib-youtube
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-sphinxcontrib-youtube
Version:        1.2.0
Release:        0
Summary:        Sphinx "youtube" extension
License:        BSD-3-Clause
URL:            https://github.com/sphinx-contrib/youtube
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-youtube/sphinxcontrib-youtube-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-requests
Suggests:       python-furo
Suggests:       python-sphinx-copybutton
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 0.6}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Sphinx "youtube" extension

%prep
%autosetup -p1 -n sphinxcontrib-youtube-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%{python_sitelib}/sphinxcontrib/youtube
%{python_sitelib}/sphinxcontrib_youtube-%{version}*-nspkg.pth
%{python_sitelib}/sphinxcontrib_youtube-%{version}*-info

%changelog
