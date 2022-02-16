#
# spec file for package python-wakeonlan
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-orangebox
Version:        0.2.0
Release:        0
License:        GPL-3.0-or-later
Summary:        Betaflight blackbox flight recorder parser
Group:          Development/Languages/Python
Url:            https://github.com/atomgomba/orangebox
#!RemoteAssetUrl: git+https://github.com/atomgomba/orangebox#v0.2.0
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives

BuildArch:      noarch
%python_subpackages

%description

%prep
%setup -q -n orangebox -c -T
cp -a %_sourcedir/orangebox/* .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bb2csv
%python_clone -a %{buildroot}%{_bindir}/bbsplit

%post
%python_install_alternative bb2csv
%python_install_alternative bbsplit

%postun
%python_uninstall_alternative bb2csv
%python_uninstall_alternative bbsplit

%files %{python_files}
%python_alternative %_bindir/bb2csv
%python_alternative %_bindir/bbsplit
%{python_sitelib}/*

