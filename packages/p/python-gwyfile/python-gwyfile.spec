#
# spec file for package python-gwyfile
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


%define packagename gwyfile
Name:           python-gwyfile
Version:        0.2.0
Release:        0
Summary:        Pure Python implementation of the Gwyddion file format
License:        MIT
URL:            https://github.com/tuxu/gwyfile
Source:         https://github.com/tuxu/gwyfile/archive/%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Fix_depreciated_fromstring_warning.patch andythe_great@pm.me -- Fix fromstring depreciated to frombuffer warning during testing.
Patch0:         Fix_depreciated_fromstring_warning.patch
# PATCH-FIX-OPENSUSE python312.patch
Patch1:         python312.patch
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Pure Python implementation of the Gwyddion file format.

%prep
%autosetup -p1 -n %{packagename}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.rst
%{python_sitelib}/%{packagename}
%{python_sitelib}/%{packagename}-%{version}.dist-info

%changelog
