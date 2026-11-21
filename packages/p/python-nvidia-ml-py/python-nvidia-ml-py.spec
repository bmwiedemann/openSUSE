#
# spec file for package python-nvidia-ml-py
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-nvidia-ml-py
Version:        13.615.71
Release:        0
Summary:        Python bindings for the NVIDIA Management Library
License:        BSD-3-Clause
URL:            https://pypi.org/project/nvidia-ml-py/
Source:         https://files.pythonhosted.org/packages/source/n/nvidia_ml_py/nvidia_ml_py-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python bindings to the NVIDIA Management Library, providing GPU
management and monitoring functions. This is a wrapper around NVML;
the libnvidia-ml.so.1 library itself ships with the NVIDIA driver.

%prep
%autosetup -n nvidia_ml_py-%{version}
# The sdist ships no LICENSE file; the BSD-3-Clause text lives at the
# end of README.txt. Extract it so %%license has something to ship.
grep -A 999999 "COPYRIGHT" README.txt > LICENSE
# Do not install a top-level "example" module into site-packages;
# ship example.py as documentation instead.
sed -i "s/, 'example'//" setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand $python -c "import pynvml; print(pynvml.__file__)"}

%files %{python_files}
%license LICENSE
%doc README.txt example.py
%{python_sitelib}/pynvml.py
%pycache_only %{python_sitelib}/__pycache__/pynvml.*.pyc
%{python_sitelib}/nvidia_ml_py-%{version}.dist-info

%changelog
