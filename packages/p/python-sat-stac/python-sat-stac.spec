#
# spec file for package python-sat-stac
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
# from imp import load_source
%global skip_python312 1
%global skip_python313 1
%define packagename sat-stac
Name:           python-sat-stac
Version:        0.4.1
Release:        0
Summary:        A library for reading and working with Spatio-Temporal Asset Catalogs
License:        MIT
URL:            https://github.com/sat-utils/sat-stac
Source:         https://files.pythonhosted.org/packages/source/s/sat-stac/sat-stac-%{version}.tar.gz
BuildRequires:  %{python_module python-dateutil >= 2.7.5}
BuildRequires:  %{python_module requests >= 2.19.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.7.5
Requires:       python-requests >= 2.19.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Sat-search is a Python 3 library and a command line tool for discovering
and downloading publicly available satellite imagery using a conformant
API such as sat-api.

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
for p in %{packagename} ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
# This archive does not have test files.
# The archive in github has it, but need network connection for test.

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/%{packagename}
%{python_sitelib}/*egg-info
%{python_sitelib}/satstac

%changelog
