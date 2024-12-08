#
# spec file for package python-PyInstaller
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
%bcond_without  test
%define modname PyInstaller
Name:           python-PyInstaller
Version:        6.11.1
Release:        0
Summary:        Bundle a Python application and all its dependencies into a single package
License:        GPL-2.0-only
URL:            https://www.pyinstaller.org
Source:         https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v%{version}.tar.gz#/pyinstaller-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
Requires:       python-altgraph
Requires:       python-packaging >= 22.0
Requires:       python-pyinstaller-hooks-contrib >= 2024.0
Requires:       python-setuptools >= 42.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     upx
%if %{with test}
BuildRequires:  %{python_module altgraph}
BuildRequires:  %{python_module packaging >= 22.0}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyinstaller-hooks-contrib >= 2024.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  upx
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
%pytest_arch -n auto tests/unit
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
%{python_sitearch}/PyInstaller
%{python_sitearch}/pyinstaller-%{version}*info

%changelog
