#
# spec file for package python-ezdxf
#
# Copyright (c) 2025 SUSE LLC
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


%define packagename ezdxf
Name:           python-ezdxf
Version:        1.2.0
Release:        0
Summary:        Python package for manipulating DXF drawings
License:        MIT
URL:            https://ezdxf.mozman.at/
Source:         https://github.com/mozman/ezdxf/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
# SECTION setup requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module qt5}
# /SECTION
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module fonttools}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module typing_extensions}
Requires:       python-fonttools
Requires:       python-numpy
Requires:       python-pyparsing >= 2.0.1
Requires:       python-typing_extensions
Recommends:     python-matplotlib
Recommends:     python-qt5
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A Python package to create and modify DXF drawings, independent from the
DXF version.

%prep
%autosetup -p1 -n %{packagename}-%{version}
sed -i '1 {/env python/ d}' src/ezdxf/addons/drawing/qtviewer.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ezdxf
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative ezdxf

%postun
%python_uninstall_alternative ezdxf

%check
# text2path: some tests only work with the presence of Arial font family
%pytest_arch -k "not test_814_text2path"

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/ezdxf
%{python_sitearch}/%{packagename}
%{python_sitearch}/%{packagename}-%{version}.dist-info

%changelog
