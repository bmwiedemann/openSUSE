#
# spec file for package python-csvkit
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


%define binaries csvclean csvcut csvformat csvgrep csvjoin csvjson csvlook csvpy csvsort csvsql csvstack csvstat in2csv sql2csv
Name:           python-csvkit
Version:        2.0.1
Release:        0
Summary:        A library of utilities for working with CSV
License:        MIT
URL:            https://github.com/wireservice/csvkit
Source0:        https://files.pythonhosted.org/packages/source/c/csvkit/csvkit-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/wireservice/csvkit/5f22e664121b13d9ff005a9206873a8f97431dca/examples/testdbf_converted.csv
BuildRequires:  %{python_module agate >= 1.6.3}
BuildRequires:  %{python_module agate-dbf >= 0.2.0}
BuildRequires:  %{python_module agate-excel >= 0.2.2}
BuildRequires:  %{python_module agate-sql >= 0.5.3}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy
Requires:       python-agate >=  1.6.3
Requires:       python-agate-dbf >= 0.2.0
Requires:       python-agate-excel
Requires:       python-agate-sql
Requires:       python-openpyxl
Requires:       python-xlrd
Recommends:     python-zstandard
%if %python_version_nodots < 310
Requires:       python-importlib-metadata
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%pyproject_wheel

%install
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
  %python_clone -a %{buildroot}%{_mandir}/man1/${b}.1
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pyunittest discover -s tests/ -v

%post
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b .. "\n"))
  print(rpm.expand("%python_install_alternative " .. b .. ".1%{ext_man}\n"))
end}

%postun
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b .. "\n"))
  print(rpm.expand("%python_uninstall_alternative " .. b .. ".1%{ext_man}\n"))
end}

%files %{python_files}
%license COPYING
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b .. "\n"))
  print(rpm.expand("%python_alternative %{_mandir}/man1/" .. b .. ".1%{ext_man}" .. "\n"))
end}
%{python_sitelib}/csvkit
%{python_sitelib}/csvkit-%{version}.dist-info

%changelog
