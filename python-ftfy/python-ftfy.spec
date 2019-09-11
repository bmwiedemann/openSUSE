#
# spec file for package python-ftfy
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
%define         skip_python2 1
Name:           python-ftfy
Version:        5.6
Release:        0
Summary:        Python module for repairing mis-decoded Unicode text
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/LuminosoInsight/python-ftfy
Source:         https://github.com/LuminosoInsight/python-ftfy/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wcwidth
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wcwidth}
# /SECTION
%python_subpackages

%description
Ftfy attempts to repair Unicode text that has been erroneously
put through an encode/decode cycle with different encodings.

%prep
%setup -q -n python-ftfy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH="$PATH:%{buildroot}%{_bindir}"
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%python3_only %{_bindir}/ftfy
%{python_sitelib}/*

%changelog
