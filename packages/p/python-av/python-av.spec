#
# spec file for package python-av
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-av
Version:        18.1.0
Release:        0
Summary:        Python bindings for FFmpeg's libraries
License:        BSD-3-Clause
URL:            https://github.com/PyAV-Org/PyAV
Source:         https://files.pythonhosted.org/packages/source/a/av/av-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.1.0}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Pythonic bindings for FFmpeg's libraries.

%prep
%autosetup -p1 -n av-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyav
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/av/filter/*.{c,h}

%post
%python_install_alternative pyav

%postun
%python_uninstall_alternative pyav

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/pyav
%{python_sitearch}/av
%{python_sitearch}/av-%{version}.dist-info

%changelog
