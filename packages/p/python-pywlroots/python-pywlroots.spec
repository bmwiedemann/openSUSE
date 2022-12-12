#
# spec file for package python-pywlroots
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without test
Name:           python-pywlroots
Version:        0.15.24
Release:        0
Summary:        Python binding to the wlroots library using cffi
License:        NCSA
Group:          Development/Languages/Python
URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz
Source1:        python-pywlroots-rpmlintrc
Patch0:         fix-include-paths.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distutils-extra}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pywayland >= 0.4.14}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xkbcommon}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  libdrm >= 2.4.113
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(wlroots) >= 0.15.0
BuildConflicts: pkgconfig(wlroots) >= 0.16.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Requires:       python-pywayland
Requires:       python-xkbcommon
%python_subpackages

%description
Python binding to the wlroots library using cffi.

%prep
%setup -q -n pywlroots-%{version}
%patch0 -p1

%build
export CFLAGS="-I/usr/include/wayland -I/usr/include/libdrm -I/usr/include/libxkbcommon -I/usr/include/pixman-1 -I/usr/include/libinput $CFLAGS"
%python_exec wlroots/ffi_build.py
%pyproject_wheel

%install
export CFLAGS="-I/usr/include/wayland -I/usr/include/libdrm -I/usr/include/libxkbcommon -I/usr/include/pixman-1 -I/usr/include/libinput $CFLAGS"
%python_exec wlroots/ffi_build.py
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
export CFLAGS="-I/usr/include/wayland -I/usr/include/libdrm -I/usr/include/libxkbcommon -I/usr/include/pixman-1 -I/usr/include/libinput $CFLAGS"
%pytest -vv
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*wlroots*/

%changelog
