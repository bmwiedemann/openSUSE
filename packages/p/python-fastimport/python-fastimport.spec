#
# spec file for package python-fastimport
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
Name:           python-fastimport
Version:        0.9.8
Release:        0
Summary:        Fastimport parser in Python
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/jelmer/python-fastimport
Source:         https://files.pythonhosted.org/packages/source/f/fastimport/fastimport-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is the Python parser that was originally developed for
bzr-fastimport, but extracted so it can be used by other projects.

It is currently used by bzr-fastimport and dulwich. hg-fastimport and
git-remote-hg use a slightly modified version of it.

%prep
%setup -q -n fastimport-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/fast-import-query
%python_clone -a %{buildroot}%{_bindir}/fast-import-info
%python_clone -a %{buildroot}%{_bindir}/fast-import-filter
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest fastimport.tests.test_suite

%post
%python_install_alternative fast-import-query
%python_install_alternative fast-import-info
%python_install_alternative fast-import-filter

%postun
%python_uninstall_alternative fast-import-query
%python_uninstall_alternative fast-import-info
%python_uninstall_alternative fast-import-filter

%files %{python_files}
%doc NEWS README.md
%license COPYING
%{python_sitelib}/fastimport*
%python_alternative %{_bindir}/fast-import-filter
%python_alternative %{_bindir}/fast-import-info
%python_alternative %{_bindir}/fast-import-query

%changelog
