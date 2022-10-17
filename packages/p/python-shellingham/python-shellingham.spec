#
# spec file for package python-shellingham
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-shellingham
Version:        1.5.0
Release:        0
Summary:        Library to detect surrounding shell
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/shellingham
Source:         https://github.com/sarugaku/shellingham/archive/refs/tags/%{version}.tar.gz#/shellingham-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python library to detect surrounding shell.

%prep
%setup -q -n shellingham-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/shellingham
%{python_sitelib}/shellingham-%{version}*-info

%changelog
