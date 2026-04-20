#
# spec file for package linstor-client
#
# Copyright (c) 2026 SUSE LLC and contributors
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
BuildRequires:  %{python_module linstor >= %{python_linstor}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-linstor >= %{python_linstor}}
BuildArch:      noarch
%python_subpackages

%description
This client program communicates to a linstor controller node which manages the DRBD9 resources.

%package -n linstor
Summary:        Binaries of linstor client
Group:          Productivity/Clustering/HA

%description -n linstor
Binaries of linstor client

%prep
%autosetup -p1

sed -i '/^#!/d' linstor_client_main.py \
                linstor_client/consts.py \
                linstor_client/utils.py

%build
# man pages included in tarball
%pyproject_wheel

%install
%pyproject_install
# Move bash-completion, pip can't write outside of sitelib
mv -v %{buildroot}%{python3_sitelib}/usr/share %{buildroot}/usr
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
# And clean up
rm -r %{buildroot}%{$python_sitelib}/usr
}

%files %{python_files}
%{python_sitelib}/linstor_client
%{python_sitelib}/linstor_client-%{version}.dist-info
%{python_sitelib}/linstor_client_main.py
%pycache_only %{python_sitelib}/__pycache__/linstor_client_main.*.pyc

%files -n linstor
%{_bindir}/linstor
%{_datadir}/bash-completion/completions/linstor

%changelog
