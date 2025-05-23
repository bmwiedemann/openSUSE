#
# spec file for package python-pywlroots
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
%bcond_without test
Name:           python-pywlroots
Version:        0.17.0
Release:        0
Summary:        Python binding to the wlroots library using cffi
License:        NCSA
Group:          Development/Languages/Python
URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz
Source1:        python-pywlroots-rpmlintrc
# Patch0:         fix-include-paths.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distutils-extra}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pywayland >= 0.4.14}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xkbcommon >= 0.2}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  libdrm >= 2.4.113
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
# For future possible versions
BuildConflicts: pkgconfig(wlroots) >= 0.18.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Requires:       python-pywayland
Requires:       python-xkbcommon
%python_subpackages

%description
Python binding to the wlroots library using cffi.

%prep
%autosetup -n pywlroots-%{version}

%build
export CFLAGS="%optflags $(pkg-config --cflags wayland-client xkbcommon pixman-1 libinput libdrm)"
%python_exec wlroots/ffi_build.py
%pyproject_wheel

%install
export CFLAGS="%optflags $(pkg-config --cflags wayland-client xkbcommon pixman-1 libinput libdrm)"
%python_exec wlroots/ffi_build.py
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
export CFLAGS="%optflags $(pkg-config --cflags wayland-client xkbcommon pixman-1 libinput libdrm)"
%pytest -vv
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*wlroots*/

%changelog
