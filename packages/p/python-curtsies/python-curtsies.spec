#
# spec file for package python-curtsies
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-curtsies
Version:        0.4.1
Release:        0
Summary:        Curses-like terminal wrapper, with colored strings!
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bpython/curtsies
Source:         https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
BuildRequires:  %{python_module blessed >= 1.5}
BuildRequires:  %{python_module cwcwidth}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyte}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blessed >= 1.5
Requires:       python-cwcwidth
BuildArch:      noarch
%python_subpackages

%description
Curses-like terminal wrapper with a display based on compositing 2d
arrays of text.

%prep
%setup -q -n curtsies-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/curtsies
%{python_sitelib}/curtsies-%{version}-py*.egg-info

%changelog
