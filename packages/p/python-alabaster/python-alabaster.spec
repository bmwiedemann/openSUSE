#
# spec file for package python-alabaster
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-alabaster
Version:        0.7.13
Release:        0
Summary:        Modified Kr Sphinx doc theme
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/bitprophet/alabaster
Source:         https://files.pythonhosted.org/packages/source/a/alabaster/alabaster-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his Requests project), which was itself
originally based on @mitsuhiko's theme used for Flask & related
projects.

%prep
%setup -q -n alabaster-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/alabaster*
%license LICENSE
%doc README.rst

%changelog
