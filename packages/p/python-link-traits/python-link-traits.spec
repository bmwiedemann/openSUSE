#
# spec file for package python-link-traits
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


%define skip_python2 1
%define packagename link_traits
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-link-traits
Version:        1.0.3
Release:        0
Summary:        A fork to traitlets' link and dlink to link traits in addition to traitlets
License:        BSD-3-Clause
URL:            https://github.com/hyperspy/link_traits
Source:         https://github.com/hyperspy/link_traits/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-traits
Suggests:       python-traitlets
BuildArch:      noarch
%python_subpackages

%description
A fork to traitlets' link and dlink to link traits in addition to traitlets.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING.md
%doc README.md
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}

%changelog
