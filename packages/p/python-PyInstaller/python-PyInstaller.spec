#
# spec file for package python-PyInstaller
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
%bcond_without  test
Name:           python-PyInstaller
Version:        3.5
Release:        0
Summary:        Bundle a Python application and all its dependencies into a single package
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://www.pyinstaller.org
Source:         https://files.pythonhosted.org/packages/source/P/PyInstaller/PyInstaller-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
Requires:       python-macholib >= 1.8
Requires:       python-pefile >= 2017.8.1
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     upx
%if %{with test}
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module QtAwesome}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module macholib >= 1.8}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module pefile >= 2017.8.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pycountry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-dis3
BuildRequires:  upx
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
%setup -q -n PyInstaller-%{version}
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
%pytest_arch tests/unit tests/functional --ignore=tests/functional/test_libraries.py --ignore=tests/functional/test_hooks -k 'not test_find_module'
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
