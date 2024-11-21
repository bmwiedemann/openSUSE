#
# spec file for package python-av
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
Name:           python-av
Version:        13.1.0
Release:        0
Summary:        Python bindings for FFmpeg's libraries
License:        BSD-3-Clause
URL:            https://github.com/PyAV-Org/PyAV
Source:         https://files.pythonhosted.org/packages/source/a/av/av-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  (libavutil-devel >= 6 with libavutil-devel < 8)
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
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyav
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative pyav

%postun
%python_uninstall_alternative pyav

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/pyav
%{python_sitearch}/av
%{python_sitearch}/av-%{version}-py%{python_version}.egg-info

%changelog
