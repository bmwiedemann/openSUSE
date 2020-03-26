#
# spec file for package python-imageio
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-imageio
Version:        2.5.0
Release:        0
Summary:        Python library for reading and writing image, video, and related formats
License:        BSD-2-Clause
URL:            https://imageio.github.io/
Source0:        https://files.pythonhosted.org/packages/source/i/imageio/imageio-%{version}.tar.gz
Source1:        python-imageio-rpmlintrc
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-imageio-ffmpeg
Requires:       python-numpy
Recommends:     libfreeimageplus3
Recommends:     python-Pillow
BuildArch:      noarch
%ifpython3
Requires:       python-imageio-ffmpeg
%endif
%if %{with python2}
BuildRequires:  python-enum34
%endif
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
Imageio is a Python library that provides an interface to read and
write a wide range of image data, including animated images, volumetric
data, and scientific formats.

%prep
%setup -q -n imageio-%{version}

# Plugins are not executable scripts
for plgpy in imageio/plugins/_*.py ; do
    echo "Fixing $plgpy..."
    sed -i -e '1{/\/usr\/bin.*python/d}' $plgpy
done

%build
export IMAGEIO_NO_INTERNET=1
%python_build

%install
export IMAGEIO_NO_INTERNET=1
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export IMAGEIO_NO_INTERNET=1
%pytest -k "not test_fei_file_fail and not test_ffmpeg and not test_series_unclosed and not test_import_dependencies"

%files %{python_files}
%license LICENSE
%doc CONTRIBUTORS.txt README.md
%{python_sitelib}/*
%python3_only %{_bindir}/imageio_download_bin
%python3_only %{_bindir}/imageio_remove_bin

%changelog
