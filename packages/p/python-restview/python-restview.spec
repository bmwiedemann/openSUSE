#
# spec file for package python-restview
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
Name:           python-restview
Version:        2.9.2
Release:        0
Summary:        ReStructuredText viewer
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://mg.pov.lt/restview/
Source:         https://files.pythonhosted.org/packages/source/r/restview/restview-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module readme_renderer}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docutils
Requires:       python-pygments
Requires:       python-readme_renderer
BuildArch:      noarch

%python_subpackages

%description
A viewer for ReStructuredText documents that renders them on the fly.

%prep
%setup -q -n restview-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%python3_only %{_bindir}/restview
%{python_sitelib}/*

%changelog
