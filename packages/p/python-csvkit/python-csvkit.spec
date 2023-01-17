#
# spec file for package python-csvkit
#
# Copyright (c) 2023 SUSE LLC
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
%define binaries csvclean csvcut csvformat csvgrep csvjoin csvjson csvlook csvpy csvsort csvsql csvstack csvstat in2csv sql2csv
%define         skip_python2 1
%define         skip_python36 1
Name:           python-csvkit
Version:        1.1.0
Release:        0
Summary:        A library of utilities for working with CSV
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/csvkit
Source0:        https://files.pythonhosted.org/packages/source/c/csvkit/csvkit-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/wireservice/csvkit/5f22e664121b13d9ff005a9206873a8f97431dca/examples/testdbf_converted.csv
BuildRequires:  %{python_module SQLAlchemy >= 0.9.3}
BuildRequires:  %{python_module Sphinx >= 1.0.7}
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module agate >= 1.6.1}
BuildRequires:  %{python_module agate-dbf >= 0.2.0}
BuildRequires:  %{python_module agate-excel >= 0.2.2}
BuildRequires:  %{python_module agate-sql >= 0.5.3}
BuildRequires:  %{python_module dbf >= 0.9.3}
BuildRequires:  %{python_module et_xmlfile}
BuildRequires:  %{python_module jdcal}
BuildRequires:  %{python_module openpyxl >= 2.2.0.b1}
BuildRequires:  %{python_module python-dateutil >= 2.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  %{python_module xlrd >= 0.9.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
CSVkit is a library of utilities for working with CSV. It is inspired
by pdftk, gdal and the original csvcut utility by Joe Germuska and
Aaron Bycoffe.

%prep
%setup -q -n csvkit-%{version}
# find and remove unneeded shebangs
find csvkit -name "*.py" | xargs sed -i '1 {/^#!/ d}'
# agate-dbf >= 0.2.2 creates uppercase fieldnames for this example file -- gh#wireservice/csvkit#1073
%if %{pkg_vcmp python3-agate-dbf >= 0.2.2}
cp %{SOURCE1} examples/testdbf_converted.csv
%endif

%build
%python_build

%install
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec -m unittest discover -s tests/ -v

%post
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b .. "\n"))
end}

%postun
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b .. "\n"))
end}

%files %{python_files}
%license COPYING
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b .. "\n"))
end}
%{python_sitelib}/csvkit-%{version}*-info
%{python_sitelib}/csvkit/

%changelog
