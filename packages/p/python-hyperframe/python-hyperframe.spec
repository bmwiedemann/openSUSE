#
# spec file for package python-hyperframe
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
%define skip_python2 1
Name:           python-hyperframe
Version:        6.0.0
Release:        0
Summary:        HTTP/2 framing layer for Python
License:        MIT
URL:            https://github.com/python-hyper/hyperframe
Source0:        https://files.pythonhosted.org/packages/source/h/hyperframe/hyperframe-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library contains the HTTP/2 framing code used in the hyper project.
It provides a pure-Python codebase that is capable of decoding a binary
stream into HTTP/2 frames.

%prep
%setup -q -n hyperframe-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CONTRIBUTORS.rst CHANGELOG.rst
%{python_sitelib}/hyperframe
%{python_sitelib}/hyperframe-%{version}-py%{python_version}.egg-info

%changelog
