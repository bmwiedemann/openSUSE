#
# spec file for package python-libversion
#
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           python-libversion
Version:        1.2.4
Release:        0
Summary:        Python bindings for libversion
License:        MIT
URL:            https://github.com/repology/py-libversion
Source:         https://files.pythonhosted.org/packages/source/l/libversion/libversion-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libversion) >= 2.7.0
%python_subpackages

%description
Libversion is an advanced version string comparison library. It can
compare versions of software packages, including complex cases like
1.2-x.3~alpha4. Is is used by the Repology project.

This package contains the Python bindings for libversion.

%prep
%autosetup -p1 -n libversion-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitearch}/libversion
%{python_sitearch}/libversion-%{version}.dist-info

%changelog
