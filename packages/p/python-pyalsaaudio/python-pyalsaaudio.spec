#
# spec file for package python-pyalsaaudio
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-pyalsaaudio
Version:        0.8.4
Release:        0
Summary:        ALSA bindings for Python
License:        Python-2.0
Group:          Development/Languages/Python
Url:            http://larsimmisch.github.io/pyalsaaudio/
Source:         https://files.pythonhosted.org/packages/source/p/pyalsaaudio/pyalsaaudio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  alsa-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
This package contains wrappers for accessing the ALSA API from Python.
It is fairly complete for PCM devices and Mixer access.

%prep
%setup -q -n pyalsaaudio-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES LICENSE
%{python_sitearch}/*

%changelog
