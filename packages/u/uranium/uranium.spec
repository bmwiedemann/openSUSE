#
# spec file for package uranium
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


%define UM_1_minor 6

Name:           uranium
%define sversion        4.9
Version:        4.9.0
Release:        0
Summary:        Python framework for Desktop applications
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Ultimaker/Uranium
Source0:        https://github.com/Ultimaker/Uranium/archive/%{sversion}.tar.gz#/%{name}-%{version}.tar.gz
# X-OPENSUSE-FIX fix cmake install directory.
Patch1:         fix-cmake-install.patch
BuildRequires:  cmake
#BuildRequires:  gcc-c++
# for tests:
BuildRequires:  python3-Arcus >= %{version}
BuildRequires:  python3-Twisted
BuildRequires:  python3-cryptography
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-qt5
BuildRequires:  python3-scipy
BuildRequires:  python3-shapely
# END for tests
Requires:       python3-Arcus
Requires:       python3-cryptography
Recommends:     python3-numpy-stl
BuildArch:      noarch
# No 32bit support in cura-engine anymore
ExcludeArch:    %ix86 %arm
# Registered in UM/Qt/Bindings/Bindings.py
Provides:       qt5qmlimport(UM.1) = %{UM_1_minor}

%description
A Python framework for building Desktop applications.

%prep
%setup -q -n Uranium-%sversion
%patch1 -p1

# Sanity check
UM_1_LARGEST_MINOR=$(\
  sed -e '/qmlRegister\(Singleton\)\?Type/ { s/.*"UM",.*1, *\([0-9]\+\).*/\1/ p } ; d' \
  UM/Qt/Bindings/Bindings.py | sort -g -u | tail -n 1 )
test "${UM_1_LARGEST_MINOR}" -eq "%{UM_1_minor}" || exit 1

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
%{__python3} -m pytest -v -k 'not TestHttpRequestManager.py'

%files -f %{name}.lang
%license LICENSE
%doc docs README.md
%{_prefix}/lib/uranium
%{python3_sitelib}/UM
%{_datadir}/uranium
%{_datadir}/cmake/Modules/UraniumTranslationTools.cmake

%changelog
