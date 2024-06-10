#
# spec file for package python-sounddevice
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-sounddevice
Version:        0.4.7
Release:        0
Summary:        Module to play and record sound with Python
License:        MIT
URL:            https://python-sounddevice.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/s/sounddevice/sounddevice-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS.rst README.rst examples
%license LICENSE
%{python_sitelib}/{_sounddevice.py,sounddevice.py}
%pycache_only %{python_sitelib}/__pycache__/{sounddevice,_sounddevice}*

%{python_sitelib}/sounddevice-%{version}.dist-info

%check
# no upstream tests, examples needs devices

%changelog
