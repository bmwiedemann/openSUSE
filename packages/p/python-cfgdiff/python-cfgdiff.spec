#
# spec file for package python-cfgdiff
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cfgdiff
Version:        0.0.0+git.1487961889.dc4e96e
Release:        0
Summary:        Cfgdiff -- diff(1) all your configuration files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evgeni/cfgdiff
Source:         cfgdiff-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
### SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module lxml}
## /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-configobj
Requires:       python-dnspython
Requires:       python-lxml
Provides:       cfgdiff
BuildArch:      noarch
%python_subpackages

%description
cfgdiff will try to parse your configuration files, fetching all
the relevant keys and values from them and then pretty-printing
them in the original format.
These results are then diffed and the diff is shown to you.

cfgdiff currently supports the following formats:
 - INI using Python's ConfigParser library
 - JSON using Python's JSON library
 - YAML if the Python YAML library is installed
 - XML if the Python lxml library is installed

%prep
%setup -q -n cfgdiff-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/cfgdiff

%post
%python_install_alternative cfgdiff

%postun
%python_uninstall_alternative cfgdiff

%check
%python_exec -m unittest discover test/ -v

%files %{python_files}
%license LICENSE README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/cfgdiff
%{_mandir}/man1/cfgdiff.1%{?ext_man}

%changelog
