#
# spec file for package python-readme_renderer
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
Name:           python-readme_renderer
Version:        24.0
Release:        0
Summary:        A library for rendering "readme" descriptions
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/pypa/readme_renderer
Source:         https://files.pythonhosted.org/packages/source/r/readme_renderer/readme_renderer-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module bleach >= 3.0.0}
BuildRequires:  %{python_module check-manifest}
BuildRequires:  %{python_module cmarkgfm >= 0.2.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module docutils >= 0.13.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-bleach >= 3.0.0
Requires:       python-docutils >= 0.13.1
Requires:       python-six
Recommends:     python-cmarkgfm >= 0.2.0
BuildArch:      noarch

%python_subpackages

%description
Readme Renderer is a library that will safely render arbitrary ``README`` files
into HTML. It is designed to be used in Warehouse to render the
long_description for packages.

%prep
%setup -q -n readme_renderer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
