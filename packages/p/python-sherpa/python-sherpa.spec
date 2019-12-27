#
# spec file for package python-sherpa
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
%define         skip_python2 1
Name:           python-sherpa
Version:        4.12.0
Release:        0
Summary:        Modeling and fitting package for scientific data analysis
License:        GPL-3.0-only
URL:            https://github.com/sherpa/sherpa/
Source:         https://github.com/sherpa/sherpa/archive/%{version}.tar.gz#/sherpa-%{version}.tar.gz
# PATCH-FIX-UPSTREAM config_with_build.patch -- https://github.com/sherpa/sherpa/pull/714
Patch0:         config_with_build.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-six
ExcludeArch:    %{ix86}
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.3}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module six}
BuildRequires:  xauth
BuildRequires:  xorg-x11-server
# /SECTION
%python_subpackages

%description
Sherpa is the CIAO modeling and fitting application. It enables the
user to construct models from definitions and fit those models to
data, using a variety of statistics and optimization methods.

%prep
%setup -q -n sherpa-%{version}
%autopatch -p1
sed -i 's|#stk-location|stk-location|' setup.cfg
sed -i 's|#group-location|group-location|' setup.cfg

%build
%{python_expand sed -i 's|stk-location=.*|stk-location=build/%{_lib}/python%{$python_version}/site-packages/stk.so|' setup.cfg
sed -i 's|group-location=.*|group-location=build/%{_lib}/python%{$python_version}/site-packages/group.so|' setup.cfg
%{$python_build}
}

%install
%{python_expand sed -i 's|stk-location=.*|stk-location=build/%{_lib}/python%{$python_version}/site-packages/stk.so|' setup.cfg
sed -i 's|group-location=.*|group-location=build/%{_lib}/python%{$python_version}/site-packages/group.so|' setup.cfg
%{$python_install}
}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv sherpa sherpa_temp
%python_expand ls -l %{buildroot}%{$python_sitearch}/sherpa/utils/
ls -l *build*/*/*/
%pytest_arch %{buildroot}%{$python_sitearch}/sherpa/
mv sherpa_temp sherpa

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/sherpa_test
%python3_only %{_bindir}/sherpa_smoke
%{python_sitearch}/*

%changelog
