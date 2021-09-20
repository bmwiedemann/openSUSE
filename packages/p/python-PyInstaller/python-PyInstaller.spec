#
# spec file for package python-PyInstaller
#
# Copyright (c) 2021 SUSE LLC
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
%bcond_without  test
%define modname PyInstaller
Name:           python-PyInstaller
Version:        4.5.1
Release:        0
Summary:        Bundle a Python application and all its dependencies into a single package
License:        GPL-2.0-only
URL:            https://www.pyinstaller.org
Source:         https://github.com/pyinstaller/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
Requires:       python-devel
Requires:       python-macholib >= 1.8
Requires:       python-pefile >= 2017.8.1
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     upx
%if %{with test}
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module QtAwesome}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module macholib >= 1.8}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pefile >= 2017.8.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  upx
%if %{with python2}
BuildRequires:  python-dis3
%endif
%endif
%ifpython2
Requires:       python-dis3
%endif
%python_subpackages

%description
PyInstaller bundles a Python application and all its dependencies into a single
package. The user can run the packaged app without installing a Python
interpreter or any modules.

%prep
%setup -q -n pyinstaller-%{version}
%autopatch -p1

chmod a-x PyInstaller/utils/hooks/__init__.py

# Force build of bootloader
rm -r PyInstaller/bootloader

%build
# -Wno-stringop-overflow only needed on ppc64
export CFLAGS="%{optflags} -Wno-stringop-truncation -Wno-unused-variable -Wno-unused-function -Wno-unused-but-set-variable -Wno-stringop-overflow"
%python_build

%install
%python_install
%{python_expand  # Relocate to sitearch
if [ "%{$python_sitearch}" != "%{$python_sitelib}" ]; then
  mkdir -p %{buildroot}%{$python_sitearch}
  mv %{buildroot}%{$python_sitelib}/* %{buildroot}%{$python_sitearch}
fi
%fdupes %{buildroot}%{$python_sitearch}
}

%python_clone -a %{buildroot}%{_bindir}/pyinstaller
%python_clone -a %{buildroot}%{_bindir}/pyi-archive_viewer
%python_clone -a %{buildroot}%{_bindir}/pyi-bindepend
%python_clone -a %{buildroot}%{_bindir}/pyi-grab_version
%python_clone -a %{buildroot}%{_bindir}/pyi-makespec
%python_clone -a %{buildroot}%{_bindir}/pyi-set_version

%if %{with test}
%check
export LANG=en_US.UTF-8
# test_get_co_using_ctypes, test_get_co_using_ctypes_from_extension, test_replace_paths_in_code broken with python 3.8 on PyInstall 3.6
# gh#pyinstaller/pyinstaller#4406 skip TestDeeplyNested.testRegr (it is just the only method in the class)
%pytest_arch -n auto tests/unit -k 'not (test_find_module or test_egg and not test_nspkg1 or test_get_co_using_ctypes or test_get_co_using_ctypes_from_extension or test_replace_paths_in_code or TestDeeplyNested)'
%endif

%post
%{python_install_alternative pyinstaller pyi-archive_viewer pyi-bindepend pyi-grab_version pyi-makespec pyi-set_version}

%postun
%python_uninstall_alternative pyinstaller

%files %{python_files}
%doc README.rst doc/CHANGES.rst
%license COPYING.txt
%python_alternative %{_bindir}/pyinstaller
%python_alternative %{_bindir}/pyi-archive_viewer
%python_alternative %{_bindir}/pyi-bindepend
%python_alternative %{_bindir}/pyi-grab_version
%python_alternative %{_bindir}/pyi-makespec
%python_alternative %{_bindir}/pyi-set_version
%{python_sitearch}/*

%changelog
