#
# spec file for package python-curtsies
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-curtsies
Version:        0.3.1
Release:        0
Summary:        Curses-like terminal wrapper, with colored strings!
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bpython/curtsies
Source:         https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
# https://github.com/bpython/curtsies/pull/127
Patch0:         remove-nose.patch
BuildRequires:  %{python_module blessings}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyte}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blessings
Requires:       python-wcwidth
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-typing
%endif
%if %{python_version_nodots} < 35
BuildRequires:  python3-typing
Requires:       python-typing
%endif
%ifpython2
Requires:       python-typing
%endif
%python_subpackages

%description
Curses-like terminal wrapper with a display based on compositing 2d
arrays of text.

%prep
%setup -q -n curtsies-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s tests -v

%files %{python_files}
%license LICENSE
%doc readme.md
%{python_sitelib}/*

%changelog
