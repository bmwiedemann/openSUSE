#
# spec file for package uranium
#
# Copyright (c) 2020 SUSE LLC
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


Name:           uranium
Version:        4.7.1
Release:        0
Summary:        Python framework for Desktop applications
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            http://github.com/Ultimaker/Uranium
Source0:        Uranium-%{version}.tar.xz
# X-OPENSUSE-FIX fix cmake install directory.
Patch1:         fix-cmake-install.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libArcus-devel
BuildRequires:  python3-devel >= 3.4.0
# for tests:
BuildRequires:  python3-Twisted
BuildRequires:  python3-cryptography
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-qt5
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
Requires:       python3-cryptography
Recommends:     python3-numpy-stl
BuildArch:      noarch
# No 32bit support in cura-engine anymore
ExcludeArch:    %ix86 %arm

%description
A Python framework for building Desktop applications.

%prep
%setup -q -n Uranium-%version
%patch1 -p1

%build
# Hack, remove LIB_SUFFIX for 64bit, which is correct as uranium is pure python (i.e. noarch)
%cmake -DLIB_SUFFIX="" \
       -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules
%cmake_build

%install
pushd build
%make_install
# uranium uses i18n instead of locale for the path to translation files,
# thus we cannot use %%find_lang
popd
find %{buildroot}%{_datadir}/%{name} -name %{name}.po* -delete
echo '%defattr(644,root,root,755)' > %{name}.lang
find %{buildroot}%{_datadir}/%{name} -name %{name}.mo | sed '
  s:'%{buildroot}'::; s:\(.*/i18n/\)\([^/]\+\)\(.*mo\):%lang(\2) \1\2\3:' \
  >> %{name}.lang
find %{buildroot}%{_datadir}/%{name} -type d -path \*i18n\* | sed '
  s:'%{buildroot}'::; s:\(.*/i18n.*\):%dir \1:' \
  >> %{name}.lang

%check
%{__python3} -m pip freeze
# TestHttpRequestManager has threading issues, see https://github.com/Ultimaker/Uranium/issues/594
%{__python3} -m pytest -v -k 'not TaskManagement.TestHttpRequestManager.py'

%files -f %{name}.lang
%license LICENSE
%doc docs README.md
%{_prefix}/lib/uranium
%{python3_sitelib}/UM
%{_datadir}/uranium
%{_datadir}/cmake/Modules/UraniumTranslationTools.cmake

%changelog
