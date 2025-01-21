#
# spec file for package python-igwn-segments
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


%define modname igwn_segments
Name:           python-igwn-segments
Version:        2.0.0
Release:        0
Summary:        Representations of semi-open intervals
License:        GPL-3.0-or-later
URL:            https://igwn-segments.readthedocs.io/en/stable/
Source:         https://files.pythonhosted.org/packages/source/i/igwn-segments/igwn_segments-2.0.0.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  fdupes
%python_subpackages

%description
This package provides the segment and segmentlist objects, as well as the
infinity object used to define semi-infinite and infinite segments.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Not pytest, so run tests manually
%{python_expand #
pushd test
export PYTHONPATH=%{buildroot}%{$python_sitearch}
%{_bindir}/$python segments_*.py || exit 1
popd
}

%files %{python_files}
%{python_sitearch}/%{modname}/
%{python_sitearch}/%{modname}-%{version}.dist-info/

%changelog
