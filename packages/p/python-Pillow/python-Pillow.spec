#
# spec file for package python-Pillow
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?is_opensuse} || 0%{?suse_version} >= 1500
%bcond_without tk
%else
%bcond_with tk
%endif
Name:           python-Pillow
Version:        6.1.0
Release:        0
Summary:        Python Imaging Library (Fork)
License:        HPND
Group:          Development/Languages/Python
URL:            https://python-pillow.org/
Source:         https://files.pythonhosted.org/packages/source/P/Pillow/Pillow-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module olefile}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%if %{with tk}
BuildRequires:  %{python_module tk}
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libopenjp2)
%endif
%ifpython2
# Pillow is a friendly PIL fork which we used to package as 'imaging'
# Without providing python-imaging, all packages requiring it will break
Obsoletes:      %{oldpython}-imaging < %{version}
Provides:       %{oldpython}-imaging = %{version}
Obsoletes:      %{oldpython}-imaging-sane < %{version}
Provides:       %{oldpython}-imaging-sane = %{version}
%endif
%ifpython3
Obsoletes:      python3-imaging < %{version}
Provides:       python3-imaging = %{version}
%endif
%python_subpackages

%description
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the
Python Imaging Library by Fredrik Lundh and Contributors.

%package tk
Summary:        Python Imaging Library (Fork) - Tcl/Tk Module
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-tk
%ifpython2
# NOTE: We don't need to conflict with python-imaging here,
# because this package depends on python-Pillow, which already conflicts with python-imaging,
# so this cannot be installed alongside python-imaging
# And we cannot conflict with python-imaging directly, since python-Pillow provides python-imaging
# Just in case, conflict with python-imaging-tk in case it is ever implemented.
Obsoletes:      %{oldpython}-imaging-tk < %{version}
Provides:       %{oldpython}-imaging-tk = %{version}
%endif

%description tk
Pillow is the "friendly" PIL fork by Alex Clark and Contributors. PIL is the
Python Imaging Library by Fredrik Lundh and Contributors.

%prep
%setup -q -n Pillow-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# add missing path
%{python_expand echo "PIL" > %{buildroot}%{$python_sitearch}/PIL.pth}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
%if %{_arch} == s390 || %{_arch} == s390x
echo "WARNING ignoring tests completely due to https://github.com/python-pillow/Pillow/issues/1204 and segfault"
%else
%if %{_arch} == ppc || %{_arch} == ppc64
$python selftest.py --installed || \
echo "WARNING ignore failure https://github.com/python-pillow/Pillow/issues/1204"
$python setup.py test  || \
echo "WARNING ignore failure https://github.com/python-pillow/Pillow/issues/1204"
%else
$python selftest.py --installed
$python setup.py test
%endif
%endif
}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/PIL
%{python_sitearch}/PIL.pth
%{python_sitearch}/Pillow-%{version}-py%{python_version}.egg-info

%if %{with tk}
%exclude %{python_sitearch}/PIL/ImageTk*
%exclude %{python_sitearch}/PIL/_imagingtk*
%pycache_only %exclude %{python_sitearch}/PIL/__pycache__/ImageTk.*
%endif

%if %{with tk}
%files %{python_files tk}
%{python_sitearch}/PIL/ImageTk*
%{python_sitearch}/PIL/_imagingtk*
%pycache_only %{python_sitearch}/PIL/__pycache__/ImageTk.*

%endif

%changelog
