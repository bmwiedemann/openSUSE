#
# spec file for package python-ezdxf
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-ezdxf
Version:        0.16.3
Release:        0
Summary:        Python package for manipulating DXF drawings
License:        MIT
URL:            https://ezdxf.mozman.at/
Source:         https://github.com/mozman/ezdxf/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
# SECTION setup requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module geomdl}
BuildRequires:  %{python_module pytest-xvfb}
# /SECTION
# SECTION optional runtime requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module qt5}
# /SECTION
BuildRequires:  %{python_module pyparsing >= 2.0.1}
Requires:       python-pyparsing >= 2.0.1
Recommends:     python-matplotlib
Recommends:     python-qt5
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
A Python package to create and modify DXF drawings, independent from the
DXF version.

%prep
%setup -q -n %{packagename}-%{version}
# remove unused script interpreter line
sed -i '1 {/env python/ d}' src/ezdxf/addons/drawing/qtviewer.py

%build
%python_build

%install
%python_install
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
%{python_sitearch}/%{packagename}-%{version}*-info
%{python_sitearch}/%{packagename}

%changelog
