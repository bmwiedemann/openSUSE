#
# spec file
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


%bcond_without  test
%define pyname  pywayland
Name:           python-%{pyname}
Version:        0.4.15
Release:        0
Summary:        Python binding to the wayland library using cffi
License:        NCSA
Group:          Development/Libraries/Python
URL:            https://github.com/flacjacket/pywayland
Source0:        https://files.pythonhosted.org/packages/source/p/pywayland/pywayland-%{version}.tar.gz
Patch0:         fix-wayland-paths.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distutils-extra}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(wayland-client) >= 1.21
BuildRequires:  pkgconfig(wayland-cursor) >= 1.21
BuildRequires:  pkgconfig(wayland-protocols) >= 1.26
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Python binding to the wayland library using cffi.

%prep
%setup -q -n pywayland-%{version}
%patch0 -p1

%build
export CFLAGS="%optflags $(pkg-config --cflags wayland-client)"
%python_exec pywayland/ffi_build.py
%python_build

%install
export CFLAGS="%optflags $(pkg-config --cflags wayland-client)"
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/pywayland-scanner

%if %{with test}
%check
export CFLAGS="%optflags $(pkg-config --cflags wayland-client)"
mkdir -p %{buildroot}/fake-xdg-runtime-dir
export XDG_RUNTIME_DIR=%{buildroot}/fake-xdg-runtime-dir
%python_exec -m pywayland.scanner
%pytest -vv
rm -rfv ${XDG_RUNTIME_DIR}
%endif

%post
%python_install_alternative pywayland-scanner

%postun
%python_uninstall_alternative pywayland-scanner

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*pywayland*/
%python_alternative %{_bindir}/pywayland-scanner

%changelog
