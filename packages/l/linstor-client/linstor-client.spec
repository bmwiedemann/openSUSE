#
# spec file for package linstor-client
#
# Copyright (c) 2022 SUSE LLC
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
%define python_linstor 1.12
Name:           linstor-client
Version:        1.12.0
Release:        0
Summary:        DRBD distributed resource management utility
License:        GPL-3.0-only
Group:          Productivity/Clustering/HA
URL:            https://github.com/LINBIT/linstor-client
Source:         https://pkg.linbit.com//downloads/linstor/%{name}-%{version}.tar.gz
Patch1:         change-location-of-bash-completion.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module linstor >= %{python_linstor}}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-linstor >= %{python_linstor}}
%python_subpackages

%description
This client program communicates to a linstor controller node which manages the DRBD9 resources.

%package -n linstor
Summary:        Binaries of linstor client
Group:          Productivity/Clustering/HA

%description -n linstor
Binaries of linstor client

%prep
%setup -q
%patch1 -p1

sed -i '/^#!/d' linstor_client_main.py \
                linstor_client/consts.py \
                linstor_client/utils.py

%build
# man pages included in tarball
%python_build

%install
#python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --prefix=%{_prefix} --record=INSTALLED_FILES
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}

%files -n linstor
%{_bindir}/linstor
%{_datadir}/bash-completion/completions/linstor

%changelog
