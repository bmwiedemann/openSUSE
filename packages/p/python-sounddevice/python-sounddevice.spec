#
# spec file for package python-sounddevice
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
Name:           python-sounddevice
Version:        0.3.13
Release:        0
Summary:        Module to play and record sound with Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://python-sounddevice.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/s/sounddevice/sounddevice-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  portaudio
BuildRequires:  python-rpm-macros
Requires:       portaudio
Requires:       python-cffi >= 1.0
Recommends:     python-numpy
BuildArch:      noarch

%python_subpackages

%description
This Python module provides bindings for the PortAudio library and a few
convenience functions to play and record NumPy arrays containing audio signals.


%prep
%setup -q -n sounddevice-%{version}

%build
chmod 644 examples/*
%python_build

%install
%python_install
%python_expand fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS.rst README.rst examples
%license LICENSE
%{python_sitelib}/*

%check
# no upstream tests, examples needs devices

%changelog
