#
# spec file for package python-imagesize
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
%{?sle15_python_module_pythons}
Name:           python-imagesize
Version:        1.4.1
Release:        0
Summary:        Getting image size from PNG/JPEG/JPEG2000/GIF files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/shibukawa/imagesize_py
Source:         https://files.pythonhosted.org/packages/source/i/imagesize/imagesize-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Pure Python library which parses image files' header and returns the image size.

Supported formats:
 * PNG
 * JPEG
 * JPEG2000
 * GIF

%prep
%setup -q -n imagesize-%{version}

%build
%python_build

%install
%python_install

%check
rm -v test/test_get_filelike.py
%pytest

%files %{python_files}
%{python_sitelib}/*
%doc README.rst

%changelog
