#
# spec file for package python-pyalsaaudio
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
Name:           python-pyalsaaudio
Version:        0.10.0
Release:        0
Summary:        ALSA bindings for Python
License:        Python-2.0
URL:            https://larsimmisch.github.io/pyalsaaudio/
Source:         https://files.pythonhosted.org/packages/source/p/pyalsaaudio/pyalsaaudio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
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

%check
%pytest_arch test.py -k 'not (testMixerAll or testMixerClose or testPCMAll or testPCMClose or testPCMDeprecated)'

%files %{python_files}
%license LICENSE
%doc doc/*.rst
%{python_sitearch}/*

%changelog
