#
# spec file for package python-pa-ringbuffer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pa-ringbuffer
Version:        0.1.3
Release:        0
Summary:        Python wrapper for PortAudio's ring buffer
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/spatialaudio/python-pa-ringbuffer
Source:         https://files.pythonhosted.org/packages/source/p/pa-ringbuffer/pa-ringbuffer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
