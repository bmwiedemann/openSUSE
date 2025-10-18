#
# spec file for package python-cchardet
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define skip_python2 1
%define modname faust-cchardet
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-cchardet
Version:        2.1.19
Release:        0
Summary:        CChardet is high speed universal character encoding detector
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
URL:            https://github.com/faust-streaming/cChardet
Source:         https://files.pythonhosted.org/packages/source/f/faust-cchardet/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(uchardet)
# provide the PyPI name
Provides:       python-faust-cchardet = %{version}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
cChardet is high speed universal character encoding detector. - binding to `uchardet`_.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cchardetect
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch src/tests

%pre
%python_libalternatives_reset_alternative cchardetect

%post
%python_install_alternative cchardetect

%postun
%python_uninstall_alternative cchardetect

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/cchardetect
%{python_sitearch}/cchardet
%{python_sitearch}/%(echo %{modname}|tr '-' '_')-%{version}*-info

%changelog
