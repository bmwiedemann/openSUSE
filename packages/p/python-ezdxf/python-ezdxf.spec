#
# spec file for package python-ezdxf
#
# Copyright (c) 2020 SUSE LLC
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ezdxf
Version:        0.13.1
Release:        0
Summary:        Python package for manipulating DXF drawings
License:        MIT
URL:            https://ezdxf.mozman.at/
Source:         https://github.com/mozman/ezdxf/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module geomdl}
BuildRequires:  %{python_module numpy >= 1.2.1}
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-geomdl
Requires:       python-numpy >= 1.2.1
Requires:       python-pyparsing >= 2.0.1
Requires:       python-scipy >= 0.6.0
Requires:       python-wheel
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A Python package to create and modify DXF drawings, independent from the
DXF version.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/dxfpp
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative dxfpp

%post
%python_install_alternative dxfpp

%postun
%python_uninstall_alternative dxfpp

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/dxfpp
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}

%changelog
