#
# spec file for package python-curtsies
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
Name:           python-curtsies
Version:        0.3.0
Release:        0
Summary:        Curses-like terminal wrapper, with colored strings!
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bpython/curtsies
Source:         https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-curtsies-dont-require-typing-for-python3.5.patch gh#bpython/curtsies#111 badshah400@opensuse.org -- The typing module is only required for python3.4 and lower; patch taken from upstream git.
Patch0:         python-curtsies-dont-require-typing-for-python3.5.patch
BuildRequires:  %{python_module blessings}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyte}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-typing
Requires:       python-blessings
Requires:       python-wcwidth
BuildArch:      noarch
%if %{python_version_nodots} < 35
BuildRequires:  python3-typing
%endif
%ifpython2
Requires:       python-typing
%endif
%ifpython3
%if %{python3_version_nodots} < 35
Requires:       python-typing
%endif
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
%python_expand nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc readme.md
%{python_sitelib}/*

%changelog
