#
# spec file for package python-pyModis
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{!?license: %global license %doc}
%define         oldpython python
Name:           python-pyModis
Version:        2.0.9
Release:        0
License:        GPL-2.0-or-later
Summary:        Python library for MODIS data
Url:            http://www.pymodis.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pymodis/pyModis-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       %{oldpython}-pymodis = %{version}
Obsoletes:      %{oldpython}-pymodis < %{version}
%endif
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
The Moderate Resolution Imaging Spectroradiometer (MODIS) is a
payload imaging sensor built by Santa Barbara Remote Sensing that was
launched into Earth orbit by NASA in 1999 on board the Terra (EOS AM)
Satellite, and in 2002 on board the Aqua (EOS PM) satellite.
pyModis is a Python library to download and process MODIS data from
NASA servers.

%prep
%setup -q -n pyModis-%{version}
# Fix non-executable-script
sed -i -e '/^#!\//, 1d' pymodis/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/modis_convert.py %{buildroot}%{_bindir}/modis_convert
mv %{buildroot}%{_bindir}/modis_download.py %{buildroot}%{_bindir}/modis_download
mv %{buildroot}%{_bindir}/modis_download_from_list.py %{buildroot}%{_bindir}/modis_download_from_list
mv %{buildroot}%{_bindir}/modis_mosaic.py %{buildroot}%{_bindir}/modis_mosaic
mv %{buildroot}%{_bindir}/modis_multiparse.py %{buildroot}%{_bindir}/modis_multiparse
mv %{buildroot}%{_bindir}/modis_parse.py %{buildroot}%{_bindir}/modis_parse
mv %{buildroot}%{_bindir}/modis_quality.py %{buildroot}%{_bindir}/modis_quality

%python_clone -a %{buildroot}%{_bindir}/modis_convert
%python_clone -a %{buildroot}%{_bindir}/modis_download
%python_clone -a %{buildroot}%{_bindir}/modis_download_from_list
%python_clone -a %{buildroot}%{_bindir}/modis_mosaic
%python_clone -a %{buildroot}%{_bindir}/modis_multiparse
%python_clone -a %{buildroot}%{_bindir}/modis_parse
%python_clone -a %{buildroot}%{_bindir}/modis_quality

%post
%{python_install_alternative modis_convert modis_download modis_download_from_list modis_mosaic modis_multiparse modis_parse modis_quality}

%postun
%python_uninstall_alternative modis_convert

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license COPYING
%python_alternative %{_bindir}/modis_convert
%python_alternative %{_bindir}/modis_download
%python_alternative %{_bindir}/modis_download_from_list
%python_alternative %{_bindir}/modis_mosaic
%python_alternative %{_bindir}/modis_multiparse
%python_alternative %{_bindir}/modis_parse
%python_alternative %{_bindir}/modis_quality
%{python_sitelib}/*

%changelog
