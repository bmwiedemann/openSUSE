#
# spec file for package python-pako
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pako
Version:        0.2.3
Release:        0
Summary:        The universal package manager library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/pako
Source:         https://files.pythonhosted.org/packages/source/p/pako/pako-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Often, scripts need to install system dependencies using the native package
manager of the user's OS. Typically, this is solved by having some bash script
that runs apt-get, assuming the user is on Ubuntu. Smarter scripts use hand
crafted code to detect the user's platform and aggregate a set of dependencies
on a few of the more popular platforms. Our approach is different:
  * Parse package format (devel/debug/normal library or executable)
  * Look up package managers that exist in PATH
  * Format parsed package with common package convention of package manager

More on https://github.com/MycroftAI/pako

%prep
%setup -q -n pako-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pako
rm -f %{buildroot}%{_prefix}/pako/LICENSE

%post
%python_install_alternative pako

%postun
%python_uninstall_alternative pako

%files %{python_files}
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/pako

%changelog
