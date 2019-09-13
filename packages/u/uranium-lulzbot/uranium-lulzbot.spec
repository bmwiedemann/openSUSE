#
# spec file for package uranium-lulzbot
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


Name:           uranium-lulzbot
Conflicts:      uranium
Version:        3.6.18
Release:        0
Summary:        3D printer control software: python UI stack
License:        AGPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            https://code.alephobjects.com/diffusion/U/uranium.git
Source0:        Uranium-%{version}.tar.xz
Patch1:         fix-build.patch
# PATCH-FIX-OPENSUSE fix Qt 5.12 with current python qt snapshot
Patch2:         fix_qt5.12.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel >= 3.5.0
Recommends:     python3-numpy-stl

%description
Cura is an engine for processing 3D models
into 3D printing instruction for Ultimaker and other GCode based 3D printers.
It is part of the larger open source project called "Cura".

Uranium is the Python framework for the Cura UI.

%prep
%setup -q -n Uranium-%version
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%{optflags}"
export CFLAGS
sed -i 's/PythonInterp 3.5.0/PythonInterp 3.4.0/' CMakeLists.txt
%cmake 
make %{?_smp_mflags}

%install
%if 0%{?suse_version}
pushd build
%make_install
popd
%else
# Fedora
%make_install
%endif
# uranium uses i18n instead of locale for the path to translation files,
# thus we cannot use %%find_lang
find %{buildroot}%{_datadir}/uranium -name uranium.po* -delete
echo '%defattr(644,root,root,755)' > %{name}.lang
find %{buildroot}%{_datadir}/uranium -name uranium.mo | sed '
  s:'%{buildroot}'::; s:\(.*/i18n/\)\([^/]\+\)\(.*mo\):%lang(\2) \1\2\3:' \
  >> %{name}.lang
find %{buildroot}%{_datadir}/uranium -type d -path \*i18n\* | sed '
  s:'%{buildroot}'::; s:\(.*/i18n.*\):%dir \1:' \
  >> %{name}.lang
# fix cmake install dir
mv %{buildroot}/%{_datadir}/cmake* %{buildroot}/%{_datadir}/cmake

%files -f %{name}.lang
%doc docs README.md
%license LICENSE
%{python3_sitelib}/UM
%{_prefix}/lib/uranium
%dir %{_datadir}/uranium
%{_datadir}/uranium/resources
%{_datadir}/cmake

%changelog
