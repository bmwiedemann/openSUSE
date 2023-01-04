#
# spec file for package python-Pillow
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-Pillow
Version:        9.4.0
Release:        0
Summary:        Python Imaging Library (Fork)
License:        HPND
URL:            https://python-pillow.org/
Source:         https://files.pythonhosted.org/packages/source/P/Pillow/Pillow-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module olefile}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tk}
BuildRequires:  fdupes
BuildRequires:  libimagequant-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  tix
BuildRequires:  unzip
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(zlib)
Requires:       python-olefile
Obsoletes:      python-imaging < %{version}
Provides:       python-imaging = %{version}
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libopenjp2)
%endif
%python_subpackages

%description
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the
Python Imaging Library by Fredrik Lundh and Contributors.

%package tk
Summary:        Python Imaging Library (Fork) - Tcl/Tk Module
Requires:       %{name} = %{version}
Requires:       python-tk

%description tk
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the
Python Imaging Library by Fredrik Lundh and Contributors.

%prep
%setup -q -n Pillow-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
# add missing path
%{python_expand echo "PIL" > %{buildroot}%{$python_sitearch}/PIL.pth}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch} PYTHONDONTWRITEBYTECODE=1
%if "%{_arch}" == "s390" || "%{_arch}" == "s390x"
echo "WARNING ignoring tests completely due to https://github.com/python-pillow/Pillow/issues/1204 and segfault"
%else
%if "%{_arch}" == "ppc" || "%{_arch}" == "ppc64"
$python selftest.py --installed || \
echo "WARNING ignore failure https://github.com/python-pillow/Pillow/issues/1204"
pytest-%{$python_bin_suffix} --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -v || \
echo "WARNING ignore failure https://github.com/python-pillow/Pillow/issues/1204"
%else
$python selftest.py --installed
pytest-%{$python_bin_suffix} --ignore=_build.python2 --ignore=_build.python3 --ignore=_build.pypy3 -v -k 'not (test_stroke or test_stroke_multiline)'
%endif
%endif
}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.md
%{python_sitearch}/PIL
%{python_sitearch}/PIL.pth
%{python_sitearch}/Pillow-%{version}-py%{python_version}.egg-info
%exclude %{python_sitearch}/PIL/ImageTk*
%exclude %{python_sitearch}/PIL/_imagingtk*
%pycache_only %exclude %{python_sitearch}/PIL/__pycache__/ImageTk.*

%files %{python_files tk}
%{python_sitearch}/PIL/ImageTk*
%{python_sitearch}/PIL/_imagingtk*
%pycache_only %{python_sitearch}/PIL/__pycache__/ImageTk.*

%changelog
