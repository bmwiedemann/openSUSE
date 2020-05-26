#
# spec file for package python-moksha-common
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-moksha-common
Version:        1.2.5
Release:        0
Summary:        Common components for Moksha
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://mokshaproject.net
Source:         https://files.pythonhosted.org/packages/source/m/moksha.common/moksha.common-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       python-kitchen
Requires:       python-pytz
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module kitchen}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
Common components for Moksha.

%prep
%setup -q -n moksha.common-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/moksha
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if %{with test}
%check
%python_exec setup.py test
%endif

%post
%python_install_alternative moksha

%postun
%python_uninstall_alternative moksha

%files %{python_files}
%license COPYING
%doc AUTHORS README
%python_alternative %{_bindir}/moksha
%{python_sitelib}/*

%changelog
