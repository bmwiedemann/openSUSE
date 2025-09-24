#
# spec file for package python-imageio-ffmpeg
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-imageio-ffmpeg
Version:        0.6.0
Release:        0
Summary:        FFMPEG wrapper for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/imageio/imageio-ffmpeg
Source:         https://files.pythonhosted.org/packages/source/i/imageio-ffmpeg/imageio_ffmpeg-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  ffmpeg
BuildRequires:  python-rpm-macros
Requires:       ffmpeg
BuildArch:      noarch
%python_subpackages

%description
FFMPEG wrapper for working with video files in Python.

%prep
%autosetup -n imageio_ffmpeg-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# github version has real tests, but tests require a network connection
%python_expand $python -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_version())';

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/imageio_ffmpeg
%{python_sitelib}/imageio_ffmpeg-%{version}.dist-info

%changelog
