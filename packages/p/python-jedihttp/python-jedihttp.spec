#
# spec file for package python-jedihttp
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
Name:           python-jedihttp
Version:        0+git.1497381496.75b8b74
Release:        0
Summary:        HTTP/JSON wrapper around Jedi
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        Apache-2.0
Group:          Development/Libraries
URL:            https://github.com/vheon/JediHTTP
Source:         %{name}-%{version}.tar.xz
Patch0:         build.patch
# For tests
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module hamcrest}
BuildRequires:  %{python_module jedi}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module waitress}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bottle
Requires:       python-jedi
Requires:       python-waitress
Requires:       update-alternatives
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
HTTP/JSON wrapper around Jedi primarily created to allow using
jedi for python3 completion in YouCompleteMe.

%prep
%setup -q
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jedihttp-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative jedihttp-server

%postun
%python_uninstall_alternative jedihttp-server

%files %{python_files}
%license LICENSE
%doc README.md NOTICE
%python_alternative %{_bindir}/jedihttp-server
%{_bindir}/jedihttp-server-%{python_bin_suffix}
%{python_sitelib}/jedihttp
%{python_sitelib}/jedihttp-*.egg-info

%changelog
