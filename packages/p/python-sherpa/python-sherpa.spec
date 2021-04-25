#
# spec file for package python-sherpa
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python36 1
Name:           python-sherpa
Version:        4.13.0
Release:        0
Summary:        Modeling and fitting package for scientific data analysis
License:        GPL-3.0-only
URL:            https://github.com/sherpa/sherpa/
Source:         https://github.com/sherpa/sherpa/archive/%{version}.tar.gz#/sherpa-%{version}.tar.gz
Patch1:         reproducible.patch
# PATCH-FIX-UPSTREAM - https://github.com/sherpa/sherpa/issues/970
Patch2:         sherpa-fix-aarch64.patch
# PATCH-FIX-UPSTREAM sherpa-numpy-1.20.patch badshah400@gmail.com - Fix test errors with numpy 1.20 [https://github.com/sherpa/sherpa/pull/1092]
Patch3:         sherpa-numpy-1.20.patch
# PATCH-FIX-UPSTREAM sherpa-mpl-3.4.patch -- https://github.com/sherpa/sherpa/pull/1125
Patch4:         sherpa-mpl-3.4.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun):update-alternatives
ExcludeArch:    %{ix86}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.3}
BuildRequires:  %{python_module pytest-xvfb}
# Highly recommended by upstream when building from source https://sherpa.readthedocs.io/en/latest/install.html#building-from-source
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module matplotlib}
# /SECTION
%python_subpackages

%description
Sherpa is the CIAO modeling and fitting application. It enables the
user to construct models from definitions and fit those models to
data, using a variety of statistics and optimization methods.

%prep
%setup -q -n sherpa-%{version}
%autopatch -p1
sed -i "s|#fftw=local|fftw=local|" setup.cfg
sed -i "s|#fftw-include[-_]dirs.*$|fftw-include-dirs=%{_includedir}|" setup.cfg
sed -i "s|#fftw-lib-dirs.*$|fftw-lib-dirs=%{_libdir}|" setup.cfg
sed -i "s|#fftw-libraries|fftw-libraries|" setup.cfg

sed -i "s|/lib/|/%{_lib}/|" helpers/sherpa_config.py

%build
cp -r extern extern0
%{python_expand %{$python_build}
rm -r extern
cp -r extern0 extern
}

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/sherpa_test
%python_clone -a %{buildroot}%{_bindir}/sherpa_smoke
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%{python_expand # REMOVE HASHBANGS FROM NON-EXEC FILES
sed -i "1{/\\/usr\\/bin\\/env python/d}" %{buildroot}%{$python_sitearch}/sherpa/optmethods/ncoresde.py
sed -i "1{/\\/usr\\/bin\\/env python/d}" %{buildroot}%{$python_sitearch}/sherpa/optmethods/ncoresnm.py
sed -i "1{/\\/usr\\/bin\\/env python/d}" %{buildroot}%{$python_sitearch}/sherpa/optmethods/opt.py
sed -i "1{/\\/usr\\/bin\\/env python/d}" %{buildroot}%{$python_sitearch}/sherpa/utils/akima.py
}

%check
# avoid conftest import mismatch
mv sherpa sherpa_temp
# astropy 4.2 fits header warning
donttest+="test_load_case_3"
%pytest_arch --pyargs sherpa -k "not ($donttest)"

%post
%python_install_alternative sherpa_smoke
%python_install_alternative sherpa_test

%postun
%python_uninstall_alternative sherpa_smoke
%python_uninstall_alternative sherpa_test

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/sherpa_test
%python_alternative %{_bindir}/sherpa_smoke
%{python_sitearch}/sherpa
%{python_sitearch}/sherpa-%{version}*-info
%{python_sitearch}/stk.so
%{python_sitearch}/group.so

%changelog
