#
# spec file for package python-pa-ringbuffer
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pa-ringbuffer
Version:        0.1.4
Release:        0
Summary:        Python wrapper for PortAudio's ring buffer
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spatialaudio/python-pa-ringbuffer
Source:         https://files.pythonhosted.org/packages/source/p/pa-ringbuffer/pa-ringbuffer-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi
BuildArch:      noarch
%python_subpackages

%description
The ring buffer functionality is typically not included in binary
distributions of PortAudio, therefore most Python wrappers don't include it,
either.

The pa_ringbuffer module provides only a Python wrapper, the actual
PortAudio ring buffer code has to be compiled separately.
It can be used on any Python version where CFFI is available.

This module is designed to be used together with the sounddevice module (it
might work with other modules, too) for non-blocking transfer of data between
the main Python program and an audio callback function which is implemented in C
or some other compiled language.

This module is not meant to be used on its own, it is only useful in cooperation
with another Python module using CFFI.

%prep
%setup -q -n pa-ringbuffer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/pa_ringbuffer.py
%pycache_only %{python_sitelib}/__pycache__/pa_ringbuffer*
%{python_sitelib}/pa[-_]ringbuffer-%{version}*-info

%changelog
